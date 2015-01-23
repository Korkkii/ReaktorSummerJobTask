import sqlite3

"""
Create the sqlite3 database and add tables
"""


def init_db(name):
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE ShortUrl (url TEXT UNIQUE , base62 TEXT)''')
    cursor.execute('''INSERT INTO ShortUrl VALUES (?, ?)''', ("foo.bar/baz/bar", "fo.o/bar"))
    connection.commit()
    connection.close()