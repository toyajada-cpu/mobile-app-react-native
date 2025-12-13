import os
import logging
import datetime

def get_project_root():
    """Returns the project root directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def get_file_paths(directory):
    """Returns a list of files in the specified directory."""
    return [os.path.join(directory, file) for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

def get_log_level(level):
    """Maps a string level to a logging level."""
    logging_levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    return logging_levels.get(level.upper())

def get_current_timestamp():
    """Returns the current timestamp."""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')