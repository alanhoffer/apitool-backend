from models.entities.EUser import EUser
from models.Database import mysqlConnection

class Auth:
    
    @classmethod
    def login(self, user):
        try:
            conexion = mysqlConnection()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
            row = cursor.fetchone()
            if row != None:
                user = EUser(row[0], row[1], row[2], EUser.check_password(row[3], user.password), row[4], row[5])
                conexion.close()
                return user
            conexion.close()


        except Exception as e:
            raise (Exception(e))
    
    @classmethod
    def register(self,user):
        try:
            conexion = mysqlConnection()
            cursor = conexion.cursor()
            
            cursor.execute("SELECT * FROM users WHERE username = %s", (user.username,))
            row = cursor.fetchone()
            if row == None:
                cursor.execute("INSERT INTO users (username, email, password, name, phone, city) VALUES (%s, %s, %s, %s, %s, %s)", (user.username, user.email, EUser.generate_password_hash(user.password), user.name, user.phone, user.city))
                
                db.commit()
                cursor.execute("SELECT * FROM users WHERE email = %s", (user.email,))
                row = cursor.fetchone()
                user = EUser(row[0], row[1], row[2], EUser.generate_password_hash(user.password), row[4], row[5])
                conexion.close()
                return user
            else:
                conexion.close()
                return False
        except Exception as e:
            raise (Exception(e))
    

        
        
