# operations.py
# Mini Library Management System (Python)
# Author: Amadu Coker

# Data Structures
genres = ("Fiction", "Non-Fiction", "Sci-Fi", "Biography", "History")

books = {}  # {ISBN: {"title": str, "author": str, "genre": str, "total_copies": int, "available_copies": int}}
members = []  # [{"member_id": str, "name": str, "borrowed_books": list}]


# ------------------ CORE FUNCTIONS ------------------

def add_book(isbn, title, author, genre, total_copies):
    """Add a book if ISBN is unique and genre is valid."""
    if isbn in books:
        return "Book with this ISBN already exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies,
        "available_copies": total_copies
    }
    return "Book added successfully."


def add_member(member_id, name):
    """Add a new member if ID is unique."""
    if any(m["member_id"] == member_id for m in members):
        return "Member ID already exists."
    members.append({"member_id": member_id, "name": name, "borrowed_books": []})
    return "Member added successfully."


def search_books(keyword):
    """Search books by title or author."""
    keyword = keyword.lower()
    result = [
        {"ISBN": isbn, **details}
        for isbn, details in books.items()
        if keyword in details["title"].lower() or keyword in details["author"].lower()
    ]
    return result


def update_book(isbn, **kwargs):
    """Update book details."""
    if isbn not in books:
        return "Book not found."
    for key, value in kwargs.items():
        if key in books[isbn]:
            books[isbn][key] = value
    return "Book updated successfully."


def update_member(member_id, **kwargs):
    """Update member details."""
    for m in members:
        if m["member_id"] == member_id:
            for key, value in kwargs.items():
                if key in m:
                    m[key] = value
            return "Member updated successfully."
    return "Member not found."


def delete_book(isbn):
    """Delete a book only if no borrowed copies exist."""
    if isbn not in books:
        return "Book not found."
    borrowed = books[isbn]["total_copies"] - books[isbn]["available_copies"]
    if borrowed > 0:
        return "Cannot delete. Some copies are borrowed."
    del books[isbn]
    return "Book deleted successfully."


def delete_member(member_id):
    """Delete a member only if no borrowed books."""
    for m in members:
        if m["member_id"] == member_id:
            if m["borrowed_books"]:
                return "Cannot delete. Member has borrowed books."
            members.remove(m)
            return "Member deleted successfully."
    return "Member not found."


def borrow_book(member_id, isbn):
    """Borrow a book if available (max 3 books per member)."""
    # Check member
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    # Check book
    if isbn not in books:
        return "Book not found."
    if books[isbn]["available_copies"] <= 0:
        return "No copies available."
    if len(member["borrowed_books"]) >= 3:
        return "Borrow limit reached."
    # Borrow
    member["borrowed_books"].append(isbn)
    books[isbn]["available_copies"] -= 1
    return "Book borrowed successfully."


def return_book(member_id, isbn):
    """Return a borrowed book."""
    member = next((m for m in members if m["member_id"] == member_id), None)
    if not member:
        return "Member not found."
    if isbn not in member["borrowed_books"]:
        return "Book not borrowed by member."
    member["borrowed_books"].remove(isbn)
    books[isbn]["available_copies"] += 1
    return "Book returned successfully."