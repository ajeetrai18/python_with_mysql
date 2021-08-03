import mysql.connector as connector


class DBHelper:
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='root',
                                     database='pythontest',
                                     auth_plugin='mysql_native_password')
        query = 'create table if not exists user(userId int primary key,userName varchar(40),phone varchar(40))'
        cur = self.con.cursor()
        cur.execute(query)
        print("created")

    # insert
    def insert_user(self, userid, username, phone):
        query = "insert into user(userid,username,phone)" \
                "values({},'{}','{}')".format(userid, username, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # Fetch All
    def fetch_all(self):
        query = "select * from user;"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(f' userid: {row[0]}, userName: {row[1]},phone: {row[2]}')

    # Delete user

    def delete_user(self, userId):
        query = "delete from user where userId={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Deleted")

    # update

    def update_user(self, userid, new_name, new_phone):
        query = "update user set userName='{}',phone='{}' where userId={}".format(new_name, new_phone, userid)
        print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

