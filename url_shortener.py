from bottle import install, request, post, get, redirect, HTTPError
from bottle_sqlite import SQLitePlugin

dbname = "reaktor_task.db"
sqlite = SQLitePlugin(dbfile=dbname)
install(sqlite)


class Counter():
    """
    Counter class that keeps count of unique URL ids
    """
    __count = 0

    def __init__(self):
        self.__count = 12521413

    def increment(self):
        current = self.__count
        print(current)
        self.__count += 1
        return current


__count__ = Counter()


@post('/shorten')
def shorten_url(db):
    """
    Checks the database for URL matches
    Shortens and stores the URL in the database if no matches
    Returns the shortened version
    """
    long_url = str(request.body.getvalue(), encoding="UTF-8")
    print(long_url)
    found = db.execute('''SELECT base62 FROM ShortUrl WHERE url = ?''', (long_url,))
    row = found.fetchone()
    if row is not None:
        return row[0]
    else:
        count = __count__.increment()
        short_url = convert_to_base62_string(count)
        db.execute('''INSERT INTO ShortUrl VALUES (?, ?)''', (long_url, short_url))
        return short_url


@get('/<id>')
def redirect_url(id, db):
    """
    Redirects to the url matching the id with HTTP 301
    If no matching URL found, returns HTTP 404
    """

    found = db.execute('''SELECT url FROM ShortUrl WHERE base62 = ?''', (id,))
    url = found.fetchone()
    if url is not None:
        print(url[0])
        redirect(url[0], code=301)
    else:
        print("Failed")
        return HTTPError(status=404)


__elements__ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
                "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4",
                "5", "6", "7", "8", "9", "0", "A", "B", "C", "D", "E", "F", "G", "H", "I",
                "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
                "Y", "Z"]


def convert_to_base62_string(number):
    """
    Converts base 10 number into base 62 string
    """
    digits = []
    if number == 0:
        digits.insert(0, 0)
    while number > 0:
        digits.insert(0, number % 62)
        number //= 62
    chars = [__elements__[digit] for digit in digits]
    string = "".join(chars)
    return string


