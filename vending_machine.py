import os
from collections import Counter

awesome_ascii = """
  _______   __        _        _   __            ___             __  ___         __   _         
 / ___/ /  / /__  ___( )___   | | / /__ ___  ___/ (_)__  ___ _  /  |/  /__ _____/ /  (_)__  ___ 
/ /__/ _ \/ / _ \/ -_)/(_-<   | |/ / -_) _ \/ _  / / _ \/ _ `/ / /|_/ / _ `/ __/ _ \/ / _ \/ -_)
\___/_//_/_/\___/\__/ /___/   |___/\__/_//_/\_,_/_/_//_/\_, / /_/  /_/\_,_/\__/_//_/_/_//_/\__/ 
                                                       /___/                                                                                                                                                  
"""

ty_msg = """
 ________             __                                                            _      __
/_  __/ /  ___ ____  / /__  __ _____  __ __    _______  __ _  ___   ___ ____ ____ _(_)__  / /
 / / / _ \/ _ `/ _ \/  '_/ / // / _ \/ // /   / __/ _ \/  ' \/ -_) / _ `/ _ `/ _ `/ / _ \/_/ 
/_/ /_//_/\_,_/_//_/_/\_\  \_, /\___/\_,_( )  \__/\___/_/_/_/\__/  \_,_/\_, /\_,_/_/_//_(_)  
                          /___/          |/                            /___/                                             
"""

sad = """
    __   _                   _     _ 
  _/_/  (_)      ____       (_)   | |
 / /   _        /___/      _      / /
/ /   ( )                 ( )   _/_/ 
|_|   |/                  |/   /_/   
"""

# A dictionary that stores item information for each category
# category no. : [name, price, stock no.]
category_dict = {
    1: [
        ["Al Ain Water", 1.00, 9],
        ["Lacnor Apple Juice", 2.00, 7],
        ["Lacnor Apple Juice", 2.00, 6],
        ["Lacnor Chocolate Milk", 2.00, 8],
        ["Lacnor Strawberry Milk", 2.00, 5],
    ],
    2: [
        ["Starbucks Vanilla Frappuccino", 6.25, 10],
        ["Nescafe Spanish Latte Iced Coffee", 4.50, 8],
        ["Coke Can", 2.50, 6],
        ["Sprite Can", 2.50, 7],
        ["Lipton Lemon Iced Tea", 2.50, 9],
    ],
    3: [
        ["Lotus Biscoff Biscuits", 8.25, 5],
        ["Ritz Original Crackers", 2.25, 6],
        ["SkyFlakes Crackers", 3.79, 7],
        ["Oreo Cookies", 1.85, 8],
        ["Britannia Marie Gold Biscuits", 1.95, 9],
    ],
    4: [
        ["Al Jufair Salad Chips", 0.50, 10],
        ["Chips Oman", 0.50, 9],
        ["Takis", 7.50, 7],
        ["Lay's Potato Chips", 1.00, 6],
        ["Doritos", 1.00, 8],
    ],
}

# Clears the terminal using os library
def clear_terminal():
    os.system('cls')

# Displays all items in cart (name & price)
def display_cart(cart):
    clear_terminal()

    # Print out very cool ASCII art
    print(awesome_ascii)
    print("Shopping Cart:\n")

    # Get a dictionary of no. of duplicates for each item
    # Our cart starts off as a list so we cast it to a tuple because
    # the Counter function requires an hashable object
    # [name, price, stock] -> (name, price, stock)
    # {(name, price, stock) : no. of occurrences, ...} 
    counts = Counter(tuple(item) for item in cart)

    # Display the name and price of each item
    for item, count in counts.items():
        print(f"x{count} {item[0]} - AED {item[1]}")
    print("\n")

# Handles the payment procedure
def payment(cart):
    # If shopping cart empty when exiting
    if not cart:
        print("\nThank you for shopping with us!\n")
        return 
    
    # Calculate total cost of each item in cart
    total_cost = sum([item[1] for item in cart])

    while True:
        # Display all items in cart
        display_cart(cart)

        # Payment Input
        payment_amnt = input(f"Total Cost: {total_cost}\nEnter Payment Amount: ")
        
        # If input is a digit, cast to int and break from loop
        if payment_amnt.isdigit():
            payment_amnt = int(payment_amnt)
            break
        
        # Keep looping while input is invalid
        print("\nInvalid Input. Input must be a number.")
    
    # Checks if payment is sufficient,
    # if not then :(
    if payment_amnt >= total_cost:
        # Calculate change
        change = payment_amnt - total_cost
        
        # Prints out very nice ASCII `thank you` message
        print(ty_msg)
        #:.2f means rounding off the calculated change
        #.format() is a method, a specific type of function for strings
        #.format(change) is the calculated change. it'll fill in the curly brackets
        print("\nPayment Successful. Your change is: {:.2f} AED\n".format(change)) 
        print("Your selection has been dispensed.")

    else:
        print(sad)
        print("\nPayment Unsuccessful. Insufficient Balance.\n")


# Handles displaying menu item information for a selected category
# i.e. name, price, and stock
def choose_item_from_category(category):
    items = category_dict[category]
    while True:
        clear_terminal()
        
        # Displays menu item information
        print("\n".join([f"{idx + 1}. {item[0]} - AED {item[1]} (Stock: {item[2]})" 
                          for idx, item in enumerate(items)])) # (index, (name, price, stock)) 
        
        # ["1. name - AED price Stock: no.", "2. name - AED price Stock: no.", "3. name - AED price Stock: no."]
        # "1. name - AED price Stock: no.\n2. name - AED price Stock: no.\n3. name - AED price Stock: no."
        
        # ID Input
        item_id = input("\nEnter the ID of the item you wish to purchase ('q' to return to menu): ")
        
        # Checks if input is a digit
        if item_id.isdigit():
            item_id = int(item_id)
            # Checks if selected ID is in given range
            if 1 <= item_id <= len(items):
                # Get selected item from list
                selected_item = items[item_id - 1]
                # Checks if item is in stock
                if selected_item[2] > 0: 
                    selected_item[2] -= 1 # Decrement stock no.
                    return selected_item
                else:
                    print("\nItem out of stock. Please choose another item.")
                    continue
        # Return to Menu
        elif item_id.lower() == 'q':
            return None
        print("\nInvalid ID. Please try again.")

# Handles the category selection
def choose_category():
    menu_text = """What type of refreshment are you looking for today?
    
    1. [Non-Carbonated Beverages/Water]
    2. [Carbonated/Caffeinated Beverages]
    3. [Biscuits]
    4. [Chips]
    
Enter the corresponding number ('q' to exit): """
    while True:
        user_input = input(menu_text)
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 4:
                return user_input
        elif user_input.lower() == 'q':
            return None
        clear_terminal()
        print("\nInvalid Category. Please try again.\n")

# Main Program
if __name__ == "__main__":
    cart = [] ## assigning an empty list to variable cart
    while True:
        # Display items in cart
        display_cart(cart)

        # Select category
        category = choose_category()
        if category is None:
            clear_terminal()
            break
        # Select item from category
        selected_item = choose_item_from_category(category)
        
        # Add item to cart once selected
        if selected_item:
            cart.append(selected_item)
            print(f"\n{selected_item[0]} has been added to your cart.\n")
        else:
            print("\nReturning to the main menu.")
    payment(cart)