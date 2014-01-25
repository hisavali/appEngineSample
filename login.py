from base import BaseHandler
import re


class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        userName = self.request.get("username")
        pwd = self.request.get("pwd")
        verify_pwd = self.request.get("verifypwd")
        email = self.request.get("email")

        params = {"user_name": userName, "email": email}

        redirect = True
        if not validate_username(userName):
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

        if not redirect:
            self.render("login.html", **params)
        else:
            self.redirect("/welcome?username="+userName)


def validate_username(username):
    user_re = re.compile('^[a-zA-Z0-9_-]{3,20}$')
    return user_re.match(username)


def validate_password(pwd):
    user_re = re.compile('^.{3,20}$')
    return user_re.match(pwd)


def validate_email(email):
    user_re = re.compile('^[\S]+@[\S]+\.[\S]+$')
    return user_re.match(email)
