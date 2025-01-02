users_info_list = []  # List to store user information from the file
products_info_list = []  # List to store product information from the file
###########################################################

def dict_of_products(): 
    # Function to create a list containing dictionaries for each product
    products = []  # List to store all product dictionaries
    with open("products.txt", "r") as file:
        next(file)  # Skip the header line
        for line in file:
            line_list = line.split(",")  # Split the line into values
            line_dict = { "ID": line_list[0], "name": line_list[1], "price": line_list[2], "stock": line_list[3]}  # Create a dictionary for each product
            products.append(line_dict)  # Append the dictionary to the products list
    return products  # Return the list of product dictionaries

def update_info(list, file): 
    # Function to update a list based on the contents of a given file
    list.clear()  # Clear the list before updating
    with open(file, "r") as file:
        for line in file: 
           list.append(line.strip())  # Add each line from the file to the list

def user_register(username, age, email, file): 
    # Function to register a new user by appending their data to a file
    check_user = False  # Boolean to check if the username is already taken
    update_info(users_info_list, file)  # Sync the users_info_list with the file
    with open(file, "a") as file:
        for i in range(len(users_info_list)):
            if username.replace(" ", "_") in users_info_list[i]:  # Check if the username is already taken
                check_user = True
        if check_user == True:
            print(f"This username is taken: {username}")  # Notify the user if the username is taken
        else:
            print(f"Registering {username}")  # Register the new user
            file.write(f"{username.replace(' ', '_')}, {str(age)}, {email}\n")  # Write user data to the file

def product_register(file, list):
    # Function to register multiple products and add them to the file
    with open(file, "a") as file:
        for i in range(len(list)):  # Iterate over the product list
            for element in list[i]:
                if element != list[i][3]:  # Add product details, separated by commas
                    file.write(f"{element}, ")
                else:
                    file.write(f"{element}\n")  # Add a newline after the last element
            print(list[i][1])  # Print the product name
        print("Products successfully added.")  # Confirm products were added

def user_login(username, file):
    # Function to log in a user by checking if their username exists in the file
    check_login = False  # Boolean to track login success
    update_info(users_info_list, file)  # Sync the users_info_list with the file
    for i in range(len(users_info_list)):
        if username.replace(" ", "_") in users_info_list[i]:  # Check if the username exists
            print(f"Login successful. Welcome {username}")  # Confirm login
            check_login = True
    if check_login != True:
        print("Login unsuccessful!")  # Notify if login fails

def show_elements_name(list, file, name_number): 
    # Function to show elements (like usernames) based on their position in a line
    update_info(list, file)  # Sync the list with the file
    for user_info in users_info_list:
        username = user_info.split()[name_number]  # Extract the desired part of the line
        print(username)  # Print the extracted element

def shopping_cart(file, selected_numbers):
    # Function to create a shopping cart with selected product IDs and calculate the total price
    cart_dict = {}  # Dictionary to store selected products
    total_price = 0  # Initialize the total price
    num = 0  # Counter for products
    with open(file, "r") as file:
        for line in file:
            line_list = line.strip().split(",")  # Split the product line
            if line_list[0] in selected_numbers:  # Check if the product ID is in the selected list
                cart_dict[line_list[0]] = {line_list[1]}  # Add the product to the cart
                total_price += int(line_list[2])  # Add the price to the total
            num += 1
    return cart_dict, total_price  # Return the cart and the total price

def shopping_cart_deleter(dict, del_list):
    # Function to remove specific products from the shopping cart
    for i in range(len(del_list)):
        if del_list[i] in dict:  # Check if the product ID is in the cart
            del dict[del_list[i]]  # Remove the product from the cart

