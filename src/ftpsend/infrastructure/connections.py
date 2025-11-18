from ftpsend.domain.database import Connection

from sqlalchemy import create_engine, text


def mysql_connector(connection: Connection):
    url = f"mysql+pymysql://{connection.username}:{connection.password}@{connection.host}:port/{connection.database}"
    return create_engine(url)


if __name__ == "__main__":
    conn = Connection("piter", "piter", "ftp_send_db")

    mysql_connection = mysql_connector(conn)
    mysql_connection.connect()
