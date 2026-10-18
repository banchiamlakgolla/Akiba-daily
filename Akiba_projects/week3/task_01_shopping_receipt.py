
items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]


def validate_item(items):
    for item in items:
        if item['price'] < 0:
            raise ValueError('A price cannot be negative. ')
        if item['quantity'] < 0:
            raise ValueError('A quantity cannot be negative. ')


def calculate_subtotal(items):
    subtotal = 0
    
    for item in items:
        items_total = item['price'] * item['quantity']
        subtotal += items_total
    
    return subtotal    


def calculate_discount(subtotal):
    if subtotal >= 3000:
        discount = subtotal * 10/100
    elif subtotal >= 1000:
        discount = subtotal * 5/100
    else:
        discount = 0
    
    return discount


def calculate_tax(amount, tax_rate):
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError('Tax must be between 0 and 100. ')
    
    tax = amount * tax_rate/100
    
    return tax


def generate_receipt(items, tax_rate):
    validate_item(items)
    
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_amount = subtotal - discount
    tax = calculate_tax(discounted_amount, tax_rate)
    
    final_amount = discounted_amount + tax
    
    receipt = {
        "Subtotal =": subtotal,
        "Discount =": discount,
        "Tax =": tax,
        "Final amount =": final_amount
    }
    
    return receipt


items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

tax_rate = 15

receipt = generate_receipt(items, tax_rate)

print("--- SHOPPING RECEIPT ---")
for key, value in receipt.items():
    print(key + ":", round(value, 2), "Birr")