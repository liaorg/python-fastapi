from uvicorn import run
from common.path import ROOT_DIR
from component.ConfigManager import config_manager

# 导入应用模块
from app import app

SRC_FOLDER = ROOT_DIR / 'src'


def main():
    run(
        app='run:app',
        host=config_manager.get_value(["server", "host"]),
        port=config_manager.get_value(["server", "port"]),
        log_level=config_manager.get_value(["log_level"]),
        reload=True,
        reload_dirs=[str(SRC_FOLDER)],
        workers=1,
    )
