import jinja2
import os
import webapp2 # webapp2 is a module that you import


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
              self.response.out.write('tay tay')
      else:
              self.response.out.write(template.render(string))
# creates a WSGIApplication and assigns it to the variable app.
app = webapp2.WSGIApplication([
  ('/', MainHandler), ("/submission",FormHandler)],debug=True)
