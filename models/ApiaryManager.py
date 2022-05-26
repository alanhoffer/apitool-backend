
from models.entities.EApiary import EApiary
from models.Database import mysqlConnection
import datetime

class ApiaryManager():
    
    @classmethod
    def createApiary(self, apiary):
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        sql = "INSERT INTO apiarys (name, userid, profile_img, note_text, created_at, updated_at, hives_quantity, food_quantity, eprotection_status, status, flumetrine_quantity, amitraz_quantity, oxalic_quantity, oxytetracycline_quantity, suplements_promotorl, suplements_beepower) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (apiary.name, apiary.userid, apiary.profile_img, apiary.note_text, actual_date, actual_date, apiary.hives_quantity, apiary.food_quantity, apiary.eprotection_status, apiary.status, apiary.flumetrine_quantity, apiary.amitraz_quantity, apiary.oxalic_quantity, apiary.oxytetracycline_quantity, apiary.suplements_promotorl, apiary.suplements_beepower))
        db.commit()
        return cursor.lastrowid
        

    @classmethod
    def getApiaries(self, userid):
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        
        cursor.execute("SELECT * FROM apiarys WHERE userid = %s", (userid,))
        rows = cursor.fetchall()
        apiaries = []
        for row in rows:
            apiaries.append(EApiary(row[0], row[1], row[2], row[3], row[4],row[5],row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]).__dict__)
        conexion.close()
        return apiaries
    
    @classmethod
    def getApiaryById(self, apiaryid):
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM apiarys WHERE apiaryid = %s", (apiaryid,))
        row = cursor.fetchone()
        if row:
            conexion.close()
            return EApiary(row[0], row[11], row[1], row[2], row[3], row[4],row[5],row[6], row[7], row[8], row[9], row[10])
        
    @classmethod
    def updateApiary(self, apiary):
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        actual_date = datetime.datetime.now().strftime("%Y"+"-%m"+"-%d")
        if apiary:
            cursor.execute("UPDATE apiarys SET name = %s, descripcion = %s, profileimg = %s, updated_date = %s, cantcolonias = %s, cantalimento = %s, cantbaterias = %s, cantvarroa = %s, cantantibiotico = %s WHERE apiaryid = %s", (apiary.name, apiary.description, apiary.image_url, actual_date, apiary.cantcolonias, apiary.cantalimento, apiary.cantbaterias, apiary.cantvarroa, apiary.cantantibiotico, apiary.id))
            conexion.commit()
            conexion.close()
            return True
    
    @classmethod
    def deleteApiary(self, apiaryid):
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("DELETE FROM apiarys WHERE apiaryid = %s", (apiaryid,))
        conexion.commit()
        conexion.close()
        return True
    
    @classmethod
    def createApiaryConfig(self, config): 
        
        conexion = mysqlConnection()
        cursor = conexion.cursor()
        
        cursor.execute("INSERT INTO apiary_config (apiaryid, hive_quantity, apiary_food_quantity, apiary_note_record, apiary_electric_protection, apiary_status, health_flumetrine, health_amitraz, health_oxalic, antibiotic_oxytetracycline, suplements_promotorl, suplements_beepower, apiary_mode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (config.apiaryid, config.hive_quantity, config.apiary_food_quantity, config.apiary_note_record, config.apiary_electric_protection, config.apiary_status, config.health_flumetrine, config.health_amitraz, config.health_oxalic, config.antibiotic_oxytetracycline, config.suplements_promotorl, config.suplements_beepower, config.apiary_mode))
        conexion.commit()
        conexion.close()
        return True
        
        

