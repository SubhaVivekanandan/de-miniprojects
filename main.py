import sys
import csv
from rich.console import Console
import tabulate

console = Console()

# load product list
products_list = []
with open('./products.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    products_list = list(dict_reader)
    file.close()

# load order list
orders_list = []
with open('./orders.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    orders_list = list(dict_reader)
    file.close()

def save_orders_file():
    order_field_names = ['customer_name',
                         'customer_address', 'customer_phone', 'status', 'courier', 'items']
    with open('./orders.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=order_field_names)
        writer.writeheader()
        writer.writerows(orders_list)
    file.close()

def print_orders_list():
    header = orders_list[0].keys()
    rows = [x.values() for x in orders_list]
    print(tabulate.tabulate(rows, header, tablefmt='fancy_outline'))

def save_products_file():
    product_field_names = ['name', 'price']
    with open('./products.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=product_field_names)
        writer.writeheader()
        writer.writerows(products_list)
    file.close()

def print_products_list():
    header = products_list[0].keys()
    rows = [x.values() for x in products_list]
    print(tabulate.tabulate(rows, header, tablefmt='fancy_outline'))

# function for creating main menu
def main_menu_options():
    console.print(
        '''
*************************************[bold yellow]Main Menu!![/bold yellow]************************************
[bold green]
0.Exit
1.Product Menu
2.Courier Menu
3.Order Menu
[/bold green]
************************************************************************************
        '''
    )


def product_menu_options():
    console.print(
        '''
*************************************[bold yellow]Product Menu!![/bold yellow]************************************
[bold green]
0.Return to main menu
1.Print list of products
2.Add a new product to list
3.Update exisisting product in the list
4.Delete a product from list
[/bold green]
************************************************************************************
        '''
    )


def order_menu_options():
    console.print(
        '''
*************************************[bold yellow]Order Menu!![/bold yellow]************************************
[bold green]
0.Return to main menu
1.Print the existing  Order List
2.Add a new order to list
3.Update order status in the list
4.Add/Update existing order list
5.Delete a product from list
[/bold green]
************************************************************************************
        '''
    )


def main():
    main_menu_options()
    option = int(input("Select option(0/1/2/3) :"))
    if option == 0:
        save_products_file()
        console.print(
            '\n[bold yellow]!Exiting Main menu Application!![/bold yellow]****************************************************')
        sys.exit()  # exits from main menu
    elif option == 1:
        product_menu_options()
        product_menu()  # calls fn for displaying product menu
    elif option == 2:
        product_menu()  # calls fn for displaying orders menu
    elif option == 3:
        orders_menu()  # calls fn for displaying orders menu


def product_menu():
    option = int(input("Enter your option 0-4 :"))
    console.print(
        '\n*******************************************************************************')
    print("You have selected :", option)
    if option == 0:
        main()
    elif option == 1:
        print_products_list()
    elif option == 2:
        new_product_name = input('Enter new product name:')
        new_product_price = input('Enter new product price:')
        new_dict = {'name': new_product_name, 'price': new_product_price}
        products_list.append(new_dict)
        save_products_file()
        print_products_list()
    elif option == 3:
        for product in products_list:
            index = products_list.index(product)
            console.print(
                f" The [bold green]{product} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the product index value for an update:"))
        for key, value in products_list[user_input_index].items():
            new_property = input('Enter the values for name & price:')
            if new_property:
                products_list[user_input_index][key] = new_property
            else:
                break
        save_products_file()
        print_products_list()
    elif option == 4:
        for product in products_list:
            index = products_list.index(product)
            console.print(
                f" The [bold green]{product} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the product index value for deletion:"))
        del products_list[user_input_index]
        save_products_file()
        print_products_list()
    product_menu()


def orders_menu():
    order_menu_options()
    option = int(input("Enter your option 0-5 :"))
    console.print(
        '\n*******************************************************************************')
    print("You have selected :", option)
    if option == 0:
        main()
    elif option == 1:
        print_orders_list()
    elif option == 2:
        customer_name = input('Enter new customer name:')
        customer_address = input('Enter the customer address:')
        customer_phone_number = input('Enter the phone number:')
        
        for product in products_list:
            index = products_list.index(product)
            console.print(
                f" The [bold green]{product} [/bold green]index value is : [bold green]{index}[/bold green]")
            
        input_product_index_values = [int(x) for x in input("Enter multiple values\n").split(',')]
        product_index_values = ', '.join(str(x) for x in input_product_index_values)
        
        # //write courier index value
        
        status = "Preparing"
        new_order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone_number,
            "status": status,
            "courier": 1,
            "items": product_index_values
            
        }
        orders_list.append(new_order)
        save_orders_file()
        print_orders_list()
    elif option == 3:
        for order in orders_list:
            index = orders_list.index(order)
            console.print(
                f" The [bold green]{order} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the order index value for updating an existing status value:"))
        print(orders_list[user_input_index]['status'])
        customer_status = input('Enter the customer status:')
        orders_list[user_input_index]['status'] = customer_status
        save_orders_file()
        print_orders_list()
    elif option == 4:
        # wip
        for item in orders_list:
            index = orders_list.index(item)
            print(f"the {item} is value {index}")
        user_input_index = int(input("Enter the index value:"))
        for key, value in orders_list[user_input_index].items():
            property_values = input('Enter the value:')
            if property_values:
                orders_list[user_input_index][key] = property_values
            else:
                break
        save_orders_file()
        print_orders_list()
    elif option == 5:
        for order in orders_list:
            index = orders_list.index(order)
            console.print(
                f" The [bold green]{order} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the order index value for deleting the orders:"))
        del orders_list[user_input_index]
        save_orders_file()
        print_orders_list()
    orders_menu()


if __name__ == "__main__":
    main()
