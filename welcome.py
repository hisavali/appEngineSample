
from base import BaseHandler
from login import check_hash_val
import  datetime,calendar
from email.utils import formatdate
import logging

class WelcomeHandler(BaseHandler):
    def get(self):
        logging.info('GET Welcome handler')
        un = ''
        cookie_username = self.request.cookies.get("user")
        if cookie_username:
            logging.info('Cookie Value : ' + cookie_username)
        cookie_secure_username_val = ''
        if cookie_username:
            un = str(check_hash_val(cookie_username))
            now = datetime.datetime.utcnow()
            timestamp = calendar.timegm(now.utctimetuple())
            expires = formatdate(timestamp, localtime=False,usegmt=True)
            self.response.headers.add_header("Set-Cookie", "user="+str(cookie_username), expires=expires)
            return self.render("welcome.html", username= un)
        else:
            params = {}
            self.redirect("/signup",**params)
