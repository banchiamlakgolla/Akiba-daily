print("================================")
print("Prime number checker")
print("================================")

number = int(input("Enter a number: "))

if number <= 1:
    print("The number is not prime.")

else:
    is_prime = True

    # We only need to check up to the square root of the number.
    # If a number has a divisor larger than its square root, 
    # there is also a smaller divisor. 
    for divisor in range(2, int(number ** 0.5) + 1):

        if number % divisor == 0:
            is_prime = False
            break

    if is_prime:
        print("The number is prime.")
    else:
        print("The number is not prime.")
