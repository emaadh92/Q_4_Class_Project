import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their books."""

    def __init__(self):
        """Initialize the BookCollection with an empty list."""
        self.books_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from json file to memory.
        if file does not exist or corrupt, initialize with empty list."""
        try:
            with open(self.storage_file, "r") as file:
                self.books_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = [] 

    def save_to_file(self):
        """Store to the current books list to json file."""

        with open(self.storage_file, "w") as file:
            json.dump(self.books_list, file, indent=4)

    def create_new_books(self):
        """Add a new book to the collection by user."""

        book_title = input("Enter the book title: ")
        book_author = input("Enter the book author: ")
        publication_year = input("Enter the publication year: ")
        book_genre = input("Enter the book genre: ")
        is_book_read = (
            input("Have you read this book? (yes/no): ").strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "publication_year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.books_list.append(new_book)
        self.save_to_file()
        print(f"Book '{book_title}' added to the collection!!!\n")


    def delete_book(self):
        """Delete a book from the collection by user."""

        book_title = input("Enter the title of the book to delete: ")
        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                print(f"Book '{book_title}' deleted from the collection!!!\n")
                return
        print(f"Book '{book_title}' not found in the collection.\n")


    def search_book(self):
        """Search for a book in the collection by user."""

        book_title = input("Enter the title of the book to search: ")
        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                print(f"Book found: {book}")
                return
        print(f"Book '{book_title}' not found in the collection.\n")


    def update_book_details(self):
        """Update the details of a book in the collection by user."""

        book_title = input("Enter the title of the book to update: ")
        for book in self.books_list:
            if book["title"].lower() == book_title.lower():
                new_title = input("Enter the new title (leave blank to keep current): ")
                new_author = input("Enter the new author (leave blank to keep current): ")
                new_year = input("Enter the new publication year (leave blank to keep current): ")
                new_genre = input("Enter the new genre (leave blank to keep current): ")

                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                if new_year:
                    book["publication_year"] = new_year
                if new_genre:
                    book["genre"] = new_genre

                self.save_to_file()
                print(f"Book '{book_title}' updated successfully!!!\n")
                return
        print(f"Book '{book_title}' not found in the collection.\n")
        

    def view_all_books(self):
        """Display all books in the collection."""

        if not self.books_list:
            print("No books in the collection.\n")
            return

        print("Books in the collection:")
        for book in self.books_list:
            print(f"- {book['title']} by {book['author']} ({book['publication_year']}) - Genre: {book['genre']} - Read: {'Yes' if book['read'] else 'No'}")
        print("")

    def view_reading_progress(self):
        """Display the reading progress of the user."""
        total_books = len(self.books_list)
        if total_books == 0:
            print("No books in the collection to track progress.\n")
            return

        read_books = sum(1 for book in self.books_list if book["read"])
        print(f"Reading Progress: {read_books}/{total_books} books read ({(read_books / total_books) * 100:.2f}%).\n")
    
    def Exit(self):
        """Exit the application."""

        print("Exiting the application. Goodbye!")
        exit()


    def start_application(self):
        """Start the application and provide a menu for the user to choose from."""

        while True:
            print("Welcome to the Book Collection Manager!")
            print("1. Add a new book")
            print("2. Delete a book")
            print("3. Search for a book")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")

            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                self.create_new_books()
            elif choice == "2":
                self.delete_book()
            elif choice == "3":     
                self.search_book()
            elif choice == "4":
                self.update_book_details()
            elif choice == "5":
                self.view_all_books()
            elif choice == "6":        
                self.view_reading_progress()
            elif choice == "7":
                self.Exit()
            else:
                print("Invalid choice. Please try again.\n")
           

if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.start_application()