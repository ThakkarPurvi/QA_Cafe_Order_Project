# The controller acts as the API for the app, in this case it will exist as a terminal based app
# using inputs and if statements to specify what the app should do

# It will run commands from the service file, which in turn uses the DB file to
# query and create data and will return the data back to the user

from service import *


def qa_cafe_app():
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
            print(f"----------- Thank you for your using QA Cafe, have a nice day! -----------")
            exit()
        else:
            print("Incorrect choice.. try again..")
        end_choice = input("Do you want to query more data Y / N: ")
        if end_choice.upper() == "N":
            print(f"----------- Thank you for your using QA Cafe, have a nice day! -----------")
            running = False

qa_cafe_app()


# print(service.read_all_qa_cafe_order())