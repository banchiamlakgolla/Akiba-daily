
print("==============================")
print("      Number Guessing Game")
print("==============================")

secret_number = 7
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = int(input("Guess the secret number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!")
        print("You guessed the number in", attempts, "attempts.")
        break
    else:
        print("Wrong guess!")

if guess != secret_number:
    print("Game Over!")