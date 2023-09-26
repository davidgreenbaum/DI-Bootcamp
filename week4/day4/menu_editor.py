from functools import partial
from item import MenuItem
from manager import MenuManager

def view_item(menu_manager: MenuManager): # displays item, its price, or if its not on the menu

    item_name = input("Item name: ")
    item = menu_manager.get_by_name(item_name)
    if item is None:
        print(f"No such item in the menu: {item_name}")
    else:
        print(item.item_name, item.item_price)

def initiate_item():  #establishes an item so that it can be added

    item_name = input("Item name: ")
    item_price = int(input("Item price: "))
    new_item = MenuItem(item_name, item_price)
    return new_item

def add_item(menu_manager: MenuManager): # adds the item and price and confirms to user

    item = initiate_item()
    menu_manager.add_item(item)
    print(f"{item.item_name}, {item.item_price} WAS ADDED TO THE DATABASE")

def delete_item(menu_manager: MenuManager):

    item_name = input("Item name to delete: ")
    if menu_manager.delete_item(item_name):
        print(f"{item_name} WAS DELETED FROM THE DATABASE")
    else:
        print(f"No such item in the menu: {item_name}")

def update_item(menu_manager: MenuManager): # changes an existing item... either name or price....

    item_name = input("Item name to update: ")
    new_item = initiate_item()
    new_item_name = input("New name (or skip): ")
    new_item_price = input("New price (or skip): ")
    menu_manager.update_item(item_name, new_item_name, new_item_price)

def pretty_print_menu(menu_list): # makes the info easier to read

    print("\nWelcome to Vice's Wondrous World of Culinary Delights")
    print("=" * 50)
    print("{:<10} {:<25} {:<15}".format("Item No.", "Dish", "Price"))
    print("-" * 50)
    
    for item in menu_list:
        item_no, dish, price = item
        print("{:<10} {:<25} ${:<15.2f}".format(item_no, dish, price))
    
    print("=" * 50)

def show_menu(menu_manager: MenuManager):

    menu_items = menu_manager.all()
    pretty_print_menu(menu_items)

def show_user_menu(menu=None): # key commands for user to be calling functions

    OPERATION_OPTIONS = {
        "V": partial(view_item, menu),
        "A": partial(add_item, menu),
        "D": partial(delete_item, menu),
        "U": partial(update_item, menu),
        "S": partial(show_menu, menu)
    }

    USER_OPTIONS = """
        View an Item (V)
        Add an Item (A)
        Delete an Item (D)
        Update an Item (U)
        Show the Menu (S)
    """

    if menu is None:
        menu = MenuManager()

    try:
        while True:
            print(USER_OPTIONS)
            user_choice = input("CHOICE: ")
            operation_choice = OPERATION_OPTIONS.get(user_choice)

            if operation_choice is None:
                show_user_menu(menu)  # Pass 'menu' as an argument
            
            operation_choice()

    except KeyboardInterrupt:
        OPERATION_OPTIONS["S"]()

def add_item_to_menu(menu_manager: MenuManager):
    """Add an item to the restaurant's menu"""
    
    item = initiate_item()
    menu_manager.add_item_to_menu(item)
    print(f"{item.item_name} was added successfully to the restaurant's menu.")

def remove_item_from_menu(menu_manager: MenuManager):
    """Remove an item from the restaurant's menu"""

    item_name = input("Item name to remove from the restaurant's menu: ")
    if menu_manager.remove_item_from_menu(item_name):
        print(f"{item_name} was removed successfully from the restaurant's menu.")
    else:
        print(f"Error: {item_name} not found in the restaurant's menu.")

def update_item_in_menu(menu_manager: MenuManager):
    """Update an item in the restaurant's menu"""

    item_name = input("Item name to update in the restaurant's menu: ")
    new_item = initiate_item()
    if menu_manager.update_item_in_menu(item_name, new_item):
        print(f"{item_name} was updated successfully in the restaurant's menu.")
    else:
        print(f"Error: {item_name} not found in the restaurant's menu.")

def show_restaurant_menu(menu_manager: MenuManager):
    """Show the restaurant's menu"""
    
    restaurant_menu = menu_manager.get_restaurant_menu()
    pretty_print_menu(restaurant_menu)

if __name__ == '__main__':
    show_user_menu()
