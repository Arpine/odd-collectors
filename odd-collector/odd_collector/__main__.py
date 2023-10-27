from pathlib import Path

from odd_collector import get_version
from odd_collector.domain.plugin import PLUGIN_FACTORY
from odd_collector_sdk.collector import Collector

from .logger import logger

COLLECTOR_PACKAGE = __package__
CONFIG_PATH = Path().cwd() / "collector_config.yaml"

if __name__ == "__main__":
    logger.info(f"Starting collector. Version: {get_version()}")
    collector = Collector(
        config_path=CONFIG_PATH,
        root_package=COLLECTOR_PACKAGE,
        plugin_factory=PLUGIN_FACTORY,
    )
    collector.run()
