
# 1. Check minimum password length
def check_length(password, min_length=8):
    if len(password) >= min_length:
        return True
    else:
        return False


def check_uppercase(password):
    for character in password:
        if character.isupper():
            return True

    return False


def check_lowercase(password):
    for character in password:
        if character.islower():
            return True

    return False


def check_digit(password):
    for character in password:
        if character.isdigit():
            return True

    return False


def check_special_character(password):
    special_characters = "!@#$%^&*()-_+=?"

    for character in password:
        if character in special_characters:
            return True

    return False


def analyze_password(password, min_length=8):
    report = {
        "Minimum length": check_length(password, min_length),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special_character(password)
    }

    return report


def display_report(password, min_length=8):
    report = analyze_password(password, min_length)

    print("\n--- Password Analysis Report ---")

    for requirement, passed in report.items():
        if passed:
            print(requirement + ": PASS")
        else:
            print(requirement + ": FAIL")

    if all(report.values()):
        print("Password meets all requirements!")
    else:
        print("Password does not meet all requirements.")

        print("Missing requirements:")
        for requirement, passed in report.items():
            if not passed:
                print("-", requirement)


def main():
    passwords = [
        "password",
        "Password123",
        "PASSWORD123!",
        "password123!",
        "MyPass123!",
        "Ab1!"
    ]

    for password in passwords:
        print("Testing password:", password)
        display_report(password)


main()
