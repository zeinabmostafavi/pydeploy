from datetime import datetime
from os import name
from sqlite3 import connect



class Database:

    @staticmethod
    def insert(id,title,desceription,time,status):
        try:
            my_con = connect('todo.db')
            my_cursor = my_con.cursor()

            time = datetime.now()
            time = time.strftime("%Y-%m-%d %H:%M")
            my_cursor.execute(
                f"INSERT INTO tasks(id,title,desceription,time,status) VALUES('{id}','{title}', '{desceription}','{time}','{status}')")
            my_con.commit()
            my_con.close()
            return True
        except Exception as e:
            print("error:", e)
            return False

    @staticmethod
    def select():
        try:
            my_con = connect('todo.db')
            my_cursor = my_con.cursor()
            my_cursor.execute("SELECT * FROM tasks")
            result = my_cursor.fetchall()
            my_con.close()
            return result
        except Exception as e:
            print("error:", e)
            return []

