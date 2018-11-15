#mdm
#mdm
import tornado.web
import book
import json


class GetByIdHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    #def get(self):
    #    self.write(self.books.json_list())

    def get(self):
        ebom_id = self.get_argument('ebom_id')
        result = self.books.get_book_by_id(ebom_id)
        if result:
        	self.write(result)
        	#self.write(result.json_list())
        	self.set_status(200)
        else:
            self.write("ebom_id '{0}' not found".format(ebom_id))
            self.set_status(404)
    def post(self):
        data = json.loads(self.request.body)
        ebom_id = data["ebom_id"]
        result = self.books.get_book_by_id(ebom_id)
        if result:
            self.write(result)
            self.set_status(200)
        else:
            self.write("ebom_id '{0}' not found".format(ebom_id))
            self.set_status(404)




