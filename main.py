import cgi
from google.appengine.ext import ndb
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/client"))

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

class About_Page(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class Display_Data(webapp2.RequestHandler):
    content = nbd.StringProperty()
    model = content.Display_Data(content='foo')
    model.content = "bar"

    content = self.request.get()
    def post(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', Display_Data),
    ('/about', About_Page),
], debug=True)
