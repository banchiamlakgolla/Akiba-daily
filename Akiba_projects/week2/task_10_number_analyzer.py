print("==============================")
print("      NUMBER ANALYZER")
print("==============================")

print("Enter 10 numbers.")

number = int(input("Enter number 1: "))

largest = number
smallest = number
total = number
even_count = 0
odd_count = 0

if number % 2 == 0:
    even_count += 1
else:
    odd_count += 1

for i in range(2, 11):
    number = int(input("Enter number " + str(i) + ": "))

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

average = total / 10

print("---RESULTS ---")
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
