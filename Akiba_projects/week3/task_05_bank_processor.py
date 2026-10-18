balance = 1000
transactions = []
daily_withdrawal_limit = 5000
total_withdrawn_today = 0


def record_transactions(transaction_type, amount, balance):
    transaction = {
        "type": transaction_type, 
        "amount": amount,
        "balance_after": balance
    }
    
    transactions.append(transaction)
    
    
def deposit(amount):
    global balance
    
    # amount = int(input("Enter amount you want: "))
    
    if amount <= 0:
        print("Deposit amount must be greater that zero.")
        return
    
    balance += amount
    
    record_transactions("deposit", amount, balance)
    
    print("Deposit successful")


def withdraw(amount):
    
    global balance
    global total_withdrawn_today 
           
    if amount <= 0:
        print("Withdrawal amount must be greater than zero.")
        return
    
    if amount > balance:
        print("Insufficient balance.")
        return
    
    if total_withdrawn_today + amount > daily_withdrawal_limit:
        print("Daily withdrawal limit exceeded!")
        return
    
    balance -= amount
    
    total_withdrawn_today += amount
    
    record_transactions("withdrawal", amount, balance)
    
    print("Withdrawal successful!")
    
    
def check_balance():
    return balance


def transaction_summary():
    total_deposited = 0
    total_withdrawn = 0

    for transaction in transactions:
        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        elif transaction["type"] == "withdrawal":
            total_withdrawn += transaction["amount"]

    print("\n--- TRANSACTION SUMMARY ---")
    print("Total deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Final balance:", check_balance())

    print("\n--- TRANSACTION HISTORY ---")

    if len(transactions) == 0:
        print("No transactions recorded.")
    else:
        for transaction in transactions:
            print("Type:", transaction["type"])
            print("Amount:", transaction["amount"])
            print("Balance after:", transaction["balance_after"])


def main():
    while True:
        print("\n  =BANKING MENU =")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Transaction summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            print("Current balance:", check_balance())

        elif choice == "4":
            transaction_summary()

        elif choice == "5":
            print("Thank you for using our banking system!")
            transaction_summary()
            break

        else:
            print("Invalid choice. Please select 1-5.")


main()