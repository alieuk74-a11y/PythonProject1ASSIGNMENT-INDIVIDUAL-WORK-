"""
Demo Script for Mini Library Management System
Author: Your Name
Date: 2025-09-23
Description:
    Demonstrates the usage of the library management system functions:
    - Adding books and members
    - Searching
    - Borrowing and returning books
    - Updating and deleting records
"""

from Operation import (
    add_book,
    add_member,
    search_books,
    update_book,
    delete_book,
    borrow_book,
    return_book
)

# ----------------------------
# Sample Data
# ----------------------------

# Books (ISBN: details)
books = {}

# Members (ID: details)
members = {}

# Valid genres
genres = ("Fiction", "Non-Fiction", "Sci-Fi")

# ----------------------------
# DEMONSTRATION
# ----------------------------

print("\n=== DEMO: MINI LIBRARY MANAGEMENT SYSTEM ===\n")

# 1️⃣ Add Books
print("Adding books...")
add_book(books, "9780140449136", "The Odyssey", "Homer", "Fiction", 3, genres)
add_book(books, "9780553382563", "A Short History of Nearly Everything", "Bill Bryson", "Non-Fiction", 2, genres)
add_book(books, "9780345339683", "The Hobbit", "J.R.R. Tolkien", "Sci-Fi", 5, genres)
print("Books added successfully!\n")

# 2️⃣ Add Members
print("Adding members...")
add_member(members, "M001", "Alice Johnson")
add_member(members, "M002", "Bob Smith")
print("Members added successfully!\n")

# 3️⃣ Search for Books
print("Searching for 'Homer'...")
search_books(books, "Homer")

# 4️⃣ Borrow Books
print("\nBorrowing a book...")
borrow_book(books, members, "M001", "9780140449136")
borrow_book(books, members, "M001", "9780345339683")
print(f"Member 'M001' borrowed 2 books.\n")

# 5️⃣ Try borrowing unavailable copies
print("Borrowing until no copies left...")
borrow_book(books, members, "M002", "9780553382563")
borrow_book(books, members, "M002", "9780553382563")  # Should fail when no copies left

# 6️⃣ Return a Book
print("\nReturning a book...")
return_book(books, members, "M001", "9780140449136")

# 7️⃣ Update Book Details
print("\nUpdating book details...")
update_book(books, "9780345339683", title="The Hobbit: Revised Edition", total_copies=6)

# 8️⃣ Delete a Book
print("\nDeleting a book record...")
delete_book(books, "9780553382563")

# ----------------------------
# Final Output
# ----------------------------

print("\n=== FINAL STATE ===")
print("Books:", books)
print("Members:", members)

print("\nDemo completed successfully!")
