print("================================")
print("Even or odd")
print("================================")

number = int(input("Enter the number: "))

if number % 2 == 0:
    if number < 0:
        print("The number is negative even number.")
    elif number > 0:
        print("The number is positive even number.")
    else:
        print("The number is zero.")
    
else:
    if number < 0:
        print("The number is negative odd number.")
    else:
        print("The number is positive odd number.")
   
        
        
    
        
