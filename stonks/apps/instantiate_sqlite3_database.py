"""
Functions that interact with sqlite database. Zero SQL should be written here.
"""

import re
import sqlite3

import stonks.config as config
import stonks.database.sql.data_instantiate as data_instantiate
import stonks.database.sql.sqlite_create as stonks_sqlite

logger = config.logger


def instantiate_sqlite_database_without_table_overwrite(cxn_string: str):
    """
    Central function for creating the SQL database for housing data.
    :param cxn_string: (str) The string used in sqlite3.connect(`cxn_string`) use to instantiate a db cxn.
    """
    with sqlite3.connect(cxn_string) as cxn:
        # Create symbols table
        try:
            cxn.execute(stonks_sqlite.sql_create_table_symbol())
        except sqlite3.OperationalError as op_err:
            if re.search(r"""OperationalError\('table "\w+" already exists'\)""", repr(op_err)):
                # If result not None: table exists, do not overwrite
                pass
            else:
                # Unexpected error
                logger.error(f'Error in creating symbols table: {repr(op_err)}')
                raise op_err
        # create candlesticks table
        try:
            cxn.execute(stonks_sqlite.sql_create_table_candlestick())
        except sqlite3.OperationalError as op_err:
            if re.search(r"""OperationalError\('table "\w+" already exists'\)""", repr(op_err)):
                # If result not None: table exists, do not overwrite
                pass
            else:
                # Unexpected error
                logger.error(f'Error in creating symbols table: {repr(op_err)}')
                raise op_err
        # create source table
        try:
            cxn.execute(stonks_sqlite.sql_create_table_source())
        except sqlite3.OperationalError as op_err:
            if re.search(r"""OperationalError\('table "\w+" already exists'\)""", repr(op_err)):
                # If result not None: table exists, do not overwrite
                pass
            else:
                # Unexpected error
                logger.error(f'Error in creating symbols table: {repr(op_err)}')
                raise op_err

        # Instantiate data
        cxn.execute(data_instantiate.sql_insert_finnhub_to_source)
        cxn.commit()


def test_instant_sqlite_db() -> None:
    instantiate_sqlite_database_without_table_overwrite(config.cxn_string_sqlite3)
    config.logger.info(f'Database instantiated to: {config.cxn_string_sqlite3}')


def instantiate_database(cxn: object):
    # TODO: make a connection-independent solution for prepping database from scratch

    return


if __name__ == '__main__':
    test_instant_sqlite_db()
    pass
