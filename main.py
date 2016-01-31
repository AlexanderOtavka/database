import cgi
from google.appengine.ext import ndb
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/client"))

class Name(ndb.Model):
  content = ndb.StringProperty()

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')

        #Queries for names in datastore
        qry = Name.query()

        self.response.write(template.render({ 'names': qry.fetch() }))

class About_Page(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class Store_Data(webapp2.RequestHandler):
    def post(self):
        name = Name(content=self.request.get('name')) #Creates in memory
        name.put() #Write to datastore
        self.redirect('/#refresh')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/add', Store_Data),
    ('/about', About_Page),
], debug=True)
