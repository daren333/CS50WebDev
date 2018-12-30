import re
import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE books2 (id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year INTEGER NOT NULL);") 
    f = open('books.csv')
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        if isbn != "isbn":
            db.execute("INSERT INTO books2 (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": isbn, "title": title, "author": author, "year": int(year)})
        #print(f"Added book {title} by {author}.")
        db.commit()     

if __name__== "__main__":
    main()
