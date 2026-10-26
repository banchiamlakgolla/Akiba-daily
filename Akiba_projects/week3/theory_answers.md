# Theory Questions

## Question 1: Function Design

### Why can a 100-line function be difficult to maintain?

If a developer writes one large function to manage products, process sales, and generate reports, the code can become confusing. It may be difficult to understand what each part does, and finding errors can take a lot of time. Also, if we want to change one operation, we might accidentally affect another part of the program.

I think it is better to divide a large function into smaller functions, where each function has one main responsibility.

### 1. Single-purpose functions

A single-purpose function focuses on doing one task. For example, one function can add a product, another can process a sale, and another can generate a report. This makes the code easier to read and understand.

### 2. Parameters and return values

Parameters allow us to give information to a function, and return values allow us to get a result back from it. They make functions more flexible because we can use the same function with different inputs.

For example, a `calculate_total()` function can accept different prices and quantities and return the calculated total.

### 3. Code reuse

Functions help us avoid writing the same code repeatedly. Once we create a function, we can call it whenever we need that operation. This saves time and makes the program easier to update.

### 4. Testing and debugging

Small functions are easier to test because each one performs a specific task. If the sales calculation is wrong, for example, we can check the `sell_product()` function without having to examine the entire program.

### 5. How I would divide the program

I would divide the program into these functions:

- `add_product()` — adds a new product.
- `search_product()` — finds a product.
- `sell_product()` — sells a product and updates its stock.
- `calculate_total()` — calculates the total value or sales amount.
- `generate_report()` — displays the report.
- `main()` — controls the program and calls the other functions.

### Example of a poorly organized function

```python
def manage_store():
    products = {"Pen": 10, "Book": 20}
    products["Bag"] = 15
    products["Pen"] -= 2

    total = sum(products.values())
    print("Products:", products)
    print("Total:", total)

manage_store()
```

This function performs several tasks at once. It adds a product, updates stock, calculates a total, and prints the results. If I want to reuse only the product-selling part, I cannot easily do that without changing the function.

### Improved version

```python
def add_product(products, name, stock):
    products[name] = stock


def sell_product(products, name, quantity):
    if name in products and products[name] >= quantity:
        products[name] -= quantity
        return True

    return False


def generate_report(products):
    print("Products:", products)
    print("Total stock:", sum(products.values()))


products = {"Pen": 10, "Book": 20}

add_product(products, "Bag", 15)
sell_product(products, "Pen", 2)
generate_report(products)
```

In this version, each function has a clear purpose. I can understand what each