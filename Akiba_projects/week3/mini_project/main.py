
from products import (
    add_product,
    search_product,
    update_product,
    display_products
)

from sales import record_sale

from reports import display_reports


def get_positive_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number > 0:
                return number

            print("Please enter a number greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_non_negative_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if number >= 0:
                return number

            print("Please enter zero or a positive number.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_price(prompt):
    while True:
        try:
            price = float(input(prompt))

            if price > 0:
                return price

            print("Price must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a valid price.")


def main():
    products = {}
    sales = []

    while True:
        print("\n===== AKIBA BUSINESS TOOLKIT =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Record Sale")
        print("6. View Reports")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            product_id = input("Enter product ID: ").strip()
            name = input("Enter product name: ").strip()
            price = get_price("Enter product price (Birr): ")
            stock = get_non_negative_number("Enter initial stock: ")

            if product_id:
                add_product(products, product_id, name, price, stock)
            else:
                print("Product ID cannot be empty.")

        elif choice == "2":
            display_products(products)

        elif choice == "3":
            product_id = input("Enter product ID to search: ").strip()
            product = search_product(products, product_id)

            if product is None:
                print("Product not found.")
            else:
                print("\nProduct found:")
                print("Name:", product["name"])
                print("Price:", format(product["price"], ".2f"), "Birr")
                print("Stock:", product["stock"])

        elif choice == "4":
            product_id = input("Enter product ID to update: ").strip()

            if product_id not in products:
                print("Product not found.")
            else:
                name = input("Enter new product name: ").strip()
                price = get_price("Enter new price (Birr): ")
                stock = get_non_negative_number("Enter new stock: ")

                update_product(
                    products, product_id, name, price, stock
                )

        elif choice == "5":
            product_id = input("Enter product ID to sell: ").strip()
            quantity = get_positive_number("Enter quantity: ")

            record_sale(products, sales, product_id, quantity)

        elif choice == "6":
            display_reports(products, sales)

        elif choice == "7":
            print("Thank you for using Akiba Business Toolkit!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 7.")


if __name__ == "__main__":
    main()
