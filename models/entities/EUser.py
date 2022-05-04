from werkzeug.security import generate_password_hash, check_password_hash


class EUser():
    def __init__(self, userid, username="", email="", password="", name="", phone="", city="", permissions="") -> None:
        self.userid = userid
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.phone = phone
        self.city = city
        self.permissions = permissions
    
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)
    
    @classmethod
    def generate_password_hash(self, password):
        return generate_password_hash(password)
    
    
