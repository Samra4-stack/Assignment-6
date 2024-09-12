''' Write a program* that has an array of numbers; 
if the number is negative, it should remove the
negative number from the array.'''

arr = input("Enter numbers with some spaces: ")
remove_negative = list(map(int, arr.split()))
only_positive = []

for i in remove_negative:
    if i > 0:
        only_positive.append(i)
print(only_positive)