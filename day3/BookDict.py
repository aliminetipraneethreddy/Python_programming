library={}
print("1.Add a book to the library (Book ID, Title).")
print("2.Remove a book using Book ID.")
print("3.Search for a book by Book ID and display the title.")
print("4.Update the title of a book (e.g., correction in title).")
print("5.Display all books in the library.")
print("6.Count the total number of books in the library.")
print("_.Check if a book title exists in the library (reverse lookup).")
while True:
    c=int(input("Enter"))
    match (c):
        case 1:
            id=int(input("Enter id"))
            name=int(input("name"))
            library[id]=name
        case 2:
            if id in library:
                del library[id]
        case 3:
            s=int(input("search"))
            if s in library:
                print("Present")
            else:
                print("Absent")
        case 4:
            print(library)
        case 5:
            print(len(library))
        case 6:
            val=input("enter search")
            if val in library.values():
                print("Present")
            else:
                print("Absent")

        case _:
            break




