
import os
import webapp2
import jinja2

template_dir=os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

def render_str(template, **params):
    temp = jinja_environment.get_template(template)
    return temp.render(params)

class BaseHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, template, **kw):
        return self.response.out.write(render_str(template, **kw))
