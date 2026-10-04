print("================================")
print("          BMI REPORT")
print("================================")
print()

name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height * height)

print()
print("Name:", name)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print()

print("BMI:", bmi)

print("================================")