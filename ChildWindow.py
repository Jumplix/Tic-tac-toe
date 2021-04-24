from tkinter import *

import db_scripts
from PIL import ImageTk, Image

"""
    Для создания дочернего окна используется класс ChildWindows
    Вызов окна осуществляется по кнопке в основном окне
"""


class ChildWindows:
    """
            Конструктор класса ChildWindows
    """
    def __init__(self, parent, width, height, title="Войти", plnumb=0):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)
        self.res = 3
        self.msgtext = ""

        if plnumb == 1:
            self.firstUser = True
            self.secondUser = False
        if plnumb == 2:
            self.firstUser = False
            self.secondUser = True

        self.draw_widgets_child()
        self.grab_focus()

    """
            Метод определяющий фокус дочернего окна
    """
    def grab_focus(self):
        self.root.grab_set()
        self.root.focus()
        self.root.wait_window()

    """
            Метод отрисовки виджетов дочернего окна
    """
    def draw_widgets_child(self):
        if self.firstUser is True:
            self.labelUsName = Label(self.root, text='Игрок 1')
        elif self.secondUser is True:
            self.labelUsName = Label(self.root, text='Игрок 2')

        self.labelLogin = Label(self.root, text='Логин')
        self.textLogin = Entry(self.root, width=30)
        self.labelPassword = Label(self.root, text='Пароль')
        self.textPassword = Entry(self.root, width=30, show="*")
        self.signIn = Button(self.root, text='Войти', command=self.checkLog)
        self.signUp = Button(self.root, text='Зарегистрироваться', command=self.checkReg)
        self.labelMessage = Label(self.root, width=50, text=self.msgtext)

        self.labelUsName.place(relx=.45, rely=.1)
        self.labelLogin.place(relx=.45, rely=.2)
        self.textLogin.place(relx=.32, rely=.3)
        self.labelPassword.place(relx=.45, rely=.4)
        self.textPassword.place(relx=.32, rely=.5)
        self.signIn.place(relx=.3, rely=.6)
        self.signUp.place(relx=.45, rely=.6)
        self.labelMessage.place(relx=.1, rely=.7)

    """
            Метод для проверки входа пользователей в бд
    """

    def checkLog(self):
        db = db_scripts.datebase()
        bcheck = db.checkUser(self.textLogin.get(), self.textPassword.get())
        if bcheck == 1 and self.firstUser:
            print("Entered First")
            self.firstUser = True
            self.firstUserName = self.textLogin.get()
            self.root.destroy()
        if bcheck == 1 and self.secondUser:
            print("Entered Second")
            self.secondUser = True
            self.secondUserName = self.textLogin.get()
            self.root.destroy()
        if bcheck == 0:
            self.msgtext = "Неверный логин или пароль ИЛИ вы не зарегестрированы"
            self.draw_widgets_child()
        db.printRegister()

    """
            Метод для регистрации пользователей в бд
    """

    def checkReg(self):
        db = db_scripts.datebase()
        if self.textLogin.get() != "Bot" and (self.textPassword.get() != "" or self.textPassword.get() != "") and self.textLogin.get() != "bot":
            self.res = db.addUser(self.textLogin.get(), self.textPassword.get())
        if self.textLogin.get() == "Bot" and self.textLogin.get() == "bot":
            print("Зарезервированное имя пользователя")
        db.printRegister()
        if self.res == 1:
            self.msgtext = ""
        if self.res == 0:
            self.msgtext = "Имя занято"
            self.draw_widgets_child()

    """
            Метод для проверки вошел ли пользователь
    """

    def getUser(self, posi):
        if posi == 1:
            return self.firstUser
        elif posi == 2:
            return self.secondUser

    """
            Метод для получения имени пользователя из окна
    """

    def getUserName(self, posi):
        if posi == 1:
            return self.firstUserName
        elif posi == 2:
            return self.secondUserName
