import mysql.connector
from src.config import MYSQL_CONFIG


def connect_to_mysql():
    """
    Connects to the MySQL database.

    :param host: (str) IP/DNS of server that have de database.
    :param usuario: (str) User for connect to database.
    :param senha: (str) Password for connect to database.
    :param banco: (str) The database where will connect.

    :return: Connection object.

    Exemple: conexao = connect_to_mysql("localhost", "seu_usuario", "sua_senha", "seu_banco")
    """
    try:
        usuario = MYSQL_CONFIG['MYSQLUSER']
        senha = MYSQL_CONFIG['MYSQLPASSWORD']
        host = MYSQL_CONFIG['MYSQLSERVER']
        banco = MYSQL_CONFIG['MYSQLDB']
        # Connect to MySQL
        conn = mysql.connector.connect(
            host=host,
            port=3306,
            user=usuario,
            password=senha,
            database=banco
        )
        print("Connection success to MySQL!")
        return conn
    except mysql.connector.Error as erro:
        print(f"Error on connection to MySQL: {erro}")
        return None


def disconnect_to_mysql(conn):
    """
    Disconnects from the MySQL database.

    :param conn: (str) Connection object.
    :return: None

    :Exemple: disconnect = disconnect_to_mysql(conn)
    """
    if conn:
        conn.close()
        print(f'Client disconnected!')
    else:
        return f'Client error. Error: {conn}'
