
from base import BaseHandler
from google.appengine.ext import db
from newblog import BlogDB
import logging


class PrimaLink(BaseHandler):
    def get(self,blog_id):
        # id = self.request.get("blog_id")
        logging.info(type(blog_id))
        logging.info("value" + blog_id)
        blog = BlogDB.get_by_id(int(blog_id))
        param = {"id": blog_id,"subject": blog.subject, "content": blog.content}
        self.render("primalink.html",**param)