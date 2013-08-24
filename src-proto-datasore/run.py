import os
import sys
from todo_app.views import MainPage

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))
from google.appengine.ext import endpoints
from todo_app.apis import TodoApi
import webapp2

api = endpoints.api_server([TodoApi], restricted=False)
app = webapp2.WSGIApplication([('/', MainPage)],
                              debug=True)