books = []

def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    status = "Available"

    book = [book_id, name, author, status]
    books.append(book)
    print("Book added successfully")

def display_books():
    if len(books) == 0:
        print("No books available")
    else:
        for book in books:
            print("Book ID:", book[0])
            print("Book Name:", book[1])
            print("Author:", book[2])
            print("Status:", book[3])
            print("---------------------")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    found = False

    for book in books:
        if book[0] == book_id:
            found = True
            if book[3] == "Available":
                book[3] = "Issued"
                print("Book issued successfully")
            else:
                print("Book already issued")

    if found == False:
        print("Book not found")

def return_book():
    book_id = input("Enter Book ID to return: ")
    found = False

    for book in books:
        if book[0] == book_id:
            found = True
            if book[3] == "Issued":
                book[3] = "Available"
                print("Book returned successfully")
            else:
                print("Book was not issued")

    if found == False:
        print("Book not found")

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        print("Thank you")
        break
    else:
        print("Invalid choice")