def check_discount(cart, total_price):
    # Function to apply discounts based on the cart contents and total price
    if 1000 < total_price:
        total_price = (total_price * 90) / 100  # Apply a 10% discount
        print("Total price exceeds 1000, applying 10% discount.")
        print("Total price is now", total_price)
    if 'Laptop' in cart.values():
        total_price = total_price - 150  # Apply a discount for Laptop
        print("There is a special 150 discount on Laptop, applying now!")
        print("Total price is now", total_price)
    elif 'Monitor' in cart.values():
        total_price = total_price - 750  # Apply a discount for Monitor
        print("There is a special 750 discount on Monitor, applying now!")
        print("Total price is now", total_price)
    return total_price

def summary(variable):
    # Function to write a transaction summary to a file
    with open("transaction_summary.txt", "a") as file:
        file.write(variable)  # Append the summary to the file

def product_updates_recursive(products, factors, index=0):
    '''
    Recursive function to update product prices and stock levels.
    '''
    if index >= len(products):  # Base case: Stop when all products are processed
        return

    pro = products[index]
    ID, name, price, stock = pro['ID'], pro['name'], pro['price'], pro['stock']
    price = price.strip()
    stock = stock.strip()

    new_price = (float(price) * float(factors[1]))  # Calculate new price
    new_stock = float(stock) * float(factors[2])  # Calculate new stock

    if ID == factors[0]:  # Check if the product matches the ID to be updated
        pro['price'] = str(new_price)  # Update price
        pro['stock'] = str(int(new_stock)) + '\n'  # Update stock
        print(f"Updated: {ID}, {name}, {new_price}, {new_stock}")

    product_updates_recursive(products, factors, index + 1)  # Recursive call for next product


def product_write_file(products):
    # Function to write the updated product list back to the file
    with open("products.txt", "w") as file:
        file.write("ID, Name, Price, Stock\n")  # Write the header line first
    with open("products.txt", "a") as file:
        for product in products:
            file.write(f"{product['ID']},{product['name']},{product['price']},{product['stock']}")  # Write product details

def filter(products, list_of_filters, index=0):
    '''
    Recursive function to filter products based on the specified criteria.

    products: A list containing dictionaries for all products.
    list_of_filters: A list of filters applied to product attributes (ID, name, price range, stock range).
    index: The current index in the products list for recursion.
    '''
    if index >= len(products):  # Base case: Stop when all products are processed
        return []

    pro = products[index]  # Get the current product
    matches = True  # Flag to track if the product matches all filters

    # Filter by ID
    if list_of_filters[0] != "0" and list_of_filters[0] != pro["ID"].strip():
        matches = False  

    # Filter by Name
    if list_of_filters[1] != "0" and list_of_filters[1].lower() not in pro["name"].lower().strip():
        matches = False 

    # Filter by Price Range
    if list_of_filters[2] != (0, 0):
        min_price, max_price = map(float, list_of_filters[2])  
        if not (min_price <= float(pro["price"]) <= max_price):
            matches = False 

    # Filter by Stock Range
    if list_of_filters[3] != (0, 0):
        min_stock, max_stock = map(int, list_of_filters[3])  
        if not (min_stock <= int(pro["stock"]) <= max_stock):
            matches = False  

    if matches:
        return [pro] + filter(products, list_of_filters, index + 1)  # Add product to results if it matches
    else:
        return filter(products, list_of_filters, index + 1)  # Skip product if it doesn't match

def filter_ask():
    # Function to ask the user for filtering criteria
    filter_list = ["0", "0", (0, 0), (0, 0)]  # Default filter values
    print("1) ID", "2) Name", "3) Range of Price", "4) Range of Stock")
    print("Note that you can only filter 1 attribute at a time")
    filter_type = input("Which attribute do you want to filter (1, 2, 3, or 4)? ")

    if filter_type == "1":
        # Filter by ID
        f = input("Please type your filter: ")
        filter_list[0] = f
    elif filter_type == "2":
        # Filter by Name
        f = input("Please type your filter: ")
        filter_list[1] = f
    elif filter_type == "3":
        # Filter by Price Range
        try:
            s = float(input("Enter the minimum price: "))
            e = float(input("Enter the maximum price: "))
            filter_list[2] = (s, e)
        except ValueError:
            print("Invalid input for price range. Please enter numeric values.")
    elif filter_type == "4":
        # Filter by Stock Range
        try:
            s = int(input("Enter the minimum stock: "))
            e = int(input("Enter the maximum stock: "))
            filter_list[3] = (s, e)
        except ValueError:
            print("Invalid input for stock range. Please enter numeric values.")
    else:
        # Handle invalid input
        print("Invalid option selected.")
        
    return filter_list  # Return the filter criteria specified by the user


