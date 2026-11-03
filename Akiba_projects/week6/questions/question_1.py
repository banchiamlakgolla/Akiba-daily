print(" ========================================================")
print(" Question 1: Classes, Objects, Constructors, and Methods")
print(" ========================================================")


class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department
        
    def display_info(self):
        print("\n Student information: ")
        print("Name: ", self.name)
        print("Student Id: ", self.student_id)
        print("Department: ", self.department)
        
    def introduce(self):
        print("Hello, my name is ", self.name, "Id no= ", self.student_id)
        
        
student1 = Student("Selam", 1, "Software engineering")
student2 = Student("Amen", 2, "CS")
student3 = Student("Makida", 3, "Electrical Engineering")

student1.display_info()
student2.display_info()
student3.display_info()

student1.introduce()
student2.introduce()
student3.introduce()     


'''
 # Theory questions
# 1. What is a class in Python?
-> Class is a blueprint used to created objects, 
        defines the attributes and methods objects can have(class Student:)
# 2. What is an object?
-> Object is an instance of a class created from class, contains its own 
          attributes(data) and behavior(actions it performs) (student1 = 
           Student("Selam", 1, "Software engineering"))
# 3. What is the purpose of the __init__() method?
-> __init__()- a constructor used to initialize object's attribute with the 
              given values. 
# 4. What is the difference between an attribute and a method?
-> Attribute- describes an object' data or properties. 
-> Method- describes the action of an object(what the object can do). 

'''          