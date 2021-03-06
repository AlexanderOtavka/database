import cgi
from google.appengine.ext import ndb
import webapp2
import jinja2
import os
import random

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/client"))

class Data(ndb.Model):
  content = ndb.StringProperty()

class Home(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')

        self.response.write(template.render())

class Add_Name(webapp2.RequestHandler):
    def post(self):
        name = Data(content=cgi.escape(self.request.get('name')))
        name.put()

        self.redirect('/')

class Inner(webapp2.RequestHandler):
    def post(self):
        names = Data.query().fetch()
        template = JINJA_ENVIRONMENT.get_template('index.html')

        if len(names) == 0:
            self.response.write(template.render({'name': 'Please Enter a Name'}))
        else:
            name = random.choice(names)
            name.key.delete()
            self.response.write(template.render({'name': name.content}))

app = webapp2.WSGIApplication([
    ('/', Home),
    ('/addname', Add_Name),
    ('/inner', Inner),
], debug=True)
