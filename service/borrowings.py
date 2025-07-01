from cache import borrower as cache
from data.borrowings import borrow_book, get_monthly_borrows, return_book
from cache.borrower import add_borrower_book, get_borrower_books

def book_borrow(borrower:str, title:str):
    result = borrow_book(borrower, title)
    if result:
        add_borrower_book(borrower, title)
    return result

def get_borrows_month(borrow_month: str):
    return get_monthly_borrows(borrow_month)

def get_borrower_book(borrower: str):
    books = get_borrower_books(borrower)
    return {"borrower": borrower, "books": books}

def return_books(borrower: str, title: str):
    # 반납 처리
    result = return_book(borrower, title)
    if result:
        # Redis에서 대출자의 책 목록에서 제거
        cache.remove_borrower_book(borrower, title)
    return result