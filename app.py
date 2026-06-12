"""MarkItDown macOS App - 主窗口 GUI"""

import os
from pathlib import Path
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QSplitter,
    QLabel, QPushButton, QTableWidget, QTableWidgetItem,
    QTextEdit, QFileDialog, QMessageBox, QStatusBar, QHeaderView,
    QAbstractItemView, QFrame, QSizePolicy, QToolBar, QApplication,
    QMenu,
)
from PySide6.QtCore import Qt, QSettings, QSize, QMimeData, QTimer
from PySide6.QtGui import QAction, QFont, QColor, QDragEnterEvent, QDropEvent, QIcon

from i18n import t, FILE_FILTERS_ZH, FILE_FILTERS_EN, SAVE_FILTER_ZH, SAVE_FILTER_EN
from worker import ConvertWorker

_APP_VERSION = "0.1.6"
_ORG = "MarkItDown"
_APP_ID = "MarkItDownApp"


class DropZone(QFrame):
    """可拖放文件的区域 / Drop zone for files"""

    filesDropped = list  # will be replaced by signal in __init__

    def __init__(self, parent=None):
        super().__init__(parent)
        self._callback = None
        self.setAcceptDrops(True)
        self.setMinimumHeight(120)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._update_style(False)

    def set_callback(self, fn):
        self._callback = fn

    def _update_style(self, hover: bool):
        border_color = "#4A90D9" if hover else "#888888"
        bg = "rgba(74,144,217,0.06)" if hover else "transparent"
        self.setStyleSheet(f"""
            DropZone {{
                border: 2px dashed {border_color};
                border-radius: 12px;
                background: {bg};
            }}
        """)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            self._update_style(True)

    def dragLeaveEvent(self, event):
        self._update_style(False)

    def dropEvent(self, event: QDropEvent):
        self._update_style(False)
        paths = []
        for url in event.mimeData().urls():
            p = url.toLocalFile()
            if p and os.path.isfile(p):
                paths.append(p)
        if paths and self._callback:
            self._callback(paths)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self._callback:
            self._callback(None)  # None signals "open file dialog"


class MarkItDownWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._settings = QSettings(_ORG, _APP_ID)
        self._lang = self._settings.value("language", "zh")
        self._workers: list[ConvertWorker] = []
        self._results: dict[str, str] = {}     # path -> markdown
        self._row_map: dict[str, int] = {}     # path -> table row

        self._init_ui()
        self._retranslate()

    # ── UI 构建 ──────────────────────────────────────────────

    def _init_ui(self):
        self.setMinimumSize(960, 640)
        self.resize(1100, 720)

        # 中央容器
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(8)

        # 工具栏
        self._build_toolbar()

        # 主分割器 (上: 文件列表, 下: 预览)
        splitter = QSplitter(Qt.Orientation.Vertical)

        # ── 上部：文件列表 + 拖拽提示 ──
        upper = QWidget()
        upper_layout = QVBoxLayout(upper)
        upper_layout.setContentsMargins(0, 0, 0, 0)
        upper_layout.setSpacing(6)

        self._dropzone = DropZone()
        self._dropzone.set_callback(self._on_drop_or_click)

        # 拖拽区内部标签（创建一次，切换语言时只更新文本）
        dz_layout = QVBoxLayout(self._dropzone)
        dz_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._dz_main = QLabel()
        self._dz_main.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._dz_main.setStyleSheet("font-size: 16px; font-weight: 600; color: #666; border: none;")
        dz_layout.addWidget(self._dz_main)
        self._dz_sub = QLabel()
        self._dz_sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._dz_sub.setStyleSheet("font-size: 12px; color: #999; border: none;")
        dz_layout.addWidget(self._dz_sub)
        self._dz_fmt = QLabel()
        self._dz_fmt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._dz_fmt.setStyleSheet("font-size: 11px; color: #aaa; border: none; margin-top: 6px;")
        self._dz_fmt.setWordWrap(True)
        dz_layout.addWidget(self._dz_fmt)

        upper_layout.addWidget(self._dropzone)

        self._table = QTableWidget(0, 3)
        self._table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self._table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self._table.horizontalHeader().setStretchLastSection(False)
        self._table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self._table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self._table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self._table.verticalHeader().setVisible(False)
        self._table.setMinimumHeight(120)
        upper_layout.addWidget(self._table, 1)

        splitter.addWidget(upper)

        # ── 下部：Markdown 预览 ──
        lower = QWidget()
        lower_layout = QVBoxLayout(lower)
        lower_layout.setContentsMargins(0, 0, 0, 0)

        self._preview_label = QLabel()
        self._preview_label.setStyleSheet("font-weight: 600; font-size: 13px; padding: 4px 0;")
        lower_layout.addWidget(self._preview_label)

        self._preview = QTextEdit()
        self._preview.setReadOnly(True)
        self._preview.setFont(QFont("Menlo", 12))
        self._preview.setPlaceholderText("")
        self._preview.setStyleSheet("""
            QTextEdit {
                background: #1e1e1e;
                color: #d4d4d4;
                border: 1px solid #3c3c3c;
                border-radius: 6px;
                padding: 10px;
            }
        """)
        lower_layout.addWidget(self._preview, 1)

        splitter.addWidget(lower)
        splitter.setStretchFactor(0, 2)
        splitter.setStretchFactor(1, 3)
        layout.addWidget(splitter, 1)

        # 状态栏
        self._statusbar = QStatusBar()
        self.setStatusBar(self._statusbar)

    def _build_toolbar(self):
        tb = self.addToolBar("Main")
        tb.setMovable(False)
        tb.setIconSize(QSize(22, 22))
        tb.setStyleSheet("""
            QToolBar { spacing: 6px; padding: 4px 8px; }
            QToolBar QToolButton {
                font-size: 13px; font-weight: 500;
                padding: 4px 10px; border-radius: 6px;
            }
            QToolBar QToolButton:hover { background: rgba(0,0,0,0.06); }
            QToolBar QToolButton:pressed { background: rgba(0,0,0,0.10); }
        """)

        self._act_add = QAction("➕", self)
        self._act_add.triggered.connect(lambda: self._on_drop_or_click(None))
        tb.addAction(self._act_add)

        self._act_clear = QAction("🗑️", self)
        self._act_clear.triggered.connect(self._clear_all)
        tb.addAction(self._act_clear)

        tb.addSeparator()

        self._act_save = QAction("💾", self)
        self._act_save.triggered.connect(self._save_markdown)
        tb.addAction(self._act_save)

        self._act_copy = QAction("📋", self)
        self._act_copy.triggered.connect(self._copy_markdown)
        tb.addAction(self._act_copy)

        tb.addSeparator()

        # 语言切换：两个独立按钮
        self._btn_zh = QPushButton("中文")
        self._btn_en = QPushButton("EN")
        for btn in (self._btn_zh, self._btn_en):
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFixedSize(48, 28)
        self._btn_zh.clicked.connect(lambda: self._set_language("zh"))
        self._btn_en.clicked.connect(lambda: self._set_language("en"))
        tb.addWidget(self._btn_zh)
        tb.addWidget(self._btn_en)

    # ── 语言切换 ────────────────────────────────────────────

    def _set_language(self, lang: str):
        if lang == self._lang:
            return
        self._lang = lang
        self._settings.setValue("language", lang)
        self._retranslate()

    def _retranslate(self):
        L = self._lang
        self.setWindowTitle(t("window_title", L))

        # 语言按钮高亮
        self._btn_zh.setStyleSheet(self._lang_btn_style(L == "zh"))
        self._btn_en.setStyleSheet(self._lang_btn_style(L == "en"))

        # 工具栏提示
        self._act_add.setToolTip(t("toolbar_add_tip", L))
        self._act_add.setText(t("toolbar_add", L) + " ➕")
        self._act_clear.setToolTip(t("toolbar_clear_tip", L))
        self._act_clear.setText(t("toolbar_clear", L) + " 🗑️")
        self._act_save.setToolTip(t("toolbar_save_tip", L))
        self._act_save.setText(t("toolbar_save", L) + " 💾")
        self._act_copy.setToolTip(t("toolbar_copy_tip", L))
        self._act_copy.setText(t("toolbar_copy", L) + " 📋")
        self._btn_zh.setToolTip(t("toolbar_lang_tip", L))
        self._btn_en.setToolTip(t("toolbar_lang_tip", L))

        # 拖拽区文本
        self._dz_main.setText(t("dropzone_text", L))
        self._dz_sub.setText(t("dropzone_sub", L))
        self._dz_fmt.setText(t("dropzone_formats", L))

        # 表头
        self._table.setHorizontalHeaderLabels([
            t("col_filename", L), t("col_status", L), t("col_action", L)
        ])

        # 预览
        self._preview_label.setText(t("preview_title", L))
        if not self._results:
            self._preview.setPlaceholderText(t("preview_placeholder", L))

        # 状态栏
        self._statusbar.showMessage(t("status_ready", L))

        # 刷新表格中的状态文本和按钮
        self._refresh_table_texts()

    @staticmethod
    def _lang_btn_style(active: bool) -> str:
        if active:
            return """
                QPushButton {
                    font-size: 12px; font-weight: 600;
                    border: 1px solid #3A7BD5; border-radius: 4px;
                    background: #4A90D9; color: white;
                    padding: 0 8px;
                }
            """
        return """
            QPushButton {
                font-size: 12px; font-weight: 600;
                border: 1px solid #bbb; border-radius: 4px;
                background: #f5f5f5;
                padding: 0 8px;
            }
            QPushButton:hover { background: #e5e5e5; }
        """

    def _refresh_table_texts(self):
        L = self._lang
        status_map = {
            "waiting": t("status_waiting", L),
            "converting": t("status_converting", L),
            "done": t("status_done", L),
            "error": t("status_error", L),
            "empty": t("status_empty", L),
        }
        for row in range(self._table.rowCount()):
            status_item = self._table.item(row, 1)
            if status_item:
                raw = status_item.data(Qt.ItemDataRole.UserRole)
                status_item.setText(status_map.get(raw, raw))
            # 按钮文本
            btn = self._table.cellWidget(row, 2)
            if btn:
                # 重建按钮（简单方式）
                pass

    # ── 文件处理 ────────────────────────────────────────────

    def _on_drop_or_click(self, paths):
        """paths=None 表示点击打开对话框"""
        L = self._lang
        if paths is None:
            filters = FILE_FILTERS_ZH if L == "zh" else FILE_FILTERS_EN
            files, _ = QFileDialog.getOpenFileNames(
                self, t("dialog_open_title", L), "", filters
            )
            if not files:
                return
            paths = files

        for p in paths:
            if p not in self._row_map:
                self._add_file(p)

    def _add_file(self, file_path: str):
        L = self._lang
        row = self._table.rowCount()
        self._table.insertRow(row)
        self._row_map[file_path] = row

        # 文件名
        name_item = QTableWidgetItem(Path(file_path).name)
        name_item.setToolTip(file_path)
        name_item.setData(Qt.ItemDataRole.UserRole, file_path)
        self._table.setItem(row, 0, name_item)

        # 状态
        status_item = QTableWidgetItem(t("status_waiting", L))
        status_item.setData(Qt.ItemDataRole.UserRole, "waiting")
        status_item.setForeground(QColor("#E8A838"))
        self._table.setItem(row, 1, status_item)

        # 操作按钮
        btn = QPushButton(t("btn_remove", L))
        btn.setFixedWidth(60)
        btn.clicked.connect(lambda checked, fp=file_path: self._remove_file(fp))
        self._table.setCellWidget(row, 2, btn)

        self._start_convert(file_path)

    def _start_convert(self, file_path: str):
        L = self._lang
        row = self._row_map.get(file_path)
        if row is None:
            return

        # 更新状态
        status_item = self._table.item(row, 1)
        status_item.setText(t("status_converting", L))
        status_item.setData(Qt.ItemDataRole.UserRole, "converting")
        status_item.setForeground(QColor("#4A90D9"))

        self._statusbar.showMessage(t("status_converting_file", L, Path(file_path).name))

        worker = ConvertWorker(file_path)
        worker.finished.connect(self._on_convert_done)
        worker.error.connect(self._on_convert_error)
        self._workers.append(worker)
        worker.start()

    def _on_convert_done(self, file_path: str, markdown: str):
        L = self._lang
        row = self._row_map.get(file_path)
        if row is None:
            return

        status_item = self._table.item(row, 1)
        btn = QPushButton()
        btn.setFixedWidth(60)

        if markdown and markdown.strip():
            # 有内容
            self._results[file_path] = markdown
            status_item.setText(t("status_done", L))
            status_item.setData(Qt.ItemDataRole.UserRole, "done")
            status_item.setForeground(QColor("#5CB85C"))
            btn.setText(t("btn_preview", L))
            btn.clicked.connect(lambda checked, fp=file_path: self._show_preview(fp))
            self._statusbar.showMessage(t("status_converted", L, Path(file_path).name))
            # 自动显示第一个成功的结果
            if len(self._results) == 1:
                self._show_preview(file_path)
        else:
            # 空结果（扫描PDF、纯图片等）
            status_item.setText(t("status_empty", L))
            status_item.setData(Qt.ItemDataRole.UserRole, "empty")
            status_item.setForeground(QColor("#F0AD4E"))
            btn.setText("—")
            btn.setEnabled(False)
            self._statusbar.showMessage(
                t("status_empty_file", L, Path(file_path).name))

        self._table.setCellWidget(row, 2, btn)
        self._cleanup_worker(file_path)

    def _on_convert_error(self, file_path: str, error_msg: str):
        L = self._lang
        row = self._row_map.get(file_path)
        if row is None:
            return

        status_item = self._table.item(row, 1)
        status_item.setText(t("status_error", L))
        status_item.setData(Qt.ItemDataRole.UserRole, "error")
        status_item.setForeground(QColor("#D9534F"))

        # 更新按钮为「重试」
        btn = QPushButton(t("btn_retry", L))
        btn.setFixedWidth(60)
        btn.clicked.connect(lambda checked, fp=file_path: self._retry_convert(fp))
        self._table.setCellWidget(row, 2, btn)

        self._statusbar.showMessage(t("status_error_file", L, Path(file_path).name, error_msg))
        self._cleanup_worker(file_path)

    def _retry_convert(self, file_path: str):
        self._results.pop(file_path, None)
        self._start_convert(file_path)

    def _remove_file(self, file_path: str):
        row = self._row_map.pop(file_path, None)
        if row is not None:
            self._table.removeRow(row)
            self._results.pop(file_path, None)
            # 重建 row_map
            self._row_map.clear()
            for r in range(self._table.rowCount()):
                item = self._table.item(r, 0)
                if item:
                    fp = item.data(Qt.ItemDataRole.UserRole)
                    if fp:
                        self._row_map[fp] = r

    def _cleanup_worker(self, file_path: str):
        self._workers = [w for w in self._workers if w.isRunning()]

    # ── 预览 ────────────────────────────────────────────────

    def _show_preview(self, file_path: str):
        L = self._lang
        md = self._results.get(file_path)
        if md is None:
            QMessageBox.warning(self, t("dialog_error_title", L),
                                t("error_no_selection", L))
            return
        self._preview.setPlainText(md)
        self._preview_label.setText(f"{t('preview_title', L)} — {Path(file_path).name}")

        # 高亮选中行
        row = self._row_map.get(file_path)
        if row is not None:
            self._table.selectRow(row)

    # ── 工具栏操作 ──────────────────────────────────────────

    def _clear_all(self):
        L = self._lang
        if self._results:
            reply = QMessageBox.question(
                self, t("dialog_confirm_title", L),
                t("confirm_clear", L),
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if reply != QMessageBox.StandardButton.Yes:
                return

        self._table.setRowCount(0)
        self._row_map.clear()
        self._results.clear()
        self._preview.clear()
        self._preview.setPlaceholderText(t("preview_placeholder", L))
        self._statusbar.showMessage(t("status_cleared", L))

    def _save_markdown(self):
        L = self._lang
        # 取当前预览的内容
        text = self._preview.toPlainText()
        if not text:
            QMessageBox.information(self, t("dialog_error_title", L),
                                    t("error_no_selection", L))
            return

        filters = SAVE_FILTER_ZH if L == "zh" else SAVE_FILTER_EN
        path, _ = QFileDialog.getSaveFileName(
            self, t("dialog_save_title", L), "", filters
        )
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
            self._statusbar.showMessage(t("status_saved", L, path))

    def _copy_markdown(self):
        L = self._lang
        text = self._preview.toPlainText()
        if text:
            QApplication.clipboard().setText(text)
            self._statusbar.showMessage(t("status_copied", L))

    def closeEvent(self, event):
        self._settings.sync()
        super().closeEvent(event)
