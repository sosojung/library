from . import con, cur

def create_book(title: str, author: str):
    sql = "INSERT INTO books (title, author) VALUES (?, ?)"
    cur.execute(sql, (title, author))
    con.commit()
    return True

def available_books():
    sql = "SELECT title, author FROM books WHERE available = 1"
    cur.execute(sql)
    books = cur.fetchall()
    return [{"title": book[0], "author": book[1]} for book in books]

def delete_book(book_id: int):
    sql = "SELECT available FROM books WHERE book_id = ?"
    cur.execute(sql, (book_id,))
    result = cur.fetchone()

    if result and result[0] == 1:
        sql = "DELETE FROM books WHERE book_id = ?"
        cur.execute(sql, (book_id,))
        con.commit()
        return True
    return False