''' Implement a simple shopping cart program* using an array.
Create functions to add items, remove items, and update quantities
using array methods. Print the cart's contents after each operation. '''

arr = input("Welcome to my Mart !")
arr1 = input("Add Items To Cart : ")
items = list(arr1.split())  

def shopping_cart(items):
    print(f"Your items are {items}")
    ask_input = input("Do you want to remove any item from your cart?  ")
    if ask_input.lower() == "yes":
        remove_item = input("Which item do you want to remove?  ")
        if remove_item in items:
            items.remove(remove_item)
            print(f"Removed {remove_item} from your cart.")
        else:
            print(f"{remove_item} is not in your cart.")
    print(f"Now your updated cart is {items}")
    return items
    
result = shopping_cart(items)
print(result)