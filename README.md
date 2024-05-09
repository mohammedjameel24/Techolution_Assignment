# Techolution_Assignment

## Redesigned Library Management System Documentation

### 1. **Object-Oriented Design (models.py)**
We've introduced three classes to represent essential entities in our system:

- **`Book`**: Represents a book with attributes like title, author, and ISBN.
- **`User`**: Represents a library user with a name and user ID.
- **`Checkout`**: Represents a book checkout, associating a user with an ISBN.

### 2. **File-Based Storage (storage.py)**
We've refactored the storage mechanism using JSON files:

- `save_to_json(filename, data)`: Saves data (e.g., books, users) to a JSON file.
- `load_from_json(filename)`: Loads data from a JSON file or returns an empty list if the file doesn't exist.

### 3. **User Input via CLI (main.py)**
The main script (`main.py`) provides a user-friendly CLI interface:

- Users can add books, list books, add users, and check out books.
- The `main_menu()` function displays available options.

### 4. **Error Handling and Input Validation**
We've implemented basic error handling and input validation:

- Invalid choices are handled gracefully.
- Users are prompted for input (e.g., title, author, ISBN, user name, user ID).

### 5. **Modularity and Scalability**
Our design allows for easy extension and modification:

- New item types (e.g., DVDs, magazines) can be added by creating additional classes.
- Features like due dates, late fees, etc., can be incorporated without major changes.

### Refactored Code Overview

- **`book.py`**: Manages books.
    - `BookManagement` class handles book-related operations.
    - Methods: `add_book(title, author, isbn)`, `list_books()`.
- **`user.py`**: Manages users.
    - `UserManagement` class handles user-related operations.
    - Methods: `add_user(name, user_id)`, `list_users()`.
- **`checkout.py`**: Manages book checkouts.
    - `CheckoutManagement` class handles checkout-related operations.
    - Methods: `checkout_book(user_id, isbn)`, `list_checkouts()`.
- **`main.py`**: Main script for user interaction.
    - Displays menu options and invokes relevant methods.
