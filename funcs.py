def itemSearch():
    searchTarget = input('Enter search item: ')

    try: 
        validateInputString(searchTarget)
        with open("items.txt", "r") as file:
            for item in file:
                if searchTarget.lower().strip() == item.lower().strip(): #Removes whitespace otherwise won't find
                    print(f"\n{item.strip()} has been found.")
                    break
            else:
                print("Item was not found!\n")
    except ValueError as e:
        print(e)

def itemAdd():
    addTarget = input('Please enter the name of the item you wish to add: ')

    with open("items.txt", "a") as file: #points to end of file
        file.write(f"\n{addTarget.lower().strip()}") #New line otherwise appended to end of previous item
        print(f"Added {addTarget.strip()} to file\n")

def itemRemove():
    removeTarget = input('Enter the item to be removed: ')
    items = []

    with open("items.txt", "r+") as file:
        for item in file:
            if removeTarget.lower().strip() != item.lower().strip():
                items.append(item)
        file.seek(0) #Pointer to start of items
        file.writelines(items) #Rewrite over old items
        file.truncate() #Remove everything at/after the current pointer position (last new list)
        print(f"Removed {removeTarget.strip()} successfully.\n")



def validateInputString(value): #Prevent numbers from being entered, assuming combination is not number+characters
    try:                        #.isnumeric() will return false for the same reasons above
        float(value)            #https://www.w3schools.com/python/ref_string_isnumeric.asp
    except ValueError:
        return
    
    raise ValueError("Numeric inputs are not allowed.\n")