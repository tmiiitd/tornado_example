#mdm
#mdm
import tornado.web
import book
import json


class GetEbomCountHandler(tornado.web.RequestHandler):
    def initialize(self, books):
        self.books = books
        
    def get(self):
    	#self._n = len(Board)
        #self.write()
        self.write("'{0}'".format(self.books.get_number_of_eboms()))
        #self.write(json.dumps(self.books.json_list(), indent=4, sort_keys=True))

