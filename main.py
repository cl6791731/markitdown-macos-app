"""MarkItDown macOS App - 入口文件 / Entry point"""

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("MarkItDown")
    app.setOrganizationName("MarkItDown")
    app.setApplicationVersion("0.1.6")

    # 设置全局字体
    font = QFont()
    font.setPointSize(13)
    app.setFont(font)

    # macOS 原生样式（不设置 Fusion，保留原生菜单弹出行为）

    from app import MarkItDownWindow
    window = MarkItDownWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
