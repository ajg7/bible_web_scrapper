from books_of_the_bible import new_testament
class User_Input:
    def __init__(self, book, verse, testament):
        self.book = book;
        self.verse = verse;
        self.testament = testament;
    @staticmethod
    def verse_formatter(verse):
        parsed = verse.split(':')
        formated = parsed[0] + "-" + parsed[1]
        return formated
    @staticmethod
    def which_testament(book):
        for ele in new_testament:
            if ele.lower() == book:
                return "new"
            else:
                return "old"