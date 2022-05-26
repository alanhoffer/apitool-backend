from models.Database import mysqlConnection
from models.entities.EFriend import EFriend


class FriendManager:
    
    @classmethod
    def addFriend(self, userid, friendid):
        cursor.execute("SELECT * FROM friends WHERE userid = %s AND friendid = %s", (userid, friendid))
        row = cursor.fetchone()
        if row == None:
            cursor.execute("INSERT INTO friends (userid, friendid) VALUES (%s, %s)", (userid, friendid))
            db.commit()
            return True
        else:
            return False
    
    