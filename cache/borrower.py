from . import redis_client

def test():
    return "redis connect ok"

def add_borrower_book(borrower: str, title: str):
    key = f"borrower:{borrower}:books"
    redis_client.sadd(key, title)

def get_borrower_books(borrower: str):
    key = f"borrower:{borrower}:books"
    books = redis_client.smembers(key)
    return [book.decode('utf-8') for book in books]

def remove_borrower_book(borrower: str, title: str):
    key = f"borrower:{borrower}:books"
    redis_client.srem(key, title)