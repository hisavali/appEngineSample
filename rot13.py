
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
		return self.write_textForm(self.rot13(orig))
		# self.response.headers['Content-Type']='text/plain'
		# self.response.out.write(self.request)

	def write_textForm(self,text_value=""):
		return self.response.out.write(rot_form % {"new_text":escape_html(text_value)})


def rot13(client_str):
		if client_str:
			output=[]
			for c in client_str:
				if c.isalpha():
					if ord(c) in range(ord('a'),ord('m')) or range(ord('A'),ord('M')):
						c = chr(ord(c) + 13)
					elif ord(c) in range(ord('n'),ord('z')) or range(ord('N'),ord('Z')):
						c = chr(ord(c) - 13)
				output.append(c)
		return str(output)

# print rot13("zzzz")

