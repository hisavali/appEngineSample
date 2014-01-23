
import webapp2
from test import escape_html

rot_form="""
<form method="post">
<textarea rows="10" cols="30" name="text">%(new_text)s
</textarea>
</br>
</br>

<input type="submit">

</form>
"""
class ROT13Handler(webapp2.RequestHandler):
	def get(self):
		# self.response.headers['Content-Type']='text/plain'
		# self.response.out.write(self.request)
		return self.write_textForm("")

	def post(self):
		orig = self.request.get ('text')
		return self.write_textForm(orig.upper())
		# self.response.headers['Content-Type']='text/plain'
		# self.response.out.write(self.request)

	def write_textForm(self,text_value=""):
		return self.response.out.write(rot_form % {"new_text":escape_html(text_value)})
