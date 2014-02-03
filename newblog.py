
import os
from google.appengine.ext import db
from base import BaseHandler

class BlogDB(db.Model):
    subject = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    date_created = db.DateProperty(auto_now_add = True)
    pass

class NewBlog(BaseHandler):
    def get(self):
        self.render("newblog.html")

    def post(self):
        # self.response.headers['Content-Type']='text/plain'
        # self.response.out.write(self.request)
        subject = self.request.get("subject")
        content = self.request.get("content")

        if not subject or not content:
            param = dict()
            param["error_content"] = "Please enter correct data"
            param["subject"] = subject
            param["content"] = content
            self.render("newblog.html", **param)
        else:
            newblog = BlogDB(subject=subject,content=content)
            newblog.put()

            self.redirect('/primalink?id='+str(newblog.key().id()))
            pass


