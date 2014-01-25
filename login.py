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

        redirect=True
        error_username = ""
        if not self.validate_username(userName):
            error_username = "wrong username"
            redirect = False

        error_password = "Wrong password"
        if pwd == verify_pwd:
            if self.validate_password(pwd) and self.validate_password(verify_pwd):
                error_password = ""

        if not error_password == "":
            redirect  = False

        error_email = ""
        if email and not self.validate_email(email):
            error_email = "wrong email"
            redirect = False

        if not redirect:
            params = {"user_name": userName, "pwd": pwd, "verify_pwd": verify_pwd, "email": email,
                  "username_error": error_username, "pwd_error": error_password, "verify_pwd_error": error_password, "email_error": error_email}

            self.render("login.html", **params)
        else:
            self.redirect("/welcome?username=")

    def validate_username(self, username):
        USER_RE = re.compile("^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(username)

    def validate_password(self, pwd):
        USER_RE = re.compile("^.{3,20}$")
        return USER_RE.match(pwd)

    def validate_email(self, email):
        USER_RE = re.compile("^[\S]+@[\S]+\.[\S]+$")
        return USER_RE.match(email)