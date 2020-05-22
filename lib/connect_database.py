import pymysql.cursors
from conf.readConfig import ReadConfig

class Conne_DB():
    def conne_db(self):
        host = ReadConfig().get_db("host")
        port = ReadConfig().get_db("port")
        user = ReadConfig().get_db("user")
        password = ReadConfig().get_db("password")
        db = ReadConfig().get_db("db")
        sql = ReadConfig().get_db("sql")
        print(host,port,user,password,db,sql)

        connect = pymysql.Connect(
                host=host,
                port=int(port),
                user=user,
                password=password,
                db=db,
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor
            )

        cursor = connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data)
        print(data["total_consumption"])

if __name__ == "__main__":
    Conne_DB().conne_db()
