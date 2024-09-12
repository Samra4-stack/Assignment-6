'''  Using while loop to print first 10 even numbers '''

number = int(input("Enter a number: "))
i = 1
while i <= 20:
    if number % 2 == 0:
        print(f" {number}", end=" ")
    i += 1
    number += 1

    