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

#load couriers list
couriers_list = []
with open('./couriers.csv', 'r') as file:
    dict_reader = csv.DictReader(file)
    couriers_list = list(dict_reader)
    file.close()

#saving in orders.csv file    
def save_orders_file():
    success = False
    order_field_names = ['customer_name',
                         'customer_address', 'customer_phone', 'status', 'courier', 'items']
    try:
        with open('./orders.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=order_field_names)
            writer.writeheader()
            writer.writerows(orders_list)
            success = True
    except FileNotFoundError:
        success = False
    file.close()
    return success

#printing order.csv in table format
def print_orders_list():
    header = orders_list[0].keys()
    rows = [x.values() for x in orders_list]
    print(tabulate.tabulate(rows, header, tablefmt='fancy_outline'))

#saving in products.csv file 
def save_products_file():
    success = False
    product_field_names = ['name', 'price']
    try:
        with open('./products.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=product_field_names)
            writer.writeheader()
            writer.writerows(products_list)
            success = True
    except FileNotFoundError:
        success = False
    file.close()
    return success

#printing product.csv in table format
def print_products_list():
    header = products_list[0].keys()
    rows = [x.values() for x in products_list]
    print(tabulate.tabulate(rows, header, tablefmt='fancy_outline'))
    
#saving in couriers.csv file 
def save_couriers_file():
    success = False
    couriers_field_names = ['name', 'phone_number']
    try:
        with open('./couriers.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=couriers_field_names)
            writer.writeheader()
            writer.writerows(couriers_list)
            success = True
    except FileNotFoundError:
        success = False
    file.close()
    return success

#printing couriers 
def print_couriers_list():
    header = couriers_list[0].keys()
    rows = [x.values() for x in couriers_list]
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

#sub menu --- Products
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

#sub menu --- Orders
def order_menu_options():
    console.print(
        '''
*************************************[bold yellow]Order Menu!![/bold yellow]************************************
[bold green]
0.Return to main menu
1.Print list of Orders
2.Add a new order to list
3.Update order status in the list
4.Update existing order list
5.Delete a Order from list
[/bold green]
************************************************************************************
        '''
    )

#sub menu --- Couriers
def courier_menu_options():
    console.print(
        '''
*************************************[bold yellow]Courier Menu!![/bold yellow]************************************
[bold green]
0.Return to main menu
1.Print list of Couriers
2.Add a new courier to list
3.Update courier in the list
4.Delete a courier from list
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
        product_menu()  # calls fn for displaying product menu
    elif option == 2:
        courier_menu()  # calls fn for displaying courier menu
    elif option == 3:
        orders_menu()  # calls fn for displaying orders menu

def get_productList():
    return products_list

def get_courierList():
    return couriers_list

def get_orderList():
    return orders_list

def get_new_product():
    new_product_name = input('Enter new product name: ')
    new_product_price = input('Enter new product price: ')
    return new_product_name, new_product_price

def get_option():
    enter_option = int(input("Enter your option 0-4 : "))
    return enter_option

def product_menu():
    product_menu_options()
    option = get_option()
    console.print(
        '\n*******************************************************************************')
    print("You have selected :", option)
    if option == 0:
        main()
    elif option == 1:
        print_products_list()
    elif option == 2:
        new_product_name, new_product_price = get_new_product()
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
    
def courier_menu():
    courier_menu_options()
    option = int(input("Enter your option 0-4 :"))
    console.print(
        '\n*******************************************************************************')
    print("You have selected :", option)
    if option == 0:
        main()
    elif option == 1:
        print_couriers_list()
    elif option == 2:
        new_courier_name = input('Enter new courier person name : ')
        new_courier_phonenumber = input('Enter new phone number : ')
        new_dict = {'name': new_courier_name, 'phone_number': new_courier_phonenumber}
        couriers_list.append(new_dict)
        save_couriers_file()
        print_couriers_list()
    elif option == 3:
        for courier in couriers_list:
            index = couriers_list.index(courier)
            console.print(
                f" The [bold green]{courier} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the courier index value for an update : "))
        for key, value in couriers_list[user_input_index].items():
            new_property = input('Enter the values for name & phone number : ')
            if new_property:
                couriers_list[user_input_index][key] = new_property
            else:
                break
        save_couriers_file()
        print_couriers_list()
    elif option == 4:
        for courier in couriers_list:
            index = couriers_list.index(courier)
            console.print(
                f" The [bold green]{courier} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_index = int(
            input("Enter the courier index value for deletion : "))
        del couriers_list[user_input_index]
        save_couriers_file()
        print_couriers_list()
    courier_menu()

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
            
        input_product_index_values = [int(x) for x in input("Enter product index values :\n").split(',')]
        product_index_values = ', '.join(str(x) for x in input_product_index_values)
        
        for courier in couriers_list:
            index = couriers_list.index(courier)
            console.print(
                f" The [bold green]{courier} [/bold green]index value is : [bold green]{index}[/bold green]")
        user_input_courier_index = int(
            input("Enter the courier index value : "))
        
        status = "Preparing"
        new_order = {
            "customer_name": customer_name,
            "customer_address": customer_address,
            "customer_phone": customer_phone_number,
            "status": status,
            "courier": user_input_courier_index,
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
        for item in orders_list:
            index = orders_list.index(item)
            print(f"the {item} is value {index}")
        user_input_index = int(input("Enter the index value:"))
        for key, value in orders_list[user_input_index].items():
            property_values = input('Enter the new property value :')
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
