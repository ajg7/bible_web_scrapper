from tkinter import *
from scrapper import scrapper
from input import User_Input

root = Tk()

book_label = Label(root, text="Book of the Bible")
book_entry = Entry(root, width=25)
book_label.pack()
book_entry.pack()

verse_label = Label(root, text="Verse")
verse_entry = Entry(root, width=25)
verse_label.pack()
verse_entry.pack()

def click_search():
    book = book_entry.get().lower()
    verse = verse_entry.get()
    testament = User_Input.which_testament(book)
    formated_verse = User_Input.verse_formatter(verse)
    lookup = User_Input(book, formated_verse, testament)
    result = scrapper(lookup)
    
    separator = " "
    english = separator.join(result[0])
    if testament == "new":
        original_text = separator.join(result[1])
    else:
        original_text = separator.join(result[2])
    english_label = Label(root, text=english)
    original_text_label = Label(root, text=original_text)
    english_label.pack()
    original_text_label.pack()
    
enter_button = Button(root, text="Search", command=click_search)
enter_button.pack()

root.mainloop()