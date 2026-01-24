

import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Optional, Dict, Any
import logging
from encryption import decrypt_password  # Assuming this is a custom module for decryption

###########################################

format = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)


def get_psql_connection(
        host: str,
        port: int,
        dbname: str,
        user: str,
        password: str,
        password_encrypted: bool = False,
        **kwargs) -> 'psycopg2.extensions.connection':
    """
    Establish a connection to a PostgreSQL database.

    :param host: Database host address
    :param port: Database port number
    :param dbname: Name of the database
    :param user: Database user name
    :param password: Database user password
    :return: A connection object to the PostgreSQL database
    """

    try:
        logger.info(f"#### Connecting to PostgreSQL database: {dbname}")

        if password_encrypted:
            password = decrypt_password(password)   

        conn_params = {
            'host': host,
            'port': port,
            'dbname': dbname,
            'user': user,
            'password': password
        }

        connection = psycopg2.connect(**conn_params, cursor_factory=RealDictCursor)
        logger.info(f"Successfully connected to the database: {dbname}")

        return connection
    
    except Exception as e:
        logger.error(f"Failed to connect to PostgreSQL database - {dbname}: {e}")
        raise

# Example usage:
# conn = get_psql_connection(host='localhost', port=5432, dbname='prasad_test', user='postgres', password='xxxxxxxx')

