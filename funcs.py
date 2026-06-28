def itemSearch():
    searchTarget = input('Enter search item: ')

    if searchTarget.isnumeric() == False: 
        #Will return false if combo of num+chars https://www.w3schools.com/python/ref_string_isnumeric.asp
        with open("items.txt", "r") as file:
            for item in file:
                name, price = item.strip().split(", ")
                if name.lower().strip() == searchTarget.lower().strip(): #Removes whitespace otherwise won't find
                    print(f"\n{name.strip()} for ${price} has been found.\n")
                    break
            else:
                print("Item was not found!\n")
    else:
        print("Error: Search item must not be numbers.\n")

def itemAdd():
    try:
        addTarget = input('Please enter the name of the item you wish to add: ')
        addTargetPrice = float(input('Please enter the price of the item: '))

        if addTarget.isnumeric() == False:
            with open("items.txt", "a") as file: #points to end of file
                file.write(f"\n{addTarget.lower().strip()}, {addTargetPrice}") #New line otherwise appended to end of previous item
                print(f"Added {addTarget.strip()} for ${addTargetPrice} to file\n")
        else:
            print("Items cannot be numeric!\n")
    except ValueError:
        print("Error: Prices must be a number.\n")

def itemRemove():
    removeTarget = input('Enter the item to be removed: ')
    items = []
    itemNames = []

    with open("items.txt", "r+") as file:
        for item in file:
            name, price = item.strip().split(", ")
            itemNames.append(name.lower().strip())
        if removeTarget.lower().strip() not in itemNames:
            print("Item was not found!\n")
            return

    with open("items.txt", "r+") as file:
        for item in file:
            name, price = item.strip().split(",")
            if name.lower().strip() != removeTarget.lower().strip():
                items.append(item.strip())
        file.seek(0) #Pointer to start of items
        file.writelines('\n'.join(items)) #Rewrite over old items
        file.truncate() #Remove everything at/after the current pointer position (last new list)
        print(f"Removed {removeTarget.strip()} successfully.\n")