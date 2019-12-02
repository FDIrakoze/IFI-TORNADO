from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
import json
import asyncio

items = []

class printItems(RequestHandler):
    # TODO

class TodoItem(RequestHandler):
  def post(self):
    # add the item in items
    # TODO
    self.write({'message': 'new item added'})

  def delete(self, id):
    # Delete the item in items
    # TODO
    self.write({'message': 'Item with id %s was deleted' % id})


def make_app():
  urls = [
    ("/", printItems),
    (r"/api/item/([^/]+)?", TodoItem)
  ]
  return Application(urls, debug=True)
  
if __name__ == '__main__':
    # TODO

