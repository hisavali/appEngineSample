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
from google.appengine.api import users
import cgi

from test import valid_month,valid_day,valid_year,escape_html

import jinja2
import os

form="""
<form>
<select name="q">
<option value="1">There is only One</option>
<option>Two</option>
<option>Three</option>
</select>
</br>
<input type="submit">
</form>
"""

form1="""
<form>
<label> 
One
<input type="radio" name="q" value="One">
</label></br>
<label>
Two
<input type="radio" name="q" value="Two">
</label> </br>
<label>
Three
<input type="radio" name="q" value="Three">
</label>
</br>
<input type="submit">
"""


form2="""
<form method="post">
Your birthday?
</br>
</br>
<label>
Month
<input type="text" name="month" value="%(month)s">
</label>

<label>
Day
<input type="text" name="day" value="%(day)s">
</label>

<label>
Year
<input type="text" name="year" value="%(year)s">
</label>

</br>

<div style="color:red">%(error)s</div>

<input type="submit">
</form>
"""
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = jinja_environment.get_template('index.html')
		self.response.out.write(template.render())

class MainHandler1(webapp2.RequestHandler):
    def get(self):

#    	user = users.get_current_user()

#    	if user:
#    		self.response.write('Hello,' + user.nickname())
#    	else:
#    		self.redirect(users.create_login_url(self.request.uri))
		self.response.out.write(form)


class MainHandler2(webapp2.RequestHandler):
	"""docstring for MainHandler2"""
	def write_form(self,error="",month="",day="",year=""):
		self.response.out.write(form2 % {"error":error,
										  "month":escape_html(month),
										   "day":escape_html(day),
										   "year":escape_html(year)})

	def get(self):
		self.write_form("")

	def post(self):
		
		month = self.request.get('month')
		day = self.request.get('day')
		year = self.request.get('year')

		user_month = valid_month(month)
		user_day = valid_day(day)
		user_year = valid_year(year)

		if not (user_month and user_day and user_year):
			return self.write_form("There is error",month,day,year)
		else:
			return self.response.out.write("That is fine")
		

class Guestbook(webapp2.RequestHandler):
	def post(self):
		self.response.out.write('<html><body>You wrote:<prep>')
		self.response.out.write(cgi.escape(self.request.get('content')))
		self.response.out.write('</prep></body></html>')

app = webapp2.WSGIApplication([
    ('/', MainHandler2),
    #('/', MainHandler1),
    ('/sign',Guestbook)], debug=True)