from data import borrowings as data
from data.books import create_book, available_books, delete_book

def insert_book(title: str, author: str):
    return create_book(title, author)

def available_books_list():
    return available_books()

def remove_book(book_id: int):
    return delete_book(book_id)