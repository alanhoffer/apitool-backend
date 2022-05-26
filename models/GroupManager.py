from calendar import c
from flask import jsonify
from models.entities.EUser import EUser
from models.Database import mysqlConnection

class GroupManager:
    
    @classmethod
    def createGroup(self, userid,group):
        cursor.execute("SELECT * FROM workgroup WHERE  name = %s", (group.name,))
        row = cursor.fetchone()
        if row == None:
            cursor.execute("INSERT INTO workgroup (groupid, name) VALUES (%s, %s)", (group.id, group.name))
            db.commit()
            #Group dont exist with that name and be created
            return True
        else:
            #Group exist with that name
            return False
        
    @classmethod
    def joinGroup(self, userid, groupname):
        cursor.execute("SELECT * FROM userworkgroup WHERE userid = %s", (userid))
        row = cursor.fetchone()

        if row == None:
            
            #user dont have group & checking if group exists
            cursor.execute("SELECT * FROM workgroup WHERE  name = %s", (groupname))
            groupid = cursor.fetchone()
            if groupid:
                #group exists joining
                cursor.execute("INSERT INTO userworkgroup (userid, groupid) VALUES (%s, %s)", (userid, groupid[0]))
                db.commit()
                return True
            else: 
                #group doesnt exist
                return False
        else:
            return jsonify({"msg": "User already in group"})

    def getGroup(self, userid):
        cursor.execute("SELECT * FROM userworkgroup WHERE userid = %s", (userid))
        row = cursor.fetchone()
        if row != None:
            cursor.execute("SELECT * FROM workgroup WHERE groupid = %s", (row[1],))
            group = cursor.fetchone()
            return group
        else:
            return False
    
    def leaveGroup(self, userid):
        cursor.execute("SELECT * FROM userworkgroup WHERE userid = %s", (userid))
        row = cursor.fetchone()
        if row != None:
            cursor.execute("DELETE FROM userworkgroup WHERE userid = %s", (userid))
            db.commit()
            return True
        else:
            return False
        
    def delGroup(self, groupid):
        cursor.execute("SELECT * FROM userworkgroup WHERE groupid = %s", (groupid))
        row = cursor.fetchone()
        if row != None:
            cursor.execute("DELETE FROM userworkgroup WHERE groupid = %s", (groupid))
            cursor.execute("DELETE FROM workgroup WHERE groupid = %s", (groupid))
            db.commit()
            return True
        else:
            return False