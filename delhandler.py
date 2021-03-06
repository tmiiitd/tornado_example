#mdm
import tornado.web
import book
import json


class DelHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
        ebom_id = self.get_argument('ebom_id')
        result = self.books.del_book(ebom_id)
        if result:
            self.write("Deleted ebom_id: {0} succsessfully".format(ebom_id))
            self.set_status(200)
        else:
            self.write("ebom_id '{0}' not found".format(ebom_id))
            self.set_status(404)
    def post(self):
        data = json.loads(self.request.body)
        title = data["title"]
        result = self.books.del_book(ebom_id)
        if result:
            self.write("Deleted ebom_id: {0} successfully".format(ebom_id))
            self.set_status(200)
        else:
            self.write("ebom_id '{0}' not found".format(ebom_id))
            self.set_status(404)
