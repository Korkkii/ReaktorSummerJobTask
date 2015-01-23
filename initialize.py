import os.path

import bottle

from database import init_db
import url_shortener


"""
Initializes the database and starts bottle that listens to localhost:8080
"""

if __name__ == "__main__":
    dbname = url_shortener.dbname
    if not os.path.isfile(dbname):
        init_db(dbname)
    bottle.run(host="localhost", port="8080")
