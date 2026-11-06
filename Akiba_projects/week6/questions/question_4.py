from abc import ABC, abstractmethod
print(" ========================================================")
print(" Question 4: Polymorphism and Abstraction")
print(" ========================================================")

print("\n   ============================")
print("      Part A: Polymorphism ")
print("   ============================")


class Dog:
    
    def make_sound(self):
        print("Bark")
        

class Cat:
    
    def make_sound(self):
        print("Meo")
        
        
class Cow:
    
    def make_sound(self):
        print("Buaa")
        
        
dog = Dog()
cat = Cat()
cow = Cow()


dog.make_sound()
cat.make_sound()
cow.make_sound()

print("\n ===========================")
print("    Part B: Abstraction ")
print("  =============================")


class Shape(ABC):
    
    @abstractmethod 
    def calculate_area(self):
        pass
    
    
class Rectangle(Shape):
    
    def __init__(self, width, length):
        self.width = width
        self.length = length
        
    def calculate_area(self):
        return self.width * self.length
   
    
class Circle(Shape):
    pi = 3.14
    
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return Circle.pi * self.radius * self.radius 


rectangle = Rectangle()
circle = Circle()

rectangle.calculate_area(4, 5)
circle.calculate_area(3)

print("Rectangle Area= ", rectangle.calculate_area())
print("Circle Area= "), circle.calculate_area()       

'''
  # Theory questions:
# What is polymorphism?
-> Polymorphism- is one of the principles of OOP that enables 
         having the same method name with different function definition 
         depending on the object it uses it.  
# What is abstraction?
-> Abstraction- hiding unnecessary implementation details and exposing only 
           the essential functionality 
# What is an abstract class?
-> An abstract class- a class that cannot instantiated directly and is 
               designed to serve as a blueprint for child class. 
               Can contain abstract or regular method 
# What happens if a child class does not implement an inherited abstract 
method?
-> Python prevents from creating an object of that child class.
   raises TypeError (since a class has unimplemented abstract method)
# What is the difference between abstraction and encapsulation?
-> Abstraction - hiding the unnecessary implementation, focus on just 
          essential functionality
-> Encapsulation- Bundles data and methods together
                controls access of object attributes
'''