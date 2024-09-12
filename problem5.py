'''Create a function* that takes a positive integer as a 
parameter and uses a while loop to calculate and return 
the factorial of that number.'''

def factorial(number):
    result = 1
    while number > 1:
        result *= number
        number -= 1
    return result
number = int(input("Enter a number to find factorial: "))
result2 = factorial(number)
print(f"The Factorial of {number}! = {result2}")
   