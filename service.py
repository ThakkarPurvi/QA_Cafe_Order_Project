# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do

from db import select_query, data_query, cursor

""" ======== CREATE ORDER ======== """
def create_order():
    qa_cafe_order_query = "INSERT INTO qa_cafe_order (customer_name, order_date, item_name, item_quantity, item_price, total_cost)" \
                  "VALUES ('Vidya Sharma', '2023-02-09', 'Coffee', 2, 3.5, 7.00)";
    cursor.execute(qa_cafe_order_query)
    return True
# create_order()



""" ======== READ AN ORDER BY ID ======== """
def read_by_id(order_id):
    query = f"Read FROM qa_cafe_order where order_id = {order_id}"
    return select_query(query)


""" ======== READ ALL ORDER ======== """
def read_all_qa_cafe_order():
    query = "SELECT * FROM qa_cafe_order"
    return select_query(query)


""" ======== UPDATE AN ORDER ======== """
def update_order_id(order_id):
    query = f"UPDATE FROM qa_cafe_order where order_id = {order_id}"
    return data_query(query)
# print(update_order_id())


""" ======== DELETE AN ORDER BY ID ======== """
def delete_order_id(order_id):
    query = f"DELETE FROM qa_cafe_order where order_id = {order_id}"
    return data_query(query)
# print(delete_order_id())


""" ======== DELETE ALL ORDERS ======== """
def delete_all_order_id(order_id):
    query = f"DELETE FROM qa_cafe_order where order_id = {order_id}"
    return data_query(query)
# print(delete_all_order_id())



# print(read_all_qa_cafe_order("qa_cafe_order"))

# conn.commit()

