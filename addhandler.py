import tornado.web
import book
import json


class AddHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    #def get(self):
    #    ebom_id = self.get_argument('ebom_id')
    #    parts = [[1, "ae13tghf", "coal"], [2, "ae16thfk" , "gold"]]
    #    result = self.books.add_book(ebom_id, parts)
    #    self.write(result)
    def post(self):
        data = json.loads(self.request.body)
        ebom_id = data["ebom_id"]
        parts = data["parts"]
        present = self.books.get_book_by_id(ebom_id)
        if present:
            self.write("ebom_id '{0}' already found".format(ebom_id))
            self.set_status(404)
        else:
        	result = self.books.add_book(ebom_id, parts)
        	self.write(result) 
            
           