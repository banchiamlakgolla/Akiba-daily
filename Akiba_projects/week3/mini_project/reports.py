
def calculate_total_revenue(sales):
    total_revenue = 0

    for sale in sales:
        total_revenue += sale["total"]

    return total_revenue


def calculate_inventory_value(products):
    inventory_value = 0

    for product in products.values():
        inventory_value += product["price"] * product["stock"]

    return inventory_value


def display_low_stock(products, threshold=5):
    print("\n--- LOW-STOCK PRODUCTS ---")
    found = False

    for product_id, product in products.items():
        if product["stock"] <= threshold:
            print(
                product_id,
                "-",
                product["name"],
                "- Stock:",
                product["stock"]
            )
            found = True

    if not found:
        print("No low-stock products.")


def display_sales_summary(sales):
    if not sales:
        print("No sales have been recorded.")
        return

    print("\n--- SALES SUMMARY ---")
    print("Number of sales:", len(sales))
    print("Total quantity sold:", sum(sale["quantity"] for sale in sales))
    print(
        "Total revenue:",
        format(calculate_total_revenue(sales), ".2f"),
        "Birr"
    )


def display_reports(products, sales):
    print("\n========== BUSINESS REPORTS ==========")
    print(
        "Total revenue:",
        format(calculate_total_revenue(sales), ".2f"),
        "Birr"
    )
    print(
        "Remaining inventory value:",
        format(calculate_inventory_value(products), ".2f"),
        "Birr"
    )

    display_low_stock(products)
    display_sales_summary(sales)
