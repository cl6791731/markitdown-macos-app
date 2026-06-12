"""MarkItDown macOS App - 中英文双语模块 / Bilingual i18n module"""

LANG = {
    "zh": {
        # 窗口 / Window
        "app_name": "MarkItDown",
        "window_title": "MarkItDown - 文档转 Markdown",
        # 菜单 / Menus
        "menu_file": "文件",
        "menu_edit": "编辑",
        "menu_help": "帮助",
        "menu_open": "打开文件...",
        "menu_open_shortcut": "Ctrl+O",
        "menu_quit": "退出",
        "menu_quit_shortcut": "Ctrl+Q",
        "menu_about": "关于",
        # 工具栏 / Toolbar
        "toolbar_add": "添加文件",
        "toolbar_add_tip": "添加需要转换的文件",
        "toolbar_clear": "清空列表",
        "toolbar_clear_tip": "清空文件列表和输出",
        "toolbar_save": "保存 Markdown",
        "toolbar_save_tip": "将转换结果保存为 .md 文件",
        "toolbar_copy": "复制结果",
        "toolbar_copy_tip": "复制 Markdown 到剪贴板",
        "toolbar_lang": "中/EN",
        "toolbar_lang_tip": "切换语言 / Switch Language",
        # 拖拽区 / Drop Zone
        "dropzone_text": "将文件拖放到此处",
        "dropzone_sub": "或点击上方「添加文件」按钮选择文件",
        "dropzone_formats": "支持格式：PDF、DOCX、PPTX、XLSX、XLS、CSV、HTML、EPUB、JSON、图片、音频等",
        # 文件列表 / File List
        "col_filename": "文件名",
        "col_status": "状态",
        "col_action": "操作",
        "status_waiting": "等待中",
        "status_converting": "转换中...",
        "status_done": "完成",
        "status_error": "失败",
        "status_empty": "无文本",
        "status_empty_file": "{} 未提取到文本（可能是扫描件或纯图片）",
        "btn_preview": "预览",
        "btn_retry": "重试",
        "btn_remove": "移除",
        # 预览区 / Preview
        "preview_placeholder": "选择一个已转换的文件查看 Markdown 预览",
        "preview_title": "Markdown 预览",
        # 状态栏 / Status Bar
        "status_ready": "就绪",
        "status_loading": "正在加载文件...",
        "status_converting_file": "正在转换: {}",
        "status_converted": "已转换: {}",
        "status_error_file": "转换失败: {} - {}",
        "status_batch_done": "批量转换完成 ({}/{})",
        "status_saved": "已保存: {}",
        "status_copied": "已复制到剪贴板",
        "status_cleared": "已清空",
        # 对话框 / Dialogs
        "dialog_open_title": "选择要转换的文件",
        "dialog_save_title": "保存 Markdown 文件",
        "dialog_about_title": "关于 MarkItDown",
        "dialog_error_title": "错误",
        "dialog_confirm_title": "确认",
        "confirm_clear": "确定要清空所有文件和输出吗？",
        "error_no_selection": "请先选择一个文件",
        "error_convert": "文件转换失败：\n{}",
        # 关于 / About
        "about_version": "版本: {}",
        "about_desc": "MarkItDown 是微软开源的文档转 Markdown 工具，\n支持 PDF、DOCX、PPTX、XLSX、图片、音频等 20+ 种格式。\n\n基于 Microsoft MarkItDown (MIT License)",
        "about_repo": "项目地址: https://github.com/microsoft/markitdown",
        # 格式描述 / Format descriptions
        "format_pdf": "PDF 文档",
        "format_docx": "Word 文档",
        "format_pptx": "PowerPoint 演示文稿",
        "format_xlsx": "Excel 工作簿",
        "format_xls": "旧版 Excel 工作簿",
        "format_csv": "CSV 表格",
        "format_html": "HTML 网页",
        "format_epub": "EPUB 电子书",
        "format_json": "JSON 文件",
        "format_text": "纯文本文件",
        "format_md": "Markdown 文件",
        "format_image": "图片文件",
        "format_audio": "音频文件",
        "format_outlook": "Outlook 邮件",
        "format_zip": "ZIP 压缩包",
        "format_ipynb": "Jupyter Notebook",
        "format_msg": "Outlook 邮件 (.msg)",
        "format_xml": "XML/RSS 文件",
    },
    "en": {
        # Window
        "app_name": "MarkItDown",
        "window_title": "MarkItDown - Document to Markdown Converter",
        # Menus
        "menu_file": "File",
        "menu_edit": "Edit",
        "menu_help": "Help",
        "menu_open": "Open Files...",
        "menu_open_shortcut": "Ctrl+O",
        "menu_quit": "Quit",
        "menu_quit_shortcut": "Ctrl+Q",
        "menu_about": "About",
        # Toolbar
        "toolbar_add": "Add Files",
        "toolbar_add_tip": "Add files to convert",
        "toolbar_clear": "Clear All",
        "toolbar_clear_tip": "Clear file list and output",
        "toolbar_save": "Save Markdown",
        "toolbar_save_tip": "Save conversion result as .md file",
        "toolbar_copy": "Copy Result",
        "toolbar_copy_tip": "Copy Markdown to clipboard",
        "toolbar_lang": "中/EN",
        "toolbar_lang_tip": "Switch Language / 切换语言",
        # Drop Zone
        "dropzone_text": "Drop files here",
        "dropzone_sub": 'or click "Add Files" above',
        "dropzone_formats": "Supported: PDF, DOCX, PPTX, XLSX, XLS, CSV, HTML, EPUB, JSON, Images, Audio, etc.",
        # File List
        "col_filename": "Filename",
        "col_status": "Status",
        "col_action": "Action",
        "status_waiting": "Waiting",
        "status_converting": "Converting...",
        "status_done": "Done",
        "status_error": "Failed",
        "status_empty": "No Text",
        "status_empty_file": "{} — no text extracted (likely a scanned document or image-only file)",
        "btn_preview": "Preview",
        "btn_retry": "Retry",
        "btn_remove": "Remove",
        # Preview
        "preview_placeholder": "Select a converted file to preview Markdown",
        "preview_title": "Markdown Preview",
        # Status Bar
        "status_ready": "Ready",
        "status_loading": "Loading file...",
        "status_converting_file": "Converting: {}",
        "status_converted": "Converted: {}",
        "status_error_file": "Failed: {} - {}",
        "status_batch_done": "Batch complete ({}/{})",
        "status_saved": "Saved: {}",
        "status_copied": "Copied to clipboard",
        "status_cleared": "Cleared",
        # Dialogs
        "dialog_open_title": "Select files to convert",
        "dialog_save_title": "Save Markdown File",
        "dialog_about_title": "About MarkItDown",
        "dialog_error_title": "Error",
        "dialog_confirm_title": "Confirm",
        "confirm_clear": "Are you sure you want to clear all files and output?",
        "error_no_selection": "Please select a file first",
        "error_convert": "File conversion failed:\n{}",
        # About
        "about_version": "Version: {}",
        "about_desc": "MarkItDown is an open-source document-to-Markdown tool by Microsoft.\nSupports PDF, DOCX, PPTX, XLSX, images, audio, and 20+ formats.\n\nBased on Microsoft MarkItDown (MIT License)",
        "about_repo": "Repository: https://github.com/microsoft/markitdown",
        # Format descriptions
        "format_pdf": "PDF Document",
        "format_docx": "Word Document",
        "format_pptx": "PowerPoint Presentation",
        "format_xlsx": "Excel Workbook",
        "format_xls": "Legacy Excel Workbook",
        "format_csv": "CSV Spreadsheet",
        "format_html": "HTML Webpage",
        "format_epub": "EPUB E-book",
        "format_json": "JSON File",
        "format_text": "Plain Text File",
        "format_md": "Markdown File",
        "format_image": "Image File",
        "format_audio": "Audio File",
        "format_outlook": "Outlook Email",
        "format_zip": "ZIP Archive",
        "format_ipynb": "Jupyter Notebook",
        "format_msg": "Outlook Message (.msg)",
        "format_xml": "XML/RSS File",
    },
}


