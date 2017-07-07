import json
import jinja2
import os
import webapp2 # webapp2 is a module that you import
import random
import urllib2
import urllib

#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    #create your variables as name/value pairs in a dictionary
    my_vars = {"name": "CSSIer"}
    template = jinja_environment.get_template('templates/first.html')
    my_variables = {"name": 'troy'}
    template.render(my_variables)
    #pass the dictionary of values to render
    self.response.out.write(template.render(my_vars))

class FormHandler(webapp2.RequestHandler):
  def post(self):

      template = jinja_environment.get_template('templates/hello.html')
      mg=self.request.get("mg")
      mg2=self.request.get("mg2")
      mg3=self.request.get("mg3")
      mg4=self.request.get("mg4")
      mg5=self.request.get("mg5")
      mg6=self.request.get("mg6")
      mg7=self.request.get("mg7")
      string={"mg": mg,"mg2": mg2,"mg3": mg3,"mg4": mg4,"mg5": mg5,"mg6": mg6,"mg7": mg7}
      anything_missing = False


      for value in string.values():
          if value == "":
              anything_missing = True

      if anything_missing == True:
              self.response.out.write('nope')
      else:
              self.response.out.write(template.render(string))

class ResultHandler(webapp2.RequestHandler):
   def get(self):

     #
      base_url = "http://api.giphy.com/v1/gifs/search?"
      url_params = {'q': self.request.get("answer"), 'api_key': 'dc6zaTOxFJmzC', 'limit': 10}
      giphy_response = urllib2.urlopen(base_url + urllib.urlencode(url_params)).read()

      content_dict = json.loads(giphy_response)
      gif_url = content_dict['data'][0]['images']['original']['url']
      self.response.write(gif_url)
      template = jinja_environment.get_template('templates/results.html')
      hg=self.request.get("answer")
      hg={"gif_url":gif_url}

      self.response.out.write(template.render(hg))
# creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
  ('/', MainHandler), ("/submission",FormHandler),
  ('/results',ResultHandler)],debug=True)
