# 导入应用模块
from app import app
from common.path import ROOT_DIR
from component.ConfigManager import config_manager
from uvicorn import run

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
