import sqlite3


class datebase:

    def __init__(self):
        self.conn = sqlite3.connect('datebase.db')
        self.cur = conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS register(
                    id INT PRIMARY KEY UNIQUE not null,
                    login TEXT,
                    password TEXT);""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS rating(
                    id INT PRIMARY KEY,
                    login TEXT,
                    count_win TEXT,
                    count_lose);""")

    def addUser(self, login, password):
        self.cur.execute(f"SELECT * FROM register WHERE login ='{login}';")
        if self.cur.fetchone() is None:
            self.cur.execute(f"INSERT INTO register VALUES (?,?);", (login, password))
        if self.cur.fetchone() is not None:
            pass # вывод окна с сообщением "Такой пользователь уже существует"

    def updateUserPassword(self, login, password):
        self.cur.execute(f"SELECT * FROM register WHERE login ='{login}';")
        if self.cur.fetchone() is not None:
            self.cur.execute(f"UPDATE register SET password = '{password}' WHERE login = '{login}';")
        if self.cur.fetchone() is None:
            pass # вывод окна с сообщением "Неправильный логин"

    def setRecord(self, login, result): #result - победа (1) или поражение (0)
        if result == '1':
            self.cut.execute(f"INSERT INTO rating VAlUES (?,?,?,?)",(user_id, login,))
        if result == '0':