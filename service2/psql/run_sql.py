
import getpass
import logging
from psql_conn import get_psql_connection
from encryption import encrypt_password

#######################################################

format = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

def execute_sql(password: str, password_flag: bool):

    logger.info("Running SQL test...")

    if not password:
        logger.error("No password provided. it cannot be empty.")
        return

    # encrypt password and use the encrypted value for connection
    encrypted_password = encrypt_password(password)

    conn = None

    try:
        conn = get_psql_connection(
            host='localhost',
            port=5432,
            dbname='prasad_test',
            user='postgres',
            password=encrypted_password,
            password_encrypted=password_flag
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        result = cur.fetchone()
        logger.info(f"PostgreSQL version: {result}")
        cur.close()

    except Exception as e:
        logger.error(f"Error executing SQL test: {e}")
        raise

    finally:
        if conn:
            conn.close()
            logger.info("Database connection closed.")


def main():
    # runtime user inputs
    password = getpass.getpass("Enter the password here: ")  
    password_encryption_flag = input("Enter 'True' if password is encrypted, otherwise 'False': ")

    execute_sql(password, password_encryption_flag)

if __name__ == "__main__":
    main()