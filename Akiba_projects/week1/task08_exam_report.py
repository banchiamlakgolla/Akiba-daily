print("========================================")
print("     STUDENT RESULT    ")
print("========================================")
print()

student_name = input("Enter the name i=of the student: ")
python = int(input("Enter your python score: "))
english = int(input("Enter your English score: "))
mathematics = int(input("Enter your mathematics score: "))

average = (python + english + mathematics)/3 
print("Student: ", student_name)
print()
print("Python: ", python)
print("English: ", english)
print("Mathematics: ", mathematics)
print("---------------------------")

print("Average: ", round(average, 2))