def t(key: str, lang: str = "zh", *args) -> str:
    """获取翻译字符串 / Get translated string"""
    text = LANG.get(lang, LANG["zh"]).get(key, key)
    if args:
        return text.format(*args)
    return text


# 文件过滤器 (用于 QFileDialog) / File filters for QFileDialog
FILE_FILTERS_ZH = (
    "所有支持的文件 (*.pdf *.docx *.pptx *.xlsx *.xls *.csv *.html *.htm"
    " *.epub *.json *.jsonl *.txt *.text *.md *.markdown *.ipynb"
    " *.jpg *.jpeg *.png *.gif *.bmp *.tiff *.webp"
    " *.wav *.mp3 *.msg *.zip *.xml *.rss *.mhtml *.mht);;"
    "PDF 文档 (*.pdf);;"
    "Word 文档 (*.docx);;"
    "PowerPoint (*.pptx);;"
    "Excel 工作簿 (*.xlsx *.xls);;"
    "CSV 表格 (*.csv);;"
    "HTML 网页 (*.html *.htm *.mhtml *.mht);;"
    "EPUB 电子书 (*.epub);;"
    "JSON 文件 (*.json *.jsonl);;"
    "纯文本 (*.txt *.text *.md *.markdown);;"
    "图片 (*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.webp);;"
    "音频 (*.wav *.mp3);;"
    "Outlook 邮件 (*.msg);;"
    "ZIP 压缩包 (*.zip);;"
    "Jupyter Notebook (*.ipynb);;"
    "XML/RSS (*.xml *.rss);;"
    "所有文件 (*)"
)

FILE_FILTERS_EN = (
    "All Supported Files (*.pdf *.docx *.pptx *.xlsx *.xls *.csv *.html *.htm"
    " *.epub *.json *.jsonl *.txt *.text *.md *.markdown *.ipynb"
    " *.jpg *.jpeg *.png *.gif *.bmp *.tiff *.webp"
    " *.wav *.mp3 *.msg *.zip *.xml *.rss *.mhtml *.mht);;"
    "PDF Documents (*.pdf);;"
    "Word Documents (*.docx);;"
    "PowerPoint (*.pptx);;"
    "Excel Workbooks (*.xlsx *.xls);;"
    "CSV Spreadsheets (*.csv);;"
    "HTML Pages (*.html *.htm *.mhtml *.mht);;"
    "EPUB E-books (*.epub);;"
    "JSON Files (*.json *.jsonl);;"
    "Plain Text (*.txt *.text *.md *.markdown);;"
    "Images (*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.webp);;"
    "Audio (*.wav *.mp3);;"
    "Outlook Messages (*.msg);;"
    "ZIP Archives (*.zip);;"
    "Jupyter Notebooks (*.ipynb);;"
    "XML/RSS (*.xml *.rss);;"
    "All Files (*)"
)

SAVE_FILTER_ZH = "Markdown 文件 (*.md);;所有文件 (*)"
SAVE_FILTER_EN = "Markdown Files (*.md);;All Files (*)"
