
import webapp2

rot_form="""<textarea rows="10" cols="30" name="text" value="%(new_text)s") method="post">
</textarea>
</br>
</br>

<input type="submit">
"""
class ROT13Handler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type']='text/plain'
		self.response.out.write(self.request)
		# return self.response.out.write(rot_form)

	def post(self):
		#orig = self.request.get ('text')
		#return self.write_textForm("That is fine")
		self.response.headers['Content-Type']='text/plain'
		self.response.out.write(self.request)

	def write_textForm(self,text_value=""):
		return self.response.out.write(rot_form % {"new_text":text_value})
