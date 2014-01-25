import os
import webapp2
import jinja2
from base import BaseHandler

class ROT13Handler(BaseHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.out.write(self.request)
        return self.render("rot13.html")

    def post(self):
        orig = self.request.get('text')
        new_text = self.rot13(orig)
        return self.render("rot13.html", new_text=new_text)

    # self.response.headers['Content-Type']='text/plain'
    # self.response.out.write(self.request)


    def rot13(self, client_str):
        if client_str:
            output = []
            for c in client_str:
                print 'Processing character %s' % c
                if c.isalpha():
                    if ord(c) in range(ord('a'), ord('m') + 1):
                        c = chr(ord(c) + 13)
                    elif ord(c) in range(ord('A'), ord('M') + 1):
                        c = chr(ord(c) + 13)
                    elif ord(c) in range(ord('n'), ord('z') + 1):
                        c = chr(ord(c) - 13)
                    elif ord(c) in range(ord('N'), ord('Z') + 1):
                        c = chr(ord(c) - 13)
                output.append(c)
        return ''.join(output)