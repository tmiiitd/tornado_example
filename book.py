#mdm
import json


class Book:

    def __init__(self):
        self.books = []

    def add_book(self, ebom_id, parts):
        new_book = {}
        new_book["ebom_id"] = ebom_id
        new_book["parts"] = parts
        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)

    def del_book(self, ebom_id):
        found = False
        for idx, book in enumerate(self.books):
            if book["ebom_id"] == ebom_id:
                index = idx
                found = True
                del self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.books

    def json_list(self):
        return json.dumps(self.books)


    def get_book_by_id(self, ebom_id):
        found = False
        answer = None
        for idx, book in enumerate(self.books):
            if book["ebom_id"] == ebom_id:
                index = idx
                found = True
                answer = self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return answer

    def get_number_of_eboms(self):
        return len(self.books)
