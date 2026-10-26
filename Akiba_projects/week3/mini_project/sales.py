
def record_sale(products, sales, product_id, quantity):
    if product_id not in products:
        print("Product not found.")
        return None

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        return None

    product = products[product_id]

    if quantity > product["stock"]:
        print("Insufficient stock.")
        print("Available stock:", product["stock"])
        return None

    unit_price = product["price"]
    total = unit_price * quantity

    # Reduce stock only after validation succeeds.
    product["stock"] -= quantity

    sale = {
        "product_id": product_id,
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": unit_price,
        "total": total
    }

    sales.append(sale)

    print("Sale recorded successfully.")
    generate_receipt(sale)

    return sale


def generate_receipt(sale):
    print("\n========== SALES RECEIPT ==========")
    print("Product:", sale["product_name"])
    print("Quantity:", sale["quantity"])
    print("Unit price:", format(sale["unit_price"], ".2f"), "Birr")
    print("Total cost:", format(sale["total"], ".2f"), "Birr")
    print("===================================")
