from typing import Union, Dict, List

BOOKS_DATABASE = [
    {
        "id_": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id_": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int) -> object:
        """

        :rtype: object
        """
        self.id_ = id_
        self.name = name
        self.pages = pages

        self.is_valid_date(self.id_, self.name, self.pages)

    def is_valid_date(self, id_, name, pages):
        pass


if __name__ == '__main__':
    # инициализируем список книг
    list_books: list[Book] = []
    book_dict: Union[dict[str, Union[str, int]], dict[str, Union[str, int]]]
    for book_dict in BOOKS_DATABASE:
        Book(id_=book_dict['id_'], name=book_dict['name'], pages=book_dict['pages'])
        book: Union[dict[str, Union[str, int]], dict[str, Union[str, int]]]
        for book in BOOKS_DATABASE:
    print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
Book(id_=1, name='test_name_1', pages=200)
Book(id_=2, name='test_name_2', pages=400)
[Book(id_=1, name='test_name_1', pages=200), Book(id_=2, name='test_name_2', pages=400)]