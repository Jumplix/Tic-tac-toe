from tkinter import *

import db_scripts
from PIL import ImageTk, Image

"""
    Для создания дочернего окна используется класс ChildWindows
    Вызов окна осуществляется по кнопке в основном окне
"""


class EndGameWindow:
    """
            Конструктор класса ChildWindows
    """
    def __init__(self, parent, width, height, title="Итог", plnumb=0, firUserName="First user", secUserName="Second user"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)
        self.res = 3
        self.msgtext = ""
        self.usnumb = plnumb
        self.fUserName = firUserName
        self.sUserName = secUserName
        self.draw_widgets_child()
        self.grab_focus()
        self.textdraw = " "

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
        if self.usnumb == 1 or self.usnumb == 2:
            self.labelWinner = Label(self.root, text='Победитель')
            self.labelLoser = Label(self.root, text='Проигравший')
            self.labelTextDraw = Label(self.root, text='')
            if self.usnumb == 1:
                self.labelWinnerName = Label(self.root, text=self.fUserName)
                self.labelLoserName = Label(self.root, text=self.sUserName)
            if self.usnumb == 2:
                self.labelWinnerName = Label(self.root, text=self.sUserName)
                self.labelLoserName = Label(self.root, text=self.fUserName)
        if self.usnumb == 3:
            self.labelWinner = Label(self.root, text='')
            self.labelLoser = Label(self.root, text='')
            self.labelWinnerName = Label(self.root, text='')
            self.labelLoserName = Label(self.root, text='')
            self.textdraw = "Ничья"
            self.labelTextDraw = Label(self.root, text=self.textdraw)

        self.labelWinner.place(relx=.35, rely=.1)
        self.labelWinnerName.place(relx=.35, rely=.2)
        self.labelTextDraw.place(relx=.25, rely=.25)
        self.labelLoser.place(relx=.35, rely=.3)
        self.labelLoserName.place(relx=.35, rely=.4)

