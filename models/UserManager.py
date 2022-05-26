from models.entities.EUser import EUser
from models.Database import mysqlConnection
  
class UserManager:
    
    @classmethod
    def get_user_by_id(self, userid=""):
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        try:
            cursor.execute("SELECT * FROM users WHERE userid = %s", (userid,))
            row = cursor.fetchone()
            if row != None:
                user = EUser(row[0], row[1], row[2], row[3], row[4], row[5], row[7], row[8], row[9]).__dict__
                conexion.close()
                return user
            
            conexion.close()
            
        except Exception as e:
            raise (Exception(e))

