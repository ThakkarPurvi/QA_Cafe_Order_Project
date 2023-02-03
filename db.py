# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3 as sql

conn = sql.connect("qa_cafe-db")
conn.execute("PRAGMA foreign_keys = 1 ")
cursor = conn.cursor()

def creating_table():
    sql_file = open("qa_cafe_order.sql")
    sql_string = sql_file.read()
    # print(sql_string)
    # Running our sql command using our cursor
    cursor.executescript(sql_string)

# Reading data
def select_query(query):
    return cursor.execute(query).fetchall()

def qa_cafe_order_query(query):
    return cursor.execute(query).fetchall()

# Manipulating data
def data_query(query):
    cursor.execute(query)
    return True

def commit_changes():
    conn.commit()