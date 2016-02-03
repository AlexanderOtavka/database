import cgi
from google.appengine.ext import ndb
import webapp2
import jinja2
import os


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/client"))

class Data(ndb.Model):
  content = ndb.StringProperty()
  password = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)

class IP(ndb.Model):
    ip_address = ndb.StringProperty()

class Home(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('login.html')
        self.response.write(template.render())

class Check_Password(webapp2.RequestHandler):
    def get(self):
        password = Data(content=cgi.escape(self.request.get('password')))
        if(password == "duncan11"):
            self.redirect('/database')
        else:
            pass

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')

        #Queries for names in datastore
        qry = Data.query()

        self.response.write(template.render({ 'names': qry.fetch() }))

class About_Page(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('about.html')
        self.response.write(template.render())

class Store_Data(webapp2.RequestHandler):
    def post(self):
        name = Data(content=cgi.escape(self.request.get('name'))) #Creates in memory
        name.put() #Write to datastore

        date = Data(content=cgi.escape(self.request.get('date')))
        date.put()

        ip = self.request.get(remote_addr)
        print ip
        ipadress = IP(ip_address=self.request.get('ipadress'))
        log = IP()
        log.ip_address = ip
        log.put()

        self.redirect('/#refresh')

app = webapp2.WSGIApplication([
    ('/', Home),
    #('/password', Check_Password),
    #('/database', MainPage),
    #('/add', Store_Data),
    ('/about', About_Page),
], debug=True)
