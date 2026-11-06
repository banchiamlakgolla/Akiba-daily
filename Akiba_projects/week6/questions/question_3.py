print(" ================================================")
print(" Question 3: Inheritance and Method Overriding")
print(" ================================================")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_info(self):
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)
        
        
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        
    def display_info(self):
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language
        
    def display_info(self):
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)
        print("Programming Language: ", self.programming_language) 
        

manager = Manager("Selam", 60000, "Management")
developer = Developer("Amen", 40000, "Python")

manager.display_info()
developer.display_info()

'''
 # Theory questions:
# What is inheritance?
-> Inheritance - one of the OOP principle that allows a child class to acquire 
            attributes and methods from parent class ( for code reusability). 
# What is the difference between a parent class and a child class?
-> Parent class - provides common attributes and method
-> child class - inherits parent class and can add or modify its own 
                  functionality. 
# What is method overriding?
-> Method overriding- enables a child class to define its own implementation
               of a method that already exists in its parent class 
# What is the purpose of super()?
-> super()- used to access methods from the next class in the Method
        Resolution Order(MRO), allows to reuse parent functionality without 
        rewriting the code(eg. constructor)
# What is the difference between single and multiple inheritance?
-> Single inheritance- a child class inherits from only one parent class
-> Multiple inheritance- a child class inherits from two or more parent classes

'''