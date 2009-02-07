import cgi
import os
import re
import Cookie

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db

#test

class MainPage(webapp.RequestHandler):
  def get(self):

    target = 'index.html'            
    template_values = {
      'test': 'hello world'
      }

    path = os.path.join(os.path.dirname(__file__), target)
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage)],debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
