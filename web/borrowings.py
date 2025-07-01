from fastapi import APIRouter
from pydantic import BaseModel
from service.borrowings import book_borrow, get_borrows_month, get_borrower_book, return_books
router = APIRouter(prefix="/borrows")

class BorrowBook(BaseModel):
    borrower: str
    title: str

class ReturnBook(BaseModel):
    borrower: str
    title: str

@router.post("")
def borrow_book(request: BorrowBook):
    return book_borrow(request.borrower, request.title)

# /borrows/month/2025-07 이런식으로 경로 설정
@router.get("/month/{borrow_month}")
def get_monthly_borrows(borrow_month: str):
    return get_borrows_month(borrow_month)

@router.get("/{borrower}/books")
def get_borrower_books(borrower: str):
    return get_borrower_book(borrower)

@router.post("/return")
def return_book(request: ReturnBook):
    return return_books(request.borrower, request.title)