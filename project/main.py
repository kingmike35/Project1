#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class PassHandler(webapp2.RequestHandler):
    def post(self):
        a = 'user'
        b = 'word'
        c = 'other'
        d = 'stuff'
        username = self.request.get("username")
        password = self.request.get("password")
        if username == a or c and password == b or d:
                self.response.write("you are in")
        else:
                self.response.write('no')

class FormHandler(webapp2.RequestHandler):
            def get(self):
                name=self.request.get('name')
                self.response.write(name)
                name=self.request.get('color')
                self.response.write(name)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/submission',FormHandler),
    ('/login', PassHandler),
], debug=True)
