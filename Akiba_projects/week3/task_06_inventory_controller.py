inventory = {}


def add_product(name, price, stock):
    if not name.strip():
        print("Product name cannot be empty.")
        return
    
    if name in inventory:
        print("Product already exists.")
        return
    
    if price < 0:
        print("Price cannot be negative!")
        return
    
    if stock < 0:
        print("Stock cannot be negative!")
        return
    
    inventory[name] = {
        "price": price,
        "stock": stock
    }
    
    print("Product added successfully!")
    

def search_product(name):
    if name not in inventory:
        print("Product not found.")
        return

    print("Product:", name)
    print("Price:", inventory[name]["price"])
    print("Stock:", inventory[name]["stock"])
    
        
def update_price(name, new_price):
    if name not in inventory:
        print("Product not found.")
        return
    
    if new_price < 0:
        print("Price cannot be negative.")
        return
    
    inventory[name]["price"] = new_price 
    
    print("Price updated successfully!") 
    

def increase_stock(name, quantity):
    if name not in inventory:
        print("Product not found.")
        return
    
    if quantity <= 0:
        print("Quantity must be positive!")
        return
    
    inventory[name]["stock"] += quantity
        
    print("Stock increased successfully!")
    
    
def sell_product(name, quantity):
    if name not in inventory:
        print("product not found!")
        return
    
    if quantity <= 0:
        print("Quantity must be positive!")
        return
    
    if inventory[name]["stock"] < quantity:
        print("Not enough stock available!")
        return
        
    inventory[name]["stock"] -= quantity
    print("Product sold successfully!")
        
    
def total_inventory_value():
    total = 0

    for name, details in inventory.items():
        price = details["price"]
        stock = details["stock"]

        total = total + (price * stock)

    print("Total inventory value:", total)
    
    
def low_stock_report(threshold=5):
    if threshold <= 0:
        print("Threshold must be positive!")
        return
    
    found = False

    for name, details in inventory.items():
        if details["stock"] < threshold:
            print(name, "- Stock:", details["stock"])
            found = True

    if not found:
        print("No products have low stock.")
    
    
def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return

    for name, details in inventory.items():
        print("Product:", name)
        print("Price:", details["price"])
        print("Stock:", details["stock"])
        
        
def main():
    while True:
        print("\n   --Inventory Stock Controller --")
        print("1. Add product")
        print("2. Search product")
        print("3. Update price")
        print("4. Increase stock")
        print("5. Sell product")
        print("6. Total inventory value")
        print("7. Low-stock report")
        print("8. Display inventory")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Product name: ")

            try:
                price = float(input("Product price: "))
                stock = int(input("Stock quantity: "))
                add_product(name, price, stock)
            except ValueError:
                print("Please enter valid numbers.")

        elif choice == "2":
            name = input("Product name: ")
            search_product(name)

        elif choice == "3":
            name = input("Product name: ")

            try:
                new_price = float(input("New price: "))
                update_price(name, new_price)
            except ValueError:
                print("Please enter a valid price.")

        elif choice == "4":
            name = input("Product name: ")

            try:
                quantity = int(input("Quantity to add: "))
                increase_stock(name, quantity)
            except ValueError:
                print("Please enter a whole number.")

        elif choice == "5":
            name = input("Product name: ")

            try:
                quantity = int(input("Quantity to sell: "))
                sell_product(name, quantity)
            except ValueError:
                print("Please enter a whole number.")

        elif choice == "6":
            total_inventory_value()

        elif choice == "7":
            value = input("Enter threshold (press Enter for 5): ")

            try:
                if value.strip() == "":
                    low_stock_report()
                else:
                    threshold = int(value)

                    if threshold < 0:
                        print("Threshold cannot be negative.")
                    else:
                        low_stock_report(threshold)
            except ValueError:
                print("Please enter a whole number.")

        elif choice == "8":
            display_inventory()

        elif choice == "9":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()