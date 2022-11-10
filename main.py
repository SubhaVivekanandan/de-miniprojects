import sys

# creating product list
product_list = ["Coke Zero", "Pepsi", "Fanta"]

# function for creating main menu
def main_menu():
    print("Main Menu")
    print('0.Exit \n 1.Main Menu 2.Order List')
    option = int(input("Select option(0/1/2) :"))
    if option == 0:
        sys.exit()  # exits from main menu
    elif option == 1:
        product_menu()  # calls fn for displaying product menu
    elif option == 2:
        orders_menu()  # calls fn for displaying orders menu


def product_menu():
    print("Product Menu")
    print("0.Return to main menu \n 1.Print list of products \n 2.Add a new product to list")
    print("3.Update exisisting product in the list \n4. Delete a product from list")
    option = int(input("Enter your option 0-4 :"))
    print("You have selected :", option)
    if option == 0:
        main_menu()
    elif option == 1:
        print(product_list)
    elif option == 2:
        new_product = input('Enter new product name:')
        product_list.append(new_product)
        print(product_list)
        
    elif option == 3:
        for product in product_list:
            index = product_list.index(product)
            print(f" The {product} index value is : {index}")
        user_input_index = int(
            input("Enter the product index value for updating an existing product:"))
        new_product = input('Enter new product name:')
        product_list[user_input_index] = new_product
        print(product_list)
    elif option == 4:
        for product in product_list:
            index = product_list.index(product)
            print(f" The {product} index value is : {index}")
        user_input_index = int(
            input("Enter the product index value for deletion:"))
        del product_list[user_input_index]
        print(product_list)
    product_menu()


def orders_menu():
    orders_list = [{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, Manchester, M21 2ER",
        "customer_phone": "0789887334",
        "status": "preparing"
    },
        {
        "customer_name": "Sarah",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "status": "Out-for-Delivery"
    },
        {
        "customer_name": "Paige",
        "customer_address": "Unit 2, 12 Main Street, Birmingham, BH1 2ER",
        "customer_phone": "0789887334",
        "status": "Delivered"
    }
    ]
    print("0.Return to main menu \n 1.Print the existing  Order List  \n 2.Add a new product to list")
    print("3.Update exisisting product in the list \n4. Delete a product from list")
    option = int(input("Enter your option 0-5 :"))
    print("You have selected :", option)
    if option == 0:
        main_menu()
    elif option == 1:
        print(orders_list)
    elif option == 2:
        customer_name = input('Enter new customer name:')
        customer_address = input('Enter the customer address:')
        customer_phone_number = input('Enter the phone number:')
        status = "Preparing"
        new_order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone_number,
            "status": status
        }
        orders_list.append(new_order)
        print(orders_list)
    elif option == 3:
        user_input_index = int(input("Enter the order index value for updating an existing status value:"))
        print(orders_list[user_input_index]['status'])
        customer_status = input('Enter the customer status:')
        orders_list[user_input_index]['status'] = customer_status
        print(orders_list)
    elif option == 4:
        print('wip')
    elif option == 5:
        user_input_index = int(input("Enter the order index value for deleting the orders:"))
        del orders_list[user_input_index]
        print(orders_list)
    orders_menu()

main_menu()
