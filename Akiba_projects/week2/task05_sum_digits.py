print("=================================")
print("      SUM OF DIGITS")
print("=================================")

number = int(input("Enter the number to add its digit: "))

total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("The sum of digits is", total)