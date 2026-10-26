
def add_product(products, product_id, name, price, stock):
    if product_id in products:
        print("A product with this ID already exists.")
        return False

    if not name.strip():
        print("Product name cannot be empty.")
        return False

    if price <= 0:
        print("Price must be greater than zero.")
        return False

    if stock < 0:
        print("Stock cannot be negative.")
        return False

    products[product_id] = {
        "name": name,
        "price": price,
        "stock": stock
    }

    print("Product added successfully.")
    return True


def search_product(products, product_id):
    return products.get(product_id)


def update_product(products, product_id, name, price, stock):
    if product_id not in products:
        print("Product not found.")
        return False

    if not name.strip():
        print("Product name cannot be empty.")
        return False

    if price <= 0 or stock < 0:
        print("Invalid price or stock.")
        return False

    products[product_id]["name"] = name
    products[product_id]["price"] = price
    products[product_id]["stock"] = stock

    print("Product updated successfully.")
    return True


def display_products(products):
    if not products:
        print("No products available.")
        return

    print("\n--- PRODUCT LIST ---")

    for product_id, product in products.items():
        print("ID:", product_id)
        print("Name:", product["name"])
        print("Price:", format(product["price"], ".2f"), "Birr")
        print("Stock:", product["stock"])
        print("-" * 25)
