#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Candidate nr: 357
Question2.py

Library Management System

Defines Book and Library classes, runs an automated test script,
and then drops into a simple menu‐driven interface.
"""


class Book:
    """Represents a book with title, author and page count."""
    
    def __init__(self, title, author, num_pages):
        """Initialize a new Book instance."""
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        """Return a readable string representation of the book."""
        return f"'{self.title}' by {self.author} ({self.num_pages} pages)"


class Library:
    """Manages a collection of Book instances and borrowed books."""
    
    def __init__(self):
        self.books = [] # All available books
        self._checked_out = [] # Books currently checked out

    def add_book(self, book):
        """Add a new Book to the library."""
        self.books.append(book)

    def remove_book(self, title):
        """Remove the first book that matches the given title."""
        for i, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                del self.books[i]
                return True
        return False

    def check_out(self, title):
        """Borrow a book by title. Moves it from shelf to checked_out list."""
        for i, book in enumerate(self.books):
            if book.title.lower() == title.lower():
                b = self.books.pop(i)
                self._checked_out.append(b) 
                return b
        return None

    def check_in(self, title):
        """Return a borrowed book by title. Restore it to the available list."""
        for i, book in enumerate(self._checked_out):
            if book.title.lower() == title.lower():
                b = self._checked_out.pop(i)
                self.books.append(b)
                return True
        return False
    
    def list_books(self):
        """Print all available books in the library (sorted alphabetical by title)."""
        if not self.books:
            print("No books in library.")
        else:
            print("\nCurrent books in library:")
            sorted_books = sorted(self.books, key=lambda b: b.title.lower())
            for idx, book in enumerate(sorted_books, start=1):
                print(f" {idx}. {book}")
            print()
    
    
def run_tests():
    """Basic functional check of Library and Book methods."""
    print("Running automated tests...")
    print()
    lib = Library()

    # 1) Preload the library with some sample books
    a = Book("Python for Everyone", "C.H & R.N", 752)
    b = Book("Think Python",  "Allen Downey", 244)
    c = Book("Python Crash Course", "Eric Matthes", 147)
    lib.add_book(a)
    lib.add_book(b)
    lib.add_book(c)

    # 2) Test check_out
    checked = lib.check_out("Think Python")
    if checked is b:
        print("check_out: PASS")
    else:
        print("check_out: FAIL")

    # 3) Test check_in
    result = lib.check_in("Think Python")
    if result:
        print("check_in: PASS")
    else:
        print("check_in: FAIL")

    # 4) Test remove_book
    removed = lib.remove_book("Python Crash Course")
    if removed:
        print("remove_book: PASS")
    else:
        print("remove_book: FAIL")

    # 5) Final library state
    print("\nLibrary after tests:")
    lib.list_books()
    print("Automated tests complete.")
    print("-" * 25)
    print()
    
    return lib

def print_menu():
    """Display the library menu options."""
    print("""
Library Menu:
    1. List all books
    2. Add a book
    3. Remove a book
    4. Check out a book
    5. Check in a book
    6. Exit
""")


def interactive_menu(lib):
    """Menu‐driven interface for manual testing of Library."""
    print("-" * 35)
    print("Welcome to Library Management System!")
    print("-" * 35)
    print()
    
    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        if choice == '1':
            lib.list_books()

        elif choice == '2':
            title = input("Enter title: ").strip().title()
            if not title:
                print("Title cannot be empty.")
                continue
            
            author = input("Enter author: ").strip().title()
            if not author:
                print("Author cannot be empty.")
                continue
            
            pages = input("Enter number of pages: ").strip()
            if not pages.isdigit() or int(pages) <= 0:
                print("Invalid page count. Must be a positive number.")
                continue
            
            lib.add_book(Book(title, author, int(pages)))
            print(f"Added: '{title.title()}' by {author} ({pages} pages)")

        elif choice == '3':
            title = input("Enter title to remove: ").strip()
            if lib.remove_book(title):
                print(f"Removed '{title}'.")
            else:
                print(f"Book '{title}' not found.")

        elif choice == '4':
            title = input("Enter title to check out: ").strip()
            book = lib.check_out(title)
            if book:
                print(f"Checked out: {book}")
            else:
                print(f"Book '{title}' not available.")

        elif choice == '5':
            title = input("Enter title to check in: ").strip()
            returned = lib.check_in(title)
            if returned:
                print(f"Checked in: '{title}'")
            else: 
                print(f"Book '{title}' was not checked out.")

        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please select 1-6.")
        print()
        

if __name__ == "__main__":
    tested_lib = run_tests()
    interactive_menu(tested_lib)