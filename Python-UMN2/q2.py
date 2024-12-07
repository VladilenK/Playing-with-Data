from q2_Classes import BookStatus, Book, LibraryMember, Library


library = Library("Xeniya's Library")
print("Created a library:", library)
print("so far number of books in the library:", len(library.books))

book = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
print("Created a book:", book)
print("Book details:" )
book.display_info()
book.update_status(BookStatus.BORROWED)
print("Book with status BORROWED:" )
book.display_info()

book2 = Book('The Catcher in the Rye', 'J.D. Salinger', '9780316769488')
book3 = Book('Lessons Learned', 'Cem Kaner', '9780471081128' )
book4 = Book('Agile Testing', 'Lisa Crispin', '9780321534460')
book5 = Book('Explore It!', 'Elisabeth Hendrickson', '9781937785024')
book6 = Book('Continuous Testing','Eran Kinsbruner', '9781484230176')
book7 = Book('The Art of Software Testing', 'Glenford J. Myers', '9781118032979')

library.add_book(book)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)
library.add_book(book7)

print(f"Added some books to the library")
print("Number of books in the library:", len(library.books))
print("List of books in the library:")
library.list_all_books()

library.remove_book(book3.isbn)
print(f"Removed a book {book3} from the library")
print("Number of books in the library:", len(library.books))
print("List of books in the library:")
library.list_all_books()


member1 = LibraryMember("Kris", 1)
print("Created a member:", member1)
member2 = LibraryMember("Kourtney", 2)
print("Created a member:", member2)
member3 = LibraryMember("Kim", 3)
print("Created a member:", member3)

if member1.borrow_book(book):
    print(f"{member1} borrowed {book}")
else:
    print(f"{member1} could not borrow {book}")

if member1.borrow_book(book2):
    print(f"{member1} borrowed {book2}")
else:
    print(f"{member1} could not borrow {book2}")

if member2.borrow_book(book2):
    print(f"{member2} borrowed {book2}")
else:
    print(f"{member2} could not borrow {book2}")

member1_books = member1.get_borrowed_books()
print(f"Total number of books {member1} borrowed: {len(member1_books)} ")
print(f"{member1} has the following books in posession:")
for book in member1_books:
    print("-", book)


member1.return_book(book2)
print(f"{member1} returned {book2}")
member1_books = member1.get_borrowed_books()
print(f"Total number of books {member1} borrowed: {len(member1_books)} ")
print(f"{member1} has the following books in posession:")
for book in member1_books:
    print("-", book)

if member2.borrow_book(book2):
    print(f"{member2} borrowed {book2}")
else:
    print(f"{member2} could not borrow {book2}")

member2_books = member2.get_borrowed_books()
print(f"Total number of books {member2} borrowed: {len(member2_books)} ")
print(f"{member2} has the following books in posession:")
member2.list_borrowed_books()


print("Number of books in the library:", len(library.books))
print("List of books in the library:")
library.list_all_books()

book_found_1 = library.search_book_by_title("The Art of Software Testing")
if book_found_1:
    print("Book found with title 'The Art of Software Testing':")
    book_found_1.display_info()
    if member3.borrow_book(book_found_1):
        print(f"{member3} borrowed {book_found_1}")
    else:
        print(f"{member3} could not borrow {book_found_1}")
else:
    print("Book with title 'The Art of Software Testing' not found in the library")


book_found_2 = library.search_book_by_title("Software Reliability: Principles and Practices")
if book_found_2:
    print("Book found with title 'Software Reliability: Principles and Practices':")
    book_found_2.display_info()
    if member3.borrow_book(book_found_2):
        print(f"{member3} borrowed {book_found_2}")
    else:
        print(f"{member3} could not borrow {book_found_2}")
else:
    print("Book with title 'Software Reliability: Principles and Practices' not found in the library")


print(f"{member3} has the following books in posession:")
member3.list_borrowed_books()


print("Number of books in the library:", len(library.books))
print("List of books in the library:")
library.list_all_books()

