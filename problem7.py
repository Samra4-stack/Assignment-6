''' Create a function* that takes an array of numbers as a parameter.
    Use a while loop to calculate and return the sum of all 
    the numbers in the array.'''
   
def sum_numbers(arr ):
    count = 0
    sum = 0
    # arr = int(input("Enter 5 numbers"))
    while count < len(arr):
        sum += arr[count]
        count += 1
    return sum
        
input = input("Enter numbers separated by spaces : " )
arr = list(map(int , input.split()))

result = sum_numbers(arr)
print(f"Total sum = {arr}  = {result}")
