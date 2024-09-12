''' Implement a program* that takes a list of temperatures in Celsius 
as input from the user. Convert each temperature to Fahrenheit using 
the formula F = (C * 9/5) + 32 and store the converted temperatures in 
an array. Use a while loop to perform the conversion for each temperature. '''

arr = input("Enter temperature in celsius with some spaces: ")
arr = list(map(int, arr.split()))
i = 0
while i < len(arr):
    fahrenheit = (arr[i] * 9/5) + 32
    print(f"{arr[i]}°C = {fahrenheit}°F")
    i += 1

    