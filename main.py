import sys

#creating product list
product_list = ["Coke Zero", "Pepsi", "Fanta"]

#function for creating main menu
def main_menu():
    print("Main Menu")
    print("0. Exit  1. Product Menu")
    option = int(input("Select option(0/1) :"))
    if option == 0:
        sys.exit() #exits from main menu
    elif option ==1:
        product_menu()#calls fn for displaying product menu
        
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
        user_input_index = int(input("Enter the product index value for updating an existing product:"))
        new_product = input('Enter new product name:')
        product_list[user_input_index] = new_product
        print(product_list)
    elif option == 4:
        for product in product_list:
            index = product_list.index(product)
            print(f" The {product} index value is : {index}")
        user_input_index = int(input("Enter the product index value for deletion:"))
        del product_list[user_input_index]
        print(product_list)
    product_menu()
    
main_menu()