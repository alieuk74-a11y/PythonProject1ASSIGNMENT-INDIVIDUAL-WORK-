# tests.py
from Operation import *

# Reset data
books.clear()
members.clear()

# Test adding books and members
assert add_book("B1", "1984", "George Orwell", "Fiction", 5) == "Book added successfully."
assert add_book("B2", "Dune", "Frank Herbert", "Sci-Fi", 3) == "Book added successfully."
assert add_member("M1", "Alice") == "Member added successfully."

# Test duplicate book/member
assert add_book("B1", "Duplicate", "Author", "Fiction", 2) == "Book with this ISBN already exists."
assert add_member("M1", "Duplicate") == "Member ID already exists."

# Test search
results = search_books("Dune")
assert len(results) == 1 and results[0]["author"] == "Frank Herbert"

# Test borrowing
assert borrow_book("M1", "B1") == "Book borrowed successfully."
assert borrow_book("M1", "B2") == "Book borrowed successfully."

# Test borrow limit
assert borrow_book("M1", "B2") == "Book borrowed successfully."  # 3rd borrow
assert borrow_book("M1", "B1") == "Borrow limit reached."

# Test returning
assert return_book("M1", "B1") == "Book returned successfully."
assert return_book("M1", "B1") == "Book not borrowed by member."

# Test deleting rules
assert delete_book("B2") == "Cannot delete. Some copies are borrowed."
assert delete_member("M1") == "Cannot delete. Member has borrowed books."

print("✅ All tests passed successfully!")