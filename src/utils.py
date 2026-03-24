import os
import logging
import datetime
from typing import Dict

def get_project_root() -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_file_paths(directory: str) -> list:
    return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def get_log_level(level: str) -> int:
    logging_levels: Dict[str, int] = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    return logging_levels.get(level.upper())

def get_current_timestamp() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log_message(level: str, message: str) -> None:
    """Logs a message with the specified level."""
    log_level = get_log_level(level)
    logging.basicConfig(level=log_level)
    logging.log(log_level, message)

def get_config_file_path(config_name: str = 'config.json') -> str:
    """Returns the path to the config file."""
    return os.path.join(get_project_root(), 'config', config_name)