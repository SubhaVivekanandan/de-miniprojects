import sys

# load product list
products_list = []
with open('products.txt', 'r') as file:
    for line in file:
        data = line.rstrip()
        products_list.append(data)

# load courier list
couriers_list = []
with open('couriers.txt', 'r') as file:
    for line in file:
        data = line.rstrip()
        couriers_list.append(data)

# create orders_list
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

order_status_list = ["Preparing", "Out for Delivery", "Delivered"]


# function for creating main menu
def main_menu():
    print("---------------------------You are in Main Menu---------------------------------------------------")
    print('--------------------------------------------------------------------------------------------------')
    print(' \n 0.Exit \n 1.Product Menu \n 2.Courier Menu \n 3.Order Menu')
    option = int(input("Select option(0/1/2/3) :"))
    if option == 0:
        sys.exit()  # exits from main menu
    elif option == 1:
        product_menu()  # calls fn for displaying product menu
    elif option == 2:
        courier_menu()  # calls fn for displaying orders menu
    elif option == 3:
        orders_menu()  # calls fn for displaying orders menu

def product_menu():
    print("---------------------------You are in Products Menu-----------------------------")
    print("\n 0.Return to main menu \n 1.Print list of products \n 2.Add a new product to list")
    print(" 3.Update exisisting product in the list \n 4.Delete a product from list")
    option = int(input("Enter your option 0-4 :"))
    print("You have selected :", option)
    if option == 0:
        main_menu()
    elif option == 1:
        print(products_list)
    elif option == 2:
        new_product = input('Enter new product name:')
        products_list.append(new_product)
        print(products_list)
        # Open a file with access mode 'a'
        file_object = open('products.txt', 'a')
        file_object.write("\n"+ new_product)
        # Close the file
        file_object.close()
    elif option == 3:
        for product in products_list:
            index = products_list.index(product)
            print(f" The {product} index value is : {index}")
        user_input_index = int(
            input("Enter the product index value for updating an existing product:"))
        new_product = input('Enter new product name:')
        products_list[user_input_index] = new_product
        print(products_list)
    elif option == 4:
        for product in products_list:
            index = products_list.index(product)
            print(f" The {product} index value is : {index}")
        user_input_index = int(
            input("Enter the product index value for deletion:"))
        del products_list[user_input_index]
        print(products_list)
    product_menu()


def courier_menu():
    print("---------------------------You are in Couriers Menu-----------------------------")
    print("\n 0.Return to main menu \n 1.Print list of couriers \n 2.Add a new courier to list")
    print(" 3.Update exisisting courier in the list \n 4. Delete a courier from list")
    option = int(input("Enter your option 0-4 :"))
    print("You have selected :", option)
    if option == 0:
        main_menu()
    elif option == 1:
        print(couriers_list)
    elif option == 2:
        new_courier = input('Enter new courier name:')
        couriers_list.append(new_courier)
        print(couriers_list)
    elif option == 3:
        for courier in couriers_list:
            index = couriers_list.index(courier)
            print(f" The {courier} index value is : {index}")
        user_input_index = int(
            input("Enter the courier index value for updating an existing courier:"))
        new_courier = input('Enter new courier name:')
        couriers_list[user_input_index] = new_courier
        print(couriers_list)
    elif option == 4:
        for courier in couriers_list:
            index = couriers_list.index(courier)
            print(f" The {courier} index value is : {index}")
        user_input_index = int(
            input("Enter the courier index value for deletion:"))
        del orders_list[user_input_index]
        print(orders_list)
    courier_menu()


def orders_menu():
    print('---------------------------You are in Orders Menu-----------------------------')
    print("\n 0.Return to main menu \n 1.Print the existing  Order List  \n 2.Add a new order to list")
    print(" 3.Update order status in the list \n 4.Add/Update existing order list \n 5.Delete a product from list")
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
        user_input_index = int(
            input("Enter the order index value for updating an existing status value:"))
        print(orders_list[user_input_index]['status'])
        customer_status = input('Enter the customer status:')
        orders_list[user_input_index]['status'] = customer_status
        print(orders_list)
    elif option == 4:
        for item in orders_list:
            index = orders_list.index(item)
            print(f"the {item} is value {index}")
        user_input_index = int(input("Enter the index value:"))
        new_property = input("Enter the age value:")
        if new_property == 'blank':
            print('No further update on Orders list')
        else:
            orders_list[user_input_index]["age"] = new_property
        print(orders_list)
    elif option == 5:
        user_input_index = int(
            input("Enter the order index value for deleting the orders:"))
        del orders_list[user_input_index]
        print(orders_list)
    orders_menu()


main_menu()
