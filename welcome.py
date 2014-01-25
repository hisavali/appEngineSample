
from base import BaseHandler

class WelcomeHandler(BaseHandler):
    def get(self):
        un = self.request.get("username")
        return self.render("welcome.html", username= un)
