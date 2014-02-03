
from base import BaseHandler
from google.appengine.ext import db
from newblog import BlogDB

class PrimaLink(BaseHandler):
    def get(self):
        id = self.request.get("id")
        param = {"id": id}
        # self.render("primalink.html", **param)
        blog = BlogDB.get(long(id))
        param = {"subject": blog.subject, "correct": blog.content}
        self.render("primalink.html",**param)