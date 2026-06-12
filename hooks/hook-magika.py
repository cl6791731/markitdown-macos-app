"""PyInstaller hook for magika — copy model + config data alongside the module."""
from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('magika', includes=['config/**', 'models/**'])
