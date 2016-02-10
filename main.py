import cgi
from google.appengine.ext import ndb
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/client"))

class Data(ndb.Model):
  content = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')

        self.response.write(template.render())

class About(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class Inner(webapp2.RequestHandler):
    def post(self):
        name = Data(content=cgi.escape(self.request.get('name'))) #Creates in memory
        name.put() #Write to datastore

        self.redirect('/#refresh')

class Outer(webapp2.RequestHandler):
    def post(self):
        print "Outer"

        self.redirect('/#refresh')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/inner', Inner),
    ('/outer', Outer),
    ('/about', About),
], debug=True)
