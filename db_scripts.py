import sqlite3


class datebase:

    def __init__(self):
        self.conn = sqlite3.connect('datebase.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS register(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT,
                    password TEXT);""")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS rating(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    login TEXT,
                    count_win INT,
                    count_lose INT);""")

    """
            Метод для проверки входа пользователя
    """

    def checkUser(self, login, password):
        self.cur.execute(f"SELECT * FROM register WHERE login ='{login}' and password = '{password}';")
        res = self.cur.fetchone()
        print(res)
        if res is None:
            return 0       # print("Такого пользователся нет, регистрируйтесь!!!!!")
        if res is not None:
            return 1       # print("Вы вошли, поздравляю")

    """
            Метод для регистрации входа пользователя
    """

    def addUser(self, login, password):
        self.cur.execute(f"SELECT * FROM register WHERE login ='{login}';")
        res = self.cur.fetchone()
        if res is None:
            self.cur.execute("INSERT INTO register (login, password) VALUES (?,?);", (login, password))
            self.conn.commit()
            self.cur.execute("INSERT INTO rating (login, count_win, count_lose) VALUES (?,?,?)", (login, 0, 0))
            self.conn.commit()
        if res is not None:
            print("Данный пользователь уже существует") # вывод окна с сообщением "Такой пользователь уже существует"

    """
            Метод для обновления пароля пользователя в бд
    """

    def updateUserPassword(self, login, password):
        self.cur.execute(f"SELECT * FROM register WHERE login ='{login}';")
        if self.cur.fetchone() is not None:
            self.cur.execute(f"UPDATE register SET password = '{password}' WHERE login = '{login}';")
        if self.cur.fetchone() is None:
            pass # вывод окна с сообщением "Неправильный логин"

    """
            Метод для сохранения результатов игры в рейтинг бд
    """

    def setRecord(self, login, result): #result - победа (1) или поражение (0)
        if result == 1:
            self.cur.execute(f"SELECT count_win FROM rating WHERE login = '{login}'")
            count_win = self.cur.fetchone()
            res = count_win[0] + 1
            self.cur.execute(f"UPDATE rating SET count_win = '{res}' WHERE login = '{login}'")
            self.conn.commit()
        if result == 0:
            self.cur.execute(f"SELECT count_lose FROM rating WHERE login = '{login}'")
            count_lose = self.cur.fetchone()
            res = count_lose[0] + 1
            self.cur.execute(f"UPDATE rating SET count_lose = {res} WHERE login = '{login}'")
            self.conn.commit()

    """
            Метод для получения рейтинга на пользователся в бд
    """

    def getRecord(self, login):
        self.cur.execute(f"SELECT count_win, count_lose FROM rating WHERE login = '{login}'")
        return self.cur.fetchone()

    """
            Метод для получения всех записей из бд рейтинг
    """

    def getAllRecord(self):
        self.cur.execute(f"SELECT login, count_win, count_lose FROM rating ORDER BY count_win DESC")
        return self.cur.fetchall()

    """
            Метод для вывода в консоль всех записей пользователей в бд
    """

    def printRegister(self):
        date = datebase()
        date.cur.execute("SELECT * FROM register")
        print(date.cur.fetchall())

    """
            Метод для вывода в консоль всех рекордов пользователей в бд
    """

    def printRecords(self):
        date = datebase()
        date.cur.execute("SELECT * FROM rating")
        print(date.cur.fetchall())


# if __name__ == '__main__':
#     date = datebase()
#     date.cur.execute(f"UPDATE rating SET count_win = {0}")
#     date.conn.commit()
#     date.cur.execute(f"UPDATE rating SET count_lose = {0}")
#     date.conn.commit()
#     # date.cur.execute("INSERT INTO rating VALUES (5, 'Second player',0,0 )")
#     # date.conn.commit()
#     print(date.cur.fetchall())