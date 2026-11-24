import functions
import json

functions.load_json()

print("Welcome to Sakanade's Library! Now, let's start!")
while True:
    print("-----------MENU-----------")
    print("1. Add books")
    print("2. Search Books")
    print("3. Remove Books")
    print("4. List books")
    print("5. Edit Books")
    print("6. Mark a book as read")
    print("7. Save your Library in JSON format")
    print("8. Exit the Library")
    print("Type below your option!")
    opmenu = int(input())
    if opmenu == 1:
        functions.add_books()
    elif opmenu == 2:
        functions.search_books()
    elif opmenu == 3:
        functions.remove_books()
    elif opmenu == 4:
        functions.list_books()
    elif opmenu == 5:
        functions.edit_books()
    elif opmenu == 6:
        functions.mark_as_read()
    elif opmenu == 7:
        functions.save_json()
    elif opmenu == 8:
        print("Exiting Sakanade's Library! Return soon!")
        break
    else:
        print("Invalid option. Try again")