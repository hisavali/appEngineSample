__author__ = 'JyotiSavaliya'

import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

# Implement the function valid_pw() that returns True if a user's password
# matches its hash. You will need to modify make_pw_hash.

def make_pw_hash(name, pw,salt):
    #salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt_value = h.split(',')[1]
    if h == make_pw_hash(name, pw,salt_value):
        return True

    return False

def f():
    salt= make_salt()
    h = make_pw_hash('abc','xyz',salt)
    print valid_pw('abc','xyz',h)