##########################################################

#TASK1: User registiration and login
print("Existing Users:")
update_info(users_info_list, "users.txt")
for user in users_info_list:
    print(user.split(",")[0])  # Display usernames only
#Register a new user
#username = input("What is your username?")
#age = input("What is your age? ")
#email = input("What is your email? ")s
#user_register(username, age, email, "users.txt")
username = 'yiğit erensoy'
user_register(username,'17','yigiterensoy@std.iyte.edu.tr','users.txt')
# Log in as the new user
user_login(username, "users.txt")

print("\n") # for readability

#Task2: Product Catalog Managment
print("Original Products:")
products = dict_of_products()
for product in products:
    print(f"{product['ID']}, {product['name']}, {product['price']}, {product['stock']}")

print("\n") # for readability

# Add new products
new_products = [
    ["21", "Smart Watch", "2000", "15"],
    ["22", "Gaming Mouse", "1500", "20"],
    ["23", "Mechanical Keyboard", "3500", "10"],
    ["24", "Wireless Earbuds", "2500", "30"],
    ["25", "Monitor", "5000", "8"]
]
product_register("products.txt", new_products)

print('\n') # for readability

# Task 3: Shopping Cart
print("Shopping cart after adding products:")
selected_products = ["1", "2", "3", "5", "7", "9", "12", "14", "16", "18", "20", "21", "22", "23", "25"]
cart, total_price = shopping_cart("products.txt", selected_products)
for item, details in cart.items():
    print(f"{item}: {details}")
print("Total price:", total_price,"\n")

# Remove specific products
products_to_remove = ["1", "7", "3", "9", "16", "23", "21"]
shopping_cart_deleter(cart, products_to_remove)
print("Cart after removing products:")
for item, details in cart.items():
    print(f"{item}: {details}")

# Task 4: Discounts and Promotions
final_price = check_discount(cart, total_price)
print("Final Total Price after Discounts:", final_price,"\n")


# Task 5: Transaction Summary
transaction_details = f"User: {username}\nProducts:\n"
for item, details in cart.items():
    transaction_details += f"{item}: {details}\n"
transaction_details += f"Final Total: {final_price}\n"
summary(transaction_details)
print("Transaction summary saved to 'transaction_summary.txt'\n")


# Task 6: Dynamic Product Updates
with open('products.txt','r') as file:
    print(file.read())
products = dict_of_products()
print("Now updating the products requested on the homework.")
product_updates_recursive(products,(1,1.1,1.2))#Updates phone as requested in the homework
product_updates_recursive(products,(4,1.1,1.2))#Updates tablet as requested in the homework
product_updates_recursive(products,(14,1.1,1.2))#Updates laptop stand as requested in the homework
product_updates_recursive(products,(21,1.1,1.2))#Updates smart watch as requested in the homework
product_updates_recursive(products,(24,1.1,1.2))#Updates wireless earbuds as requested in the homework
product_write_file(products)
print("The products requested in the homework succesfuly upgraded.\n")
#product_ID   = input('what is the id of the product you want to update? ')
#price_factor =  input("what is the price factor of the product? Ex.'1.10' for %10 increase ")
#stock_factor = input("what is the stock factor of the product? Ex.'1.10' for %10 increase ")
#product_updates_recursive(products, (product_ID,price_factor, stock_factor))
#product_write_file(products)


# Task 7: Product Search and Filtering
products = dict_of_products()
filters = filter_ask()
filtered_products = filter(products, filters)
print("Filtered Products:")
for product in filtered_products:
    print(f"{product['ID']}, {product['name']}, {product['price']}, {product['stock']}")

