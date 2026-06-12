# MarkItDown macOS App

基于 [Microsoft MarkItDown](https://github.com/microsoft/markitdown) 开源项目，将其核心转换引擎封装为 macOS 原生桌面应用，开箱即用，无需命令行操作。

## 功能特性

- **20+ 种格式支持** — PDF、DOCX、PPTX、XLSX、CSV、HTML、EPUB、JSON、图片、音频等一键转 Markdown
- **中英文双语** — 界面语言一键切换，实时生效
- **拖放即转** — 直接拖入文件开始转换
- **实时预览** — 转换结果即时预览，暗色主题 Markdown 阅读体验
- **一键保存 / 复制** — 结果保存为 .md 文件或复制到剪贴板
- **批量处理** — 同时添加多个文件批量转换

## 安装方式

1. 从 [Releases](https://github.com/cl6791731/markitdown-macos-app/releases) 下载 `MarkItDown-v0.1.6.dmg`
2. 打开 DMG，将 **MarkItDown.app** 拖入 **Applications** 文件夹
3. 首次打开：右键点击应用 → 选择「打开」（macOS 安全提示）

## 系统要求

- macOS 12.0 Monterey 及以上
- Apple Silicon (M1/M2/M3/M4) 或 Intel

## 从源码构建

```bash
# 克隆仓库
git clone https://github.com/cl6791731/markitdown-macos-app.git
cd markitdown-macos-app

# 创建虚拟环境并安装依赖
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 直接运行
python main.py

# 打包为 .app
pyinstaller markitdown_app.spec --clean --noconfirm
```

## 项目结构

```
├── main.py                 # 应用入口
├── app.py                  # 主窗口 GUI（PySide6）
├── worker.py               # 后台转换线程
├── i18n.py                 # 中英文双语模块
├── markitdown_app.spec     # PyInstaller 打包配置
├── hooks/
│   └── hook-magika.py      # magika 模型打包 hook
├── resources/
│   ├── icon.icns           # 应用图标
│   └── icon.png            # 图标源文件
└── requirements.txt
```

## 致谢

核心转换引擎来自 [Microsoft MarkItDown](https://github.com/microsoft/markitdown)，由微软 AutoGen 团队开发，采用 MIT 许可证开源。

## 联系方式

如有问题或建议，欢迎扫码添加微信交流：

<p align="center">
  <img src="wechat-qrcode.png" width="256" alt="微信二维码"/>
</p>

## 许可证

本项目基于 [MIT License](LICENSE) 开源。
