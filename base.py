
import os
import webapp2
import jinja2

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), autoescape=True)

def render_str(template, **params):
    temp = jinja_environment.get_template(template)
    return temp.render(params)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        return self.response.out.write(render_str(template, **kw))
