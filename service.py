# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do

from db import select_query, data_query, cursor, commit_changes
from order import *

""" ======== CREATE ORDER ======== """
def create_order():
    qa_cafe_order_query = "INSERT INTO qacafe (customer_name, order_date, item_name, item_quantity, item_price, total_cost)" \
                  "VALUES ('Vidya Sharma', '2023-02-09', 'Coffee', 2, 3.5, 7.00)";
    cursor.execute(qa_cafe_order_query)
    select_query = "SELECT * FROM qacafe"
    print("\n--- Order has been Created ---\n")
    return cursor.execute(select_query).fetchall()
# create_order()



""" ======== READ AN ORDER BY ID ======== """
def read_by_id():
    order_id = int(input("Please enter the order_id you want to view: "))
    query = f"SELECT * FROM qacafe WHERE order_id = {order_id}"
    print(f"\n--- Order id: {order_id} has been displayed. ---\n")
    return select_query(query)


""" ======== READ ALL ORDER ======== """
def read_all_qa_cafe_order():
    query = "SELECT * FROM qacafe"
    print(f"\n--- All orders have been printed below ---")
    return select_query(query)

""" ======== UPDATE AN ORDER ======== """
def update_order_id():
    order_id = input("Please select the order_id you would like to update: ")
    change_name = input("Enter the new name in "" quote marks: ")
    query = f"UPDATE qacafe SET customer_name = {change_name} WHERE order_id = {order_id}"
    print(f"\nNew name: {change_name} has been updated to Order_id: {order_id}")
    print("\n", data_query(query))
    return f"--- Customer Name has been updated ---\n"
# print(update_order_id())


""" ======== DELETE AN ORDER BY ID ======== """
def delete_order_id():
    num = int(input("Please enter the order_id you want to delete: "))
    query = f"DELETE FROM qacafe where order_id = {num}"
    print("\n", data_query(query))
    return f"--- Order id: {num} has been deleted. ---\n"
# print(delete_order_id(order_id))


""" ======== DELETE ALL ORDERS ======== """
def delete_all_order_id():
    query = f"DELETE FROM qacafe"
    print(data_query(query))
    return f"--- Order deleted. ---"
# print(delete_all_order_id())
