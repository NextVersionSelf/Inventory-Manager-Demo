from funcs import *
print("Welcome to Inventory Manager!\n")

while True:
    print(
    "Please enter your selection: \n"
    "1. Search for item\n"
    "2. Add Item\n"
    "3. Remove Item\n"
    "4. Update Item Price\n"
    "5. Exit\n"
    )

    user_choice = int(input())
    match user_choice:
        case 1:
            itemSearch()
        case 2:
            itemAdd()
        case 3:
            itemRemove()
        case 5:
            exit(0)