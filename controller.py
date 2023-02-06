"""The controller acts as the API for the app, in this case it will exist as a terminal based app
    using inputs and if statements to specify what the app should do
    It will run commands from the service file, which in turn uses the DB file to
    query and create data and will return the data back to the user"""

import sys
from service import update_order_id, delete_order_id, delete_all_order_id
from service import create_order, read_all_qa_cafe_order, read_by_id

THANK_YOU = "----------- Thank you for your using QA Cafe, have a nice day! -----------"

def qa_cafe_app():
    """Cafe App"""
    print(
        """
        Welcome to the QA Cafe, what would you like to do? 
        1. Create an order
        2. Read an order
        3. Read all Orders
        4. Update an order
        5. Delete an order
        6. Delete all orders
        7. Exit
        """
    )
    running = True

    while running:
        choice = int(input("Please choose a number (1-7): "))
        if choice == 1:
            print(create_order())
        elif choice == 2:
            print(read_by_id())
        elif choice == 3:
            print(read_all_qa_cafe_order())
        elif choice == 4:
            print(update_order_id())
        elif choice == 5:
            print(delete_order_id())
        elif choice == 6:
            print(delete_all_order_id())
        elif choice == 7:
            sys.exit(f"{THANK_YOU}")
        else:
            print("Incorrect choice.. try again..")
        end_choice = input("\nDo you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            sys.exit(f"{THANK_YOU}")

qa_cafe_app()

# This is a placeholder for correct code for this message.
