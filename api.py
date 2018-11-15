#mdm
#mkm
import os
import tornado.ioloop
import tornado.web
from book import Book
from addhandler import AddHandler
from delhandler import DelHandler
from gethandler import GetHandler
from getidhandler import GetByIdHandler
from getEbomCountHandler import GetEbomCountHandler

books = Book()

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Book Microservice v1")

def make_app():
    return tornado.web.Application([
        (r"/v1", MainHandler),
        (r"/v1/addEbom", AddHandler, dict(books = books)),
        (r"/v1/delEbom", DelHandler, dict(books = books)),
        (r"/v1/getEboms", GetHandler, dict(books = books)),
        (r"/v1/getEbomById", GetByIdHandler, dict(books = books)),
        (r"/v1/getEbomsCount", GetEbomCountHandler, dict(books = books)),
        ])

if __name__ == "__main__":
    app = make_app()
    port = int(os.environ.get("PORT", 9999))
    app.listen(port)
    tornado.ioloop.IOLoop.current().start()
