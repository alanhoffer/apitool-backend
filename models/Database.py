from distutils.command.config import config
import pymysql

db = pymysql.connect(
    host='localhost',
    user='root',
    password='15441109',
    db='apitool_test'
)

cursor = db.cursor()