print("===========================")
print("       EMPLOYEE PAYSLIP")
print("===========================")
print()

Employee_name = input("Enter the employee name: ")
basic_salary = float(input("Enter the basic salary:"))
trans_allowance = float(input("Enter Transport allowance:"))
food_allowance = float(input("Enter food allowance:"))
gross_salary = basic_salary + trans_allowance + food_allowance

print()

print("Employee:", Employee_name)
print("Basic Salary:", basic_salary)
print("Transport allowance:", trans_allowance)
print("Food allowance:", food_allowance)
print("------------------------")
print("Gross Salary:", gross_salary)
print("====================================")
