from models.entities.ENotice import ENotice
from models.Database import mysqlConnection
import datetime

class NoticeManager:
    
    
    @classmethod
    def getAll(self):
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM notices ORDER BY notice_id DESC")
        
        rows = cursor.fetchall()
        
        if rows:
            notice_array = []
            for row in rows:
                notice_array.append(ENotice(row[0],row[1],row[2],row[3],row[4]).__dict__)
                
            conexion.close()
            return notice_array
        else:
            conexion.close()
            return None
            
    @classmethod 
    def getById(self, id):
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM notices WHERE notice_id = %s", (id,))
        row = db.cursor().fetchone()
        if row:
            conexion.close()
            return ENotice(row[0],row[1],row[2],row[3],row[4])
        else:
            conexion.close()
            return None
            
    @classmethod
    def create(self, notice):
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        if notice:
            cursor.execute("INSERT INTO notices (notice_title, notice_text, notice_img, notice_date) VALUES (%s, %s, %s, %s)", (notice.title, notice.text, notice.img, actual_date))
            db.commit()
            conexion.close()
            return True
        else:
            conexion.close()
            return False
        
    @classmethod
    def delete(self, id):
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM notices WHERE notice_id = %s", (id,))
        db.commit()
        conexion.close()
        return True

    
    @classmethod
    def update(self, notice):
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        if notice:
            cursor.execute("UPDATE notices SET notice_title = %s, notice_text = %s, notice_img = %s, notice_date = %s WHERE notice_id = %s", (notice.title, notice.text, notice.img, actual_date, notice.id))
            db.commit()
            conexion.close()
            return True
    