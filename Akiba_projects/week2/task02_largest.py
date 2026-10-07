print("================================")
print("Largest of three")
print("================================")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the first number: "))
num3 = int(input("Enter the first number: "))

if num1 > num2 and num2 > num3:
    print("The first number(", num1, ") is the largest")
elif num2 > num1 and num1 > num3:
    print("The second number(", num2, ") is the largest")
else:
    print("The third number(", num3, ") is the largest")