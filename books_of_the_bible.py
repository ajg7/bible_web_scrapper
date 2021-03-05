import requests
from bs4 import BeautifulSoup

URL = "https://www.biblestudytools.com/books-of-the-bible/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
books_of_the_bible_containers = soup.find_all("h3", class_="large-h3")

books = []

for book_container in books_of_the_bible_containers:
    books.append(book_container.text)

old_testament = books[0:39]
new_testament = books[39:66]