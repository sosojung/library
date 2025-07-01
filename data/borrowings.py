from . import con, cur

def borrow_book(borrower:str, title:str):
    sql = "SELECT book_id FROM books WHERE title = ? AND available = 1"
    cur.execute(sql, (title,))
    book = cur.fetchone()

    if not book:
        return False

    book_id = book[0]

    sql = "INSERT INTO borrowings (book_id, borrower) VALUES (?, ?)"
    cur.execute(sql, (book_id, borrower))

    sql = "UPDATE books SET available = 0 WHERE book_id = ?"
    cur.execute(sql, (book_id,))

    con.commit()
    return True

def get_monthly_borrows(borrow_month: str):
    sql = """
    SELECT b.borrower, bk.title, bk.author
    FROM borrowings b
    JOIN books bk ON b.book_id = bk.book_id
    WHERE strftime('%Y-%m', b.borrowed_at) = ?
    """
    cur.execute(sql, (borrow_month,))
    borrows = cur.fetchall()
    return [{"borrower": borrow[0], "title": borrow[1], "author": borrow[2]} for borrow in borrows]


def return_book(borrower: str, title: str):
    sql = """
    SELECT b.borrow_id, b.book_id
    FROM borrowings b
    JOIN books bk ON b.book_id = bk.book_id
    WHERE b.borrower = ? AND bk.title = ? AND b.returned_at IS NULL
    """
    cur.execute(sql, (borrower, title))
    borrow = cur.fetchone()

    if not borrow:
        return False

    borrow_id, book_id = borrow

    sql = "UPDATE borrowings SET returned_at = current_timestamp WHERE borrow_id = ?"
    cur.execute(sql, (borrow_id,))

    sql = "UPDATE books SET available = 1 WHERE book_id = ?"
    cur.execute(sql, (book_id,))

    con.commit()
    return True