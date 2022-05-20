from models.Database import db, cursor
from models.entities.ENotice import ENotice
import datetime

class NoticeManager:
    
    
    @classmethod
    def getAll(self):
        cursor.execute("SELECT * FROM notices ORDER BY notice_id DESC")
        rows = cursor.fetchall()
        
        if rows:
            notice_array = []
            for row in rows:
                notice_array.append(ENotice(row[0],row[1],row[2],row[3],row[4]).__dict__)
                
                print(type(row[4]))
            return notice_array
        else:
            return None
            
    @classmethod 
    def getById(self, id):
        cursor.execute("SELECT * FROM notices WHERE notice_id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return ENotice(row[0],row[1],row[2],row[3],row[4])
        else:
            return None
            
    @classmethod
    def create(self, notice):
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        if notice:
            cursor.execute("INSERT INTO notices (notice_title, notice_text, notice_img, notice_date) VALUES (%s, %s, %s, %s)", (notice.title, notice.text, notice.img, actual_date))
            db.commit()
            return True
        else:
            return False
        
    @classmethod
    def delete(self, id):
        cursor.execute("DELETE FROM notices WHERE notice_id = %s", (id,))
        db.commit()
        return True

    
    @classmethod
    def update(self, notice):
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        if notice:
            cursor.execute("UPDATE notices SET notice_title = %s, notice_text = %s, notice_img = %s, notice_date = %s WHERE notice_id = %s", (notice.title, notice.text, notice.img, actual_date, notice.id))
            db.commit()
            return True
    