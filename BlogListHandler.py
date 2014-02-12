
from base import BaseHandler
from google.appengine.ext import db
from newblog import BlogDB

class BlogListHandler(BaseHandler):
    def get(self):

        blogs = BlogDB.all()
        self.render("blogs.html",blogs=blogs)
        pass

