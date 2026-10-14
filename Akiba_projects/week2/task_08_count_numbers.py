
print("==============================")
print("      COUNT NUMBERS ")
print("==============================")

number = int(input("Enter a positive number: "))

even_count = 0
odd_count = 0
total = 0

for n in range(1, number + 1):
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total += n

print("Even =", even_count)
print("Odd =", odd_count)
print("Total =", total)
