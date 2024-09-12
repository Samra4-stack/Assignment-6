'''  Write a program* to remove all the 
      odd numbers from an array.  '''

arr = input("Enter Numbers with spaces: ")
remove_odd_numbers = list(map(int , arr.split()))
even = []

for i in remove_odd_numbers:
   if i % 2 == 0:
    even.append(i)
print(even)