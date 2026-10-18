
number = int(input("Enter a number: "))


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True    
  
    
def get_divisors(number):
    if number == 0:
        raise ValueError('Zero has no finite set of positive divisors. ')
    divisors = []
    
    if number < 0:
        number = abs(number)
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
            
    return divisors
    
    
def sum_of_digits(number):
    number = abs(number)
    sum = 0
    
    while number > 0:
        digit = number % 10
        sum += digit
        number = number // 10
        
    return sum 
   
        
def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return sign * reversed_number

    
def analyze_number(number):
    if number == 0:
        divisors = None
    else:
        divisors = get_divisors(number)

    if number % 2 == 0:
        parity = "Even"
    else:
        parity = "Odd"

    analysis = {
        "Number": number,
        "Parity": parity,
        "Prime": is_prime(number),
        "Sum of digits": sum_of_digits(number),
        "Reversed number": reverse_number(number),
        "Divisors": divisors
    }

    return analysis


result = analyze_number(number)

for key, value in result.items():
    print(key + ":", value)
            