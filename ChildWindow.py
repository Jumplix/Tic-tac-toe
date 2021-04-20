from tkinter import *

import db_scripts

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

        """
            TODO:Сделать класс, который будет получать инофрмацию об активных пользователях
        """
        if plnumb == 1:
            self.firstUser = True
            self.secondUser = False
        if plnumb == 2:
            self.firstUser = False
            self.secondUser = True

        self.labelLogin = Label(self.root, text='Логин')
        self.textLogin = Entry(self.root, width=30)
        self.labelPassword = Label(self.root, text='Пароль')
        self.textPassword = Entry(self.root, width=30, show="*")
        self.signIn = Button(self.root, text='Войти', command=self.checkLog)
        self.signUp = Button(self.root, text='Зарегистрироваться', command=self.checkReg)

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
            self.labelLogin = Label(self.root, text='Игрок 1')
        elif self.secondUser is True:
            self.labelLogin = Label(self.root, text='Игрок 2')

        self.labelLogin.pack()
        self.textLogin.pack()
        self.labelPassword.pack()
        self.textPassword.pack()
        self.signIn.pack()
        self.signUp.pack()

    def checkLog(self):
        db = db_scripts.datebase()
        bcheck = db.checkUser(self.textLogin.get(), self.textPassword.get())
        if bcheck and self.firstUser is True:
            print("Entered First")
            self.firstUser = True
            self.firstUserName = self.textLogin.get()
            self.root.destroy()
        if bcheck and self.secondUser is True:
            print("Entered Second")
            self.secondUser = True
            self.secondUserName = self.textLogin.get()
            self.root.destroy()
        db.printRegister()

    def checkReg(self):
        db = db_scripts.datebase()
        db.addUser(self.textLogin.get(), self.textPassword.get())
        db.printRegister()

    def getUser(self, posi):
        if posi == 1:
            return self.firstUser
        elif posi == 2:
            return self.secondUser

    def getUserName(self, posi):
        if posi == 1:
            return  self.firstUserName
        elif posi == 2:
            return self.secondUserName
