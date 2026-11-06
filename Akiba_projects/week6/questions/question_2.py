print(" ================================================")
print(" Question 2: Encapsulation and Access Modifiers")
print(" ================================================")


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance
        
    def deposit(self, amount):
        if amount <= 0:
            print("Amount should be positive to be deposited!")
        else:
            self.__balance += amount
            print(amount, "Birr Deposited successfully!")
            print("Your current balance is ", self.__balance)
        # return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
            
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            
    def get_balance(self):
        print("Current balance = ", self.__balance, "Birr") 
    
    
account = BankAccount("Selam", 1000)  

account.deposit(500)
account.withdraw(600)
account.withdraw(1600)
account.get_balance()        


'''
  # Theory questions:
# 1. What is encapsulation?
-> Encapsulation - is combining data and methods inside a class, controls how 
                 that data is accessed and modified. 
              access controls: public, protected and private
# 2. Why do we use private attributes?
-> private attributes- used to prevent random modification for some essential 
               data( restrict direct access to important object data and 
               controlled access through methods)
# 3. What is name mangling in Python?
-> Name mangling - is a python mechanism that automatically changes the name 
            of an attribute or method that starts with two underscore (__) 
            inside class (for private attributes) 
#4. What is the difference between public, protected, and private naming 
    conventions?
-> These are python's naming conventions to indicate the intended 
        accessibility of attributes
    Public - can be accessed from anywhere(name -no underscore)
    Protected - intended for internal use and subclass (_name -one underscore)
    private - name-mangled restrict direct access(__name -two underscores)

'''