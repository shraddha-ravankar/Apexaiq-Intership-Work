"""
Inventory Management System for Technical Products
Products: Laptop, Mobile, Switch, Router, Mouse
Automatically saves inventory data to a file
"""

inventory = {
    "Laptop": {"price": 60000, "quantity": 10},
    "Mobile": {"price": 20000, "quantity": 25},
    "Switch": {"price": 1500, "quantity": 30},
    "Router": {"price": 3000, "quantity": 15},
    "Mouse": {"price": 500, "quantity": 40}
}


def save_inventory():
    """
    Saves the current inventory data to a text file automatically
    """
    file = open("inventory_data.txt", "w")

    for product, details in inventory.items():
        line = f"{product},{details['price']},{details['quantity']}\n"
        file.write(line)

    file.close()


def show_inventory():
    """
    Displays all products with price and quantity
    """
    print("\n--- Current Inventory ---")
    for product, details in inventory.items():
        print(
            f"{product} | Price: {details['price']} | Quantity: {details['quantity']}"
        )


def add_product():
    """
    Adds a new product to the inventory and saves it automatically
    """
    name = input("Enter product name: ")

    if name in inventory:
        print("Product already exists.")
        return

    price = int(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    if quantity < 0:
        print("Quantity cannot be negative.")
        return

    inventory[name] = {"price": price, "quantity": quantity}
    save_inventory()
    print("Product added and saved successfully.")


def update_stock():
    """
    Updates stock quantity of an existing product and saves it automatically
    """
    name = input("Enter product name: ")

    if name not in inventory:
        print("Product not found.")
        return

    change = int(input("Enter quantity to add/remove: "))

    if inventory[name]["quantity"] + change < 0:
        print("Stock cannot become negative.")
        return

    inventory[name]["quantity"] += change
    save_inventory()
    print("Stock updated and saved successfully.")


def main_menu():
    """
    Displays menu and handles user choices
    """
    while True:
        print("\n--- Inventory Menu ---")
        print("1. Show Inventory")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_stock()
        elif choice == "4":
            print("Exiting Inventory System.")
            break
        else:
            print("Invalid choice. Try again.")


main_menu()
