
def validate_units(units):
    if units < 0:
        return False

    return True


def calculate_first_tier(units):
    if units <= 50:
        return units * 0.50

    return 50 * 0.50


def calculate_second_tier(units):
    if units <= 50:
        return 0

    if units <= 150:
        return (units - 50) * 0.75

    return 100 * 0.75


def calculate_third_tier(units):
    if units <= 150:
        return 0

    return (units - 150) * 1.20


def calculate_total_bill(units, service_fee=0):
    if not validate_units(units):
        return None

    if service_fee < 0:
        return None

    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)

    total = first_charge + second_charge + third_charge
    total = total + service_fee

    return total


def generate_summary(units, service_fee=0):
    if not validate_units(units):
        print("Invalid units! Units cannot be negative.")
        return

    if service_fee < 0:
        print("Invalid service fee! It cannot be negative.")
        return

    first_charge = calculate_first_tier(units)
    second_charge = calculate_second_tier(units)
    third_charge = calculate_third_tier(units)

    total = calculate_total_bill(units, service_fee)

    print("\n--- Electricity Billing Summary ---")
    print("Units consumed:", units)
    print("First tier charge:", format(first_charge, ".2f"), "Birr")
    print("Second tier charge:", format(second_charge, ".2f"), "Birr")
    print("Third tier charge:", format(third_charge, ".2f"), "Birr")
    print("Service fee:", format(service_fee, ".2f"), "Birr")
    print("Total bill:", format(total, ".2f"), "Birr")


def main():
    try:
        units = float(input("Enter electricity units consumed: "))

        service_input = input(
            "Enter service fee (press Enter for no fee): "
        )

        if service_input.strip() == "":
            service_fee = 0
        else:
            service_fee = float(service_input)

        generate_summary(units, service_fee)

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


main()
