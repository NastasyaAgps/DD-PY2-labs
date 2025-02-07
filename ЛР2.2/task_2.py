BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Initialize a Book instance.

        :param id_: The ID of the book.
        :param name: The name of the book.
        :param pages: The number of pages in the book.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Return a string representation of the Book instance.
        """
        return f"Book(id={self.id}, name='{self.name}', pages={self.pages})"

    def __repr__(self):
        """
        Return a string representation of the Book instance for debugging.
        """
        return self.__str__()


class Library:
    def __init__(self, books: list[Book] = None):
        """
        Initialize a Library instance.

        :param books: A list of Book instances (optional).
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Get the next available book ID.

        :return: The next book ID. If the library is empty, returns 1.
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Get the index of a book by its ID.

        :param book_id: The ID of the book to find.
        :return: The index of the book. If the book is not found, raises a ValueError.
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Book with the specified ID not found.")


if __name__ == '__main__':
    empty_library = Library()  # Initialize an empty library
    print(empty_library.get_next_book_id())  # Check the next ID for an empty library (should return 1)

    # Create a list of Book instances from BOOKS_DATABASE
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Initialize a library with books
    print(library_with_books.get_next_book_id())  # Check the next ID for a non-empty library (should return 3)

    print(library_with_books.get_index_by_book_id(1))  # Check the index of the book with ID = 1 (should return 0)