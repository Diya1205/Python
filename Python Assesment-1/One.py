# Simple Python E-Notebook Console Application

def display_menu():
    print("\nPython E-Notebook Console Application")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

def create_note():
    note = input("Enter your note: ")
    file = open("notes.txt", "a")
    file.write(note + "\n")
    file.close()
    print("Note added successfully.")

def view_notes():
    try:
        file = open("notes.txt", "r")
        notes = file.readlines()
        file.close()
        if notes:
            print("\nYour Notes:")
            for note in notes:
                print(note.strip())
        else:
            print("No notes available.")
    except FileNotFoundError:
        print("No notes available.")

def fun():
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            create_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

fun()