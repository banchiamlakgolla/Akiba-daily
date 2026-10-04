print("==================================")
print("        RECEIPT")
print("==================================")

cust_name = input("Enter customer name:")
Product_name = input("Enter product name:")
price = float(input("Enter the price:"))
quantity = int(input("Enter the quantity:"))

total = price*quantity

print()
print("Customer:", cust_name)
print()
print("Product  Price  Qty")
print("-----------------------")
print(Product_name, " ", price, "ETB ", quantity)

print()

print("Total:", total, "ETB")
print("Thank you for shopping!")
print("=================================")
