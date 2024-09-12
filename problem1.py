''' Create a function* that takes an array, an index, 
and a value as parameters. Inside the function, use 
the insert method to insert the value at the specified 
index in the array. Return the modified array. '''

arr = input("Enter some number with some spaces:")
arr2 = list(map(int, arr.split()))
value = int(input("Enter number that you want to insert into array: "))
index = int(input("Enter index where you want to put value: "))

def insert(arr2, index, value):
    arr2.insert(index, value)
    return arr2

result = insert(arr2, index, value)
print(f" {value} at index {index}")
print(f"Your modified array is: {result}")