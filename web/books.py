from fastapi import APIRouter
from pydantic import BaseModel
from service.books import insert_book, available_books_list, remove_book

from service import borrowings as service

router = APIRouter(prefix="/books")

class CreateBook(BaseModel):
    title: str
    author: str

@router.post("")
def create_book(book: CreateBook):
    return insert_book(book.title, book.author)

@router.get("")
def available_books():
    return available_books_list()

@router.delete("/{book_id}")
def delete_book(book_id: int):
    return remove_book(book_id)