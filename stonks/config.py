"""
Establish runtime config here.

DO NOT HARDCODE ANY VARIABLES HERE.

Reading the key/value pair from the config object requires you to first index the section then index the key.
    e.g.: input: config['SectionOfInterest']['KeyOfInterest'] -> output: 'value of interest'
Another way to od it is using the object method:
    e.g.: input: config.get('section', 'key') -> output: 'value of interest'
All values read from the config.ini file are string so type conversion must be made for non-string information.

When sections not found: configparser.NoSectionError
When keys not found: configparser.NoOptionError
"""

from ast import literal_eval  # For evaluating tuples,lists from config file
from pathlib import Path
import configparser
import os
import sqlalchemy
import sqlite3
import sys
import time

from stonks import logger_config

is_debug_mode = False


#######

BASE_PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_PROJECT_PATH not in sys.path: sys.path.insert(0, BASE_PROJECT_PATH)


# Instantiate convenience variables to be moved into config file later


# Instantiate variables for later use
config_file_name = 'config.ini'
default_log_file_name = 'default.log'
default_log_folder_path = Path(BASE_PROJECT_PATH, 'logs').absolute()
valid_db_cxns = {'MYSQL', 'SQLITE', 'SQLITE3'}
# Load up config file
configuration = configparser.ConfigParser()
configuration.read(os.path.join(BASE_PROJECT_PATH, config_file_name))

FINNHUB_TOKEN = configuration.get('FINNHUB', 'TOKEN', raw=True)

########################################################################################################################

# Resolve logger variables
config_file_log_folder_path = configuration.get('LOGGING', 'LOG_FILE_FOLDER_PATH')
config_file_log_folder_path = config_file_log_folder_path if config_file_log_folder_path else default_log_folder_path
config_file_name = configuration.get('LOGGING', 'LOG_FILE_NAME', fallback=default_log_file_name)
log_file_complete_path = str(Path(config_file_log_folder_path, config_file_name).absolute())
assert os.path.isdir(config_file_log_folder_path), f'Path does not exist: {config_file_log_folder_path}'

# Instantiate logger
logger = logger_config.create_generic_logger(
    logger_name=configuration.get('LOGGING', 'LOGGER_NAME'),
    log_format=configuration.get('LOGGING', 'LOG_FORMAT', raw=True),
    stdout_log_level=configuration.get('LOGGING', 'STREAM_LOG_LEVEL', fallback=None),
    file_log_level=configuration.get('LOGGING', 'FILE_LOG_LEVEL', fallback=None),
    file_log_file_path=log_file_complete_path,
)


########################################################################################################################

# Instantiate DB cxn
db_cxn_type = configuration.get('APP', 'DB_CONNECTION').upper()
sqlite_file_name = configuration.get('SQLITE', 'FILE_NAME')
sqlite_save_path = configuration.get('SQLITE', 'LOCATION', fallback=None)
if is_debug_mode:
    print(f'sqlite_save_path = {sqlite_save_path}, type={type(sqlite_save_path)}')
if not sqlite_save_path:
    sqlite_save_path = BASE_PROJECT_PATH
else:
    if not os.path.isdir(sqlite_save_path):
        raise ValueError(f'The following path is not valid: {sqlite_save_path}')
cxn_string_sqlite3 = os.path.join(sqlite_save_path, sqlite_file_name)

if db_cxn_type == 'MYSQL':
    # TODO
    db_cxn = sqlalchemy.create_engine()
    raise NotImplementedError(f'MYSQL cxn type not yet implemented')
elif 'SQLITE' in db_cxn_type:
    db_cxn = sqlite3.connect(cxn_string_sqlite3)
else:
    raise ValueError(f'Invalid database connection type specified. Value found: {db_cxn_type}')


if __name__ == '__main__':

    pass
