"""Provides some basic database functionality on which to build bots.
"""

import structlog

from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from db.base import BASE
from db.candles import Candles
from db.holdings import Holdings
from db.transactions import Transactions

class DatabaseHandler():
    """Class that serves as the interface for bots to use to interact with the database.
    """

    def __init__(self, database_config):
        """Initializes the DatabaseHandler class.

        Args:
            database_config (dict): A dictionary containing configuration for databases.
        """

        connection_string = self.__create_connection_string(database_config)
        engine = create_engine(connection_string)
        BASE.metadata.create_all(engine)
        session = sessionmaker(bind=engine)
        self.session = session()
        self.logger = structlog.get_logger()

        self.tables = {
            "candles": Candles,
            "holdings": Holdings,
            "transactions": Transactions
        }


    def __create_connection_string(self, database_config):
        """Creates a SQL connection string depending on what is configured.

        Args:
            database_config (dict): A dictionary containing configuration for databases.

        Returns:
            str: A SQL connection string.
        """

        connection_string = database_config['engine'] + "://"
        if database_config['username'] and database_config['password']:
            connection_string += ':'.join([
                database_config['username'],
                database_config['password']])

        if database_config['host']:
            connection_string += '@' + database_config['host']

        if database_config['port']:
            connection_string += ':' + database_config['port']

        if database_config['db_name']:
            connection_string += '/' + database_config['db_name']

        return connection_string


    def read_rows(self, table_name, filter_args={}):
        """Returns a query object containing the contents of the requested table.

        Args:
            table_name (str): the string representation of the database table to query.
            filter_args (dict): A dictionary of query filter values.

        Returns:
            sqlalchemy.Query: A sqlalchemy query object with applied filters.
        """

        return self.session.query(self.tables[table_name]).filter_by(**filter_args)


    def create_row(self, table_name, create_args):
        """Attempts to create a record in the requested table.

        Args:
            table_name (str): the string representation of the database table to query.
            create_args (dict): A dictionary of column value mappings.

        Returns:
            bool: Was the create a success?
        """

        create_success = True
        try:
            self.session.add(self.tables[table_name](**create_args))
            self.session.commit()
        except SQLAlchemyError:
            create_success = False
            self.logger.error("Failed to create holding record!", create_args=create_args)
            self.session.rollback()
        return create_success


    def update_row(self, table_name, row, update_args={}):
        """Attempts to update a record isn the requested table.

        Args:
            holding (Holdings): An instance of the holding class to apply the update to.
            update_args (dict): A dictionary of column value mappings.

        Returns:
            bool: Was the update a success?
        """

        update_success = True
        try:
            self.session.query(self.tables[table_name]).filter_by(id=row.id).update(update_args)
            self.session.commit()
        except SQLAlchemyError:
            update_success = False
            self.logger.error("Failed to update holding record!", update_args=update_args)
            self.session.rollback()
        return update_success
