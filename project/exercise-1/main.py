import jinja2
import webapp2 # webapp2 is a module that you import


#set up environment for Jinja
#this sets jinja's relative directory to match the directory name(dirname) of
#the current __file__, in this case, main.py
jinja_environment = jinja2.Environment(
  loader=jinja2.FileSystemLoader("templates"))

class MainHandler(webapp2.RequestHandler):
  def get(self):
    #create your variables as name/value pairs in a dictionary
    my_vars = {"name": "CSSIer"}
    template = jinja_environment.get_template('hello.html')
    my_variables = {"name": 'troy'}
    template.render(my_variables)
    #pass the dictionary of values to render
    self.response.out.write(template.render(my_vars))

# creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
  ('/', MainHandler)], debug=True)
