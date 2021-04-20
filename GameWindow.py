from tkinter import *

import db_scripts

"""
    Для создания дочернего окна используется класс ChildWindows
    Вызов окна осуществляется по кнопке в основном окне
"""


class GameWindow:
    """
            Конструктор класса ChildWindows
            fUserName = f - first, s - second
    """
    def __init__(self, parent, width, height, title="Игра", fUserName="First player", sUserName="Second player"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)

        """
            TODO:Сделать класс, который будет содержать игровое поле, игроков и аватарки
        """

        self.labelLogin = Label(self.root, text=str(fUserName))
        # self.textLogin = Entry(self.root, width=30)
        self.labelPassword = Label(self.root, text=str(sUserName))
        # self.textPassword = Entry(self.root, width=30, show="*")
        # self.signIn = Button(self.root, text='Войти', command)
        # self.signUp = Button(self.root, text='Зарегистрироваться', command=self.checkReg)
        self.draw_widgets_child()



    def draw_widgets_child(self):

        # if self.firstUser is True:
        #     self.labelLogin = Label(self.root, text='Игрок 1')
        # elif self.secondUser is True:
        #     self.labelLogin = Label(self.root, text='Игрок 2')

        self.labelLogin.pack()
        # self.textLogin.pack()
        self.labelPassword.pack()
        # self.textPassword.pack()
