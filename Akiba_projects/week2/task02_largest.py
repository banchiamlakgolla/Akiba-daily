print("================================")
print("Largest of three")
print("================================")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


if num1 == num2 and num2 == num3:
    print("All three numbers are equal.")

elif num1 == num2:
    if num1 > num3:
        print("The first and second numbers are equal and largest.")
    else:
        print("The third number is the largest.")
elif num1 == num3:
    if num1 > num2:
        print("The first and third numbers are equal and largest.")
    else:
        print("The second number is the largest.")
elif num2 == num3:
    if num2 > num1:
        print("The second and third numbers are equal and largest.")
    else:
        print("The first number is the largest.")
elif num1 > num2 and num1 > num3:
    print("The first number (", num1, ") is the largest.")
elif num2 > num1 and num2 > num3:
    print("The second number (", num2, ") is the largest.")
else:
    print("The third number (", num3, ") is the largest.")