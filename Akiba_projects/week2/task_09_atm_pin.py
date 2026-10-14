
print("==============================")
print("      ATM PIN SYSTEM ")
print("==============================")

pin_correct = 1234
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))
    attempts += 1

    if pin_correct == pin:
        print("PIN VERIFIED SUCCESSFULLY.")
        break
    else:
        print("Incorrect PIN, please try again!")
        attempts_remaining = max_attempts - attempts
        print("You have", attempts_remaining, "remaining attempts.")

if pin != pin_correct:
    print("Maximum attempts reached!")
