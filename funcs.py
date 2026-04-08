def itemSearch():
    target = input('Enter search item: ')

    with open("items.txt", "r") as file:
        for item in file:
            if target.lower() == item.lower().strip(): ##removes whitespace otherwise won't find
                print(f"\n {item.strip()} has been found.")
                break
        else:
            print("Item was not found!\n")
