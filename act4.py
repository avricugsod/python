items = []

while True:
    print("\nMENU")
    print("1. Add")
    print("2. Edit")
    print("3. Delete")
    print("4. Show")
    print("5. Exit")

    choice = input("Choose (1-5): ")

    # ADD
    if choice == "1":
        new_item = input("Enter item to add: ")
        items.append(new_item)
        print("Item added!")

    # EDIT
    elif choice == "2":
        if len(items) == 0:
            print("List is empty!")
        else:
            for i in range(len(items)):
                print(i, "-", items[i])
            index = int(input("Enter index to edit: "))
            if 0 <= index < len(items):
                new_value = input("Enter new value: ")
                items[index] = new_value
                print("Item updated!")
            else:
                print("Invalid index!")

    # DELETE
    elif choice == "3":
        if len(items) == 0:
            print("List is empty!")
        else:
            for i in range(len(items)):
                print(i, "-", items[i])
            index = int(input("Enter index to delete: "))
            if 0 <= index < len(items):
                items.pop(index)
                print("Item deleted!")
            else:
                print("Invalid index!")

    # SHOW
    elif choice == "4":
        if len(items) == 0:
            print("List is empty!")
        else:
            print("Your List:")
            for item in items:
                print("-", item)

    # EXIT
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")