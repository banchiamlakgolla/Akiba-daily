print(" ==========================")
print("Task 1: Student Information System")
print("==========================")


class Student:
    
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
          
    def display_info(self):
        print("\n   -Student information: ") 
        print("Name: ", self.name) 
        print("Age: ", self.age)    
        print("Department: ", self.department, "\n")
        
        
student1 = Student("Selam", 20, "Software Engineering")
student2 = Student("Amen", 22, "CS")
student3 = Student("Solomon", 21, "Electrical Engineering")               
 

student1.display_info()
student2.display_info()
student3.display_info()      


print("\n ==========================")
print("   Task 2: Rectangle Calculator")
print("  ==========================")


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return self.width * self.length
    
    def perimeter(self):
        return 2 * (self.width + self.length)
    
    
rect1 = Rectangle(2, 5)
rect2 = Rectangle(3, 6)

print("\n Area = ", rect1.area(), "and perimeter = ", rect1.perimeter()) 
print("\n Area = ", rect2.area(), "and perimeter = ", rect2.perimeter())      


print("\n ==========================")
print("  Task 3: Student Score Management")
print("  ==========================")


class Student:
    school_name = "Akiba Academy"
    
    def __init__(self, name, score, department):
        self.name = name
        self.score = score
        self.department = department
        
    def display_info(self):
        print("\n   Student information: ") 
        print("Student Name: ", self.name)
        print("score: ", self.score)
        print("school_name: ", Student.school_name)
        print("Department: ", self.department)


student1 = Student("Ban", 90, "Software")
student2 = Student("Afomya", 96, "IT")
student3 = Student("Yonatan", 95, "CS")

student1.display_info()       
student2.display_info() 
student3.display_info() 

'''
    # Questions:

1. What is the difference between a class attribute and an instance attribute?
# class attribute: defined in class body and it is shared by all the instances,
  eg. school_name = "Akiba Academy" in this task is class attribute
# instance attribute: an attribute for each object(unique for each object), it can be changed or added at runtime
  eg. name, score, and department. in this task are instance attribute
   
2. Why does updating one student's score not automatically change the scores of other students?
# Because each student is separate object instance, each object has its own attributes and stores its store independently. 
'''

print("\n ==========================")
print("    Task 4: Product Information System")
print("   ==========================")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
    
    def total_value(self):
        return self.price * self.quantity
    
    
product1 = Product("Phone", 20000, 5)
product2 = Product("Bag", 2000, 5)
product3 = Product("Charger", 400, 10)

print(product1)
print(product2)
print(product3)
print("Total value for product1 =", product1.total_value())
print("Total value for product2 =", product2.total_value())
print("Total value for product3 =", product3.total_value())

''' # Question: What is the purpose of the __str__() method?
  #  __str__() used to display a user friendly text for the users
   
'''

print("\n ==========================")
print("    Task 5: Bank Account Management")
print("  ==========================")


class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print( amount, " birr Deposited successfully!")
            
        else:
            print("Invalid deposit amount!")
        return self.balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("You do not have enough amount to withdraw!")
        else:
            self.balance -= amount
            print(amount, " birr withdrawn successfully!")
        
    def display_balance(self):
        print("Account owner:", self.owner)
        print("Current balance:", self.balance, "birr")
        
        
account1 = BankAccount("Selam", 1000)
account2 = BankAccount("Amen", 2000)

print("\n  Account1 Transactions ")

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)

account1.display_balance() 


print("\n   Account2 Transactions ")

account2.deposit(1000)
account2.withdraw(500)
account2.withdraw(10000)

account2.display_balance()
 