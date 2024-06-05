import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='database_name',
            user='username',
            password='user password'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None

def insert_record(connection, table, data):
    try:
        cursor = connection.cursor()
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, list(data.values()))
        connection.commit()
        print("Record inserted successfully")
    except Error as e:
        print("Failed to insert record into MySQL table", e)
connection = create_connection()

