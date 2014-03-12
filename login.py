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
        cookie_val = str(self.request.cookies.get(name))
        if cookie_val:
            return cookie_val
        return None

    def get_cookie_user_name(self,name):
        cookie_val_user_name = self.get_cookie(name)
        if cookie_val_user_name:
            return check_hash_val(cookie_val_user_name)
        return None

    def set_cookie(self,name,value):
        self.response.headers.add_header("Set-Cookie",name+value)

    def user_already_signed_up(self,user_name):
        cookie_user_name = self.get_cookie_user_name("user")
        if cookie_user_name == user_name:
            return True

        return False

    def get(self):
        logging.info('LoginHandler get')
        params = {"user_name": ''}

        cookie_user_name = self.get_cookie_user_name("user")
        cookie_user_name_hashed = ''
        if cookie_user_name:
            # Pre-populate user name in field
            params = {"user_name": cookie_user_name}
            cookie_user_name_hashed = str(make_secure_val(cookie_user_name))

        self.set_cookie("user=",cookie_user_name_hashed)
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

        # # If cookie has same use name,show error
        if self.user_already_signed_up(username):
            logging.error('This is problem : User name is %s' %username)
            params["username_error"] = "User already exists"
            redirect = False
        elif redirect:
            logging.info('POST User name : %s' %username)
            cookie_user_name_hash = str(make_secure_val(username))
            logging.info('POST setting cookie : ' + cookie_user_name_hash)
            self.set_cookie("user=",cookie_user_name_hash)

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
