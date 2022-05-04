
from models.entities.EApiary import EApiary
from models.Database import db, cursor

class ApiaryManager():
    
    @classmethod
    def createApiary(self, apiary):
        if len(apiary.name) > 5:
            cursor.execute("INSERT INTO apiarys (userid, name) VALUES (%s, %s)", (apiary.userid , apiary.name))
            db.commit()
            return True
        else:
            return False
        

    

    @classmethod
    def updateApiary(self, apiary):
        cursor.execute("UPDATE apiarys SET name = %s, location = %s WHERE apiaryid = %s", (apiary.name, apiary.location, apiary.id))
        db.commit()
        return True

    @classmethod
    def getApiaries(self, userid):
        cursor.execute("SELECT * FROM apiarys WHERE userid = %s", (userid,))
        rows = cursor.fetchall()
        apiaries = []
        for row in rows:
            apiaries.append(EApiary(row[0], row[11], row[1], row[2], row[3], row[4],row[5],row[6], row[7], row[8], row[9], row[10]).__dict__)
        return apiaries