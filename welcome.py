
from base import BaseHandler
from login import check_hash_val

class WelcomeHandler(BaseHandler):
    def get(self):
        un = ''
        cookie_username = self.request.cookies.get("user")
        cookie_secure_username_val = ''
        if cookie_username:
            un = str(check_hash_val(cookie_username))

        return self.render("welcome.html", username= un)
