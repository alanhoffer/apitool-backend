from distutils.command.config import config
import pymysql


def mysqlConnection():
    return pymysql.connect(
                host='localhost',
                user='root',
                password='15441109',
                db='apitool_test'
            )