"""MarkItDown macOS App - 后台转换工作线程 / Background conversion worker"""

from pathlib import Path
from PySide6.QtCore import QThread, Signal


class ConvertWorker(QThread):
    """后台文件转换线程 / Background file conversion thread"""

    finished = Signal(str, str)   # (file_path, markdown_result)
    error = Signal(str, str)      # (file_path, error_message)

    def __init__(self, file_path: str, parent=None):
        super().__init__(parent)
        self.file_path = file_path

    def run(self):
        try:
            from markitdown import MarkItDown

            md = MarkItDown()
            result = md.convert_local(self.file_path)
            self.finished.emit(self.file_path, result.markdown)
        except Exception as e:
            self.error.emit(self.file_path, str(e))
