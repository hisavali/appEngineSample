from base import BaseHandler
import re
import hashlib
import logging

def make_hash(val):
    hash = hashlib.md5(val).hexdigest()
    # logging.info('Make_hash: hash ' + hash)
    return hash

def make_secure_val(s):
    return "%s|%s" % (s, make_hash(s))

def check_hash_val(val):
    usr = val.split("|")[0]
    if val == make_secure_val(usr):
        return usr

class LoginHandler(BaseHandler):

    def get_cookie(self,name):
        self.cookie_val = str(self.request.cookies.get(name))
        if self.cookie_val:
            return self.cookie_val

        return None

    def process_get_request_cookie(self):
        if self.get_cookie("user"):
            self.cookie_val_username = str(check_hash_val(self.cookie_val))
            if self.cookie_val_username:
                return self.cookie_val_username

        return None

    def get(self):
        logging.info('LoginHandler get')
        params = {"user_name": ''}
        # self.process_cookie_secure_username()

        if self.process_get_request_cookie():
            # Pre-populate user name in field
            params = {"user_name": self.cookie_val_username}
            self.cookie_val = str(make_secure_val(self.cookie_val_username))

        # logging.info('Get setting cookie : ' + cookie_secure_username_val)
        self.response.headers.add_header("Set-Cookie","user="+self.cookie_val)
        self.render("login.html", **params)

    def post(self):
        logging.info('LoginHandler post')

        username = self.request.get("username")
        pwd = self.request.get("password")
        verify_pwd = self.request.get("verify")
        email = self.request.get("email")

        params = {"user_name": username, "email": email}
        redirect = True

        if not validate_username(username):
            params["username_error"] = "wrong username"
            redirect = False

        if not (validate_password(pwd) and validate_password(verify_pwd)):
            params["pwd_error"] = "Please enter valid Password"
            redirect = False
        elif pwd != verify_pwd:
            params["verify_pwd_error"] = "Passwords don't match"
            redirect = False

        if email and not validate_email(email):
            params["email_error"] = "wrong email"
            redirect = False

        cookie_username = self.request.cookies.get("user")
        logging.debug('cookie_username : %s' % cookie_username)

        cookie_username_val = ''
        cookie_secure_username_val = ''

        if cookie_username:
            cookie_username_val = str(check_hash_val(cookie_username))
            # logging.debug('cookie_username_val : %s' % cookie_username_val)
        elif username:
            # User visiting our web page first time.
            # logging.debug('First time user : %s' % username)
            cookie_secure_username_val = str(make_secure_val(username))

        # # If cookie has same use name,show error
        if cookie_username_val == username:
            logging.error('This is problem : User name is %s' %username)
            params["username_error"] = "User already exists"
            redirect = False
        elif redirect:
            logging.info('POST setting cookie : ' + cookie_secure_username_val)
            self.response.headers.add_header("Set-Cookie","user="+cookie_secure_username_val)

        if not redirect:
            self.render("login.html", **params)
        else:
            self.redirect("/welcome")


def validate_username(username):
    user_re = re.compile('^[a-zA-Z0-9_-]{3,20}$')
    return user_re.match(username)


def validate_password(pwd):
    user_re = re.compile('^.{3,20}$')
    return user_re.match(pwd)


def validate_email(email):
    user_re = re.compile('^[\S]+@[\S]+\.[\S]+$')
    return user_re.match(email)
