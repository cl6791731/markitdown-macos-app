# -*- mode: python ; coding: utf-8 -*-
# MarkItDown macOS App - PyInstaller 配置

import sys
from pathlib import Path

block_cipher = None
src_dir = Path(SPECPATH)

a = Analysis(
    [str(src_dir / 'main.py')],
    pathex=[str(src_dir)],
    binaries=[],
    datas=[
        (str(src_dir / 'resources' / 'icon.png'), 'resources'),
    ],
    # Let PyInstaller collect magika data files next to the module
    hookspath=[str(src_dir / 'hooks')],
    hooksconfig={},
    hiddenimports=[
        'markitdown',
        'markitdown._markitdown',
        'markitdown._base_converter',
        'markitdown._stream_info',
        'markitdown._uri_utils',
        'markitdown._exceptions',
        'markitdown.converters',
        'markitdown.converters._pdf_converter',
        'markitdown.converters._docx_converter',
        'markitdown.converters._xlsx_converter',
        'markitdown.converters._pptx_converter',
        'markitdown.converters._html_converter',
        'markitdown.converters._csv_converter',
        'markitdown.converters._epub_converter',
        'markitdown.converters._plain_text_converter',
        'markitdown.converters._zip_converter',
        'markitdown.converters._outlook_msg_converter',
        'markitdown.converters._image_converter',
        'markitdown.converters._audio_converter',
        'markitdown.converters._ipynb_converter',
        'markitdown.converters._rss_converter',
        'markitdown.converters._youtube_converter',
        'markitdown.converters._bing_serp_converter',
        'markitdown.converters._wikipedia_converter',
        'markitdown.converter_utils',
        'markitdown.converter_utils.docx',
        'markitdown.converter_utils.docx.pre_process',
        'markitdown.converter_utils.docx.math',
        'markitdown.converter_utils.docx.math.omml',
        'pdfminer',
        'pdfplumber',
        'magika',
        'magika.magika',
        'magika.types',
        'magika.types.model',
        'magika.types.content_type_label',
        'magika.types.content_type_info',
        'magika.types.magika_result',
        'magika.types.magika_prediction',
        'magika.types.prediction_mode',
        'magika.types.status',
        'magika.cli',
        'markdownify',
        'bs4',
        'lxml',
        'pandas',
        'openpyxl',
        'xlrd',
        'python_pptx',
        'mammoth',
        'olefile',
        'charset_normalizer',
        'defusedxml',
        'PIL',
        'numpy',
        'onnxruntime',
    ],
    runtime_hooks=[],
    excludes=[
        'matplotlib', 'scipy', 'torch', 'tensorflow',
        'tkinter', 'unittest', 'test', 'tests',
        'pytest', 'IPython', 'notebook',
        'azure.ai', 'azure.identity',
        'pydub', 'speech_recognition', 'youtube_transcript_api',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MarkItDown',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MarkItDown',
)

app = BUNDLE(
    coll,
    name='MarkItDown.app',
    icon=str(src_dir / 'resources' / 'icon.icns'),
    bundle_identifier='com.markitdown.desktop',
    version='0.1.6',
    info_plist={
        'CFBundleName': 'MarkItDown',
        'CFBundleDisplayName': 'MarkItDown',
        'CFBundleIdentifier': 'com.markitdown.desktop',
        'CFBundleVersion': '0.1.6',
        'CFBundleShortVersionString': '0.1.6',
        'NSHumanReadableCopyright': 'Copyright Microsoft Corporation. MIT License.',
        'NSHighResolutionCapable': True,
        'CFBundleDocumentTypes': [
            {
                'CFBundleTypeName': 'PDF Document',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': ['com.adobe.pdf'],
            },
            {
                'CFBundleTypeName': 'Word Document',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': ['org.openxmlformats.wordprocessingml.document'],
            },
            {
                'CFBundleTypeName': 'PowerPoint Presentation',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': ['org.openxmlformats.presentationml.presentation'],
            },
            {
                'CFBundleTypeName': 'Excel Workbook',
                'CFBundleTypeRole': 'Viewer',
                'LSItemContentTypes': ['org.openxmlformats.spreadsheetml.sheet'],
            },
        ],
    },
)
