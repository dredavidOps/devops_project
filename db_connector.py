# importing pymysql module to facilitate database connection
import pymysql


# function to connect to the database
def db_connect():
    schema_name = 'mydb'
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    passwd = 'Testing123'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=schema_name)
    return conn


def create_records(user_id: object, user_name: object) -> object:
    connection = db_connect()
    cursor = connection.cursor()
    # insert data into the table
    query = f"INSERT into mydb.users (user_id, user_name) VALUES (%s, %s)"
    query_result = cursor.execute(query, (user_id, user_name))
    # commit/save data that has been inserted
    connection.commit()
    cursor.close()
    connection.close()
    return query_result


# reading from the database
def read_records(user_id):
    connection = db_connect()
    cursor = connection.cursor()
    query = f"SELECT * FROM mydb.users WHERE user_id = %s"
    print(f"Executing SQL: {query} with user_id: {user_id}")
    cursor.execute(query, user_id)
    query_result = cursor.fetchone()
    cursor.close()
    connection.close()
    return query_result


# Update records in the database
def update_records(user_id, user_name):
    connection = db_connect()
    cursor = connection.cursor()
    query = f"UPDATE mydb.users SET user_name = %s WHERE user_id = %s"
    cursor.execute(query, (user_name, user_id))
    connection.commit()
    cursor.close()
    connection.close()
    return "Success"


def delete_records(user_id):
    connection = db_connect()
    cursor = connection.cursor()
    query = f"DELETE FROM mydb.users WHERE user_id =%s"
    cursor.execute(query, user_id)
    connection.commit()
    cursor.close()
    connection.close()
    return "Success"


# print(read_records(user_id=2))
# print(create_records(user_id=10, user_name="Charles"))
# update records in DB
# print(update_records(user_id=10, user_name="Pete"))
# print(delete_records(user_id=15))