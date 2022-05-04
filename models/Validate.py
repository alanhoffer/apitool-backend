import re
from models.entities.EUser import EUser
from models.Variables import EMAIL_REGEX, PASSWORD_REGEX, USERNAME_REGEX, NAMESURNAME_REGEX, PHONE_REGEX, CITY_REGEX


#regex data validation

def emailRegex(email):
    if re.match(EMAIL_REGEX, email):
        return True
    return False

def passwordRegex(password):
    if re.match(PASSWORD_REGEX, password):
        return True
    return False

def usernameRegex(username):
    if re.match(USERNAME_REGEX, username):
        return True
    return False

def fullnameRegex(fullname):
    if re.match(NAMESURNAME_REGEX, fullname):
        return True
    return False
    
def phoneRegex(phone):
    if re.match(PHONE_REGEX, phone):
        return True
    return False

def cityRegex(city):
    if re.match(CITY_REGEX, city):
        return True
    return False

def register(userinfo):
    if emailRegex(userinfo['email']) and passwordRegex(userinfo['password']) and usernameRegex(userinfo['username']) and fullnameRegex(userinfo['name']) and phoneRegex(userinfo['phone']) and cityRegex(userinfo['city']):
        user = EUser(0, userinfo['username'], userinfo['email'], userinfo['password'], userinfo['name'], userinfo['phone'], userinfo['city'])
        return user
    return False

def login(userinfo):
    if usernameRegex(userinfo['username']) and passwordRegex(userinfo['password']):
        user = EUser(0, userinfo['username'], "", userinfo['password'], "", "", "")
        return user
    return False


