import os
from tkinter import *

import db_scripts
from ChildWindow import ChildWindows
from GameWindow import GameWindow
from EndGameWindow import EndGameWindow

"""
    Для создания основного окна используется класс Window
    В основном модуле для работы выполнить следующую кнструкцию:
    window = Window()
"""

class Window:
    """
        Конструктор класса Window
    """
    def __init__(self, title="Крестики-нолики", width=600, height=400):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+200")
        self.root.resizable(width=False, height=False)
        self.firstUserName = ""
        self.secondUserName = ""
        db = db_scripts.datebase()
        self.rating = db.getAllRecord()

    """
        Метод для запуска объекта окна Window
    """

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    """
        Метод для отрисовки виджетов
    """

    def draw_widgets(self):
        btnPlay = Button(self.root, width=25, height=3, text="Играть с игроком", command=self.create_child_login)
        btnPlayBot = Button(self.root, width=25, height=3, text="Играть с ботом", command=self.create_logBot)
        btnUpdRat = Button(self.root, width=15, height=2, text="Обновить рейтинг", command=self.update_rating)
        listRatLogin = Listbox()
        listRatWin = Listbox()
        listRatLose = Listbox()
        listRatLogin.insert(END," Имя")
        listRatWin.insert(END, " Победы")
        listRatLose.insert(END, " Поражения")
        for res in self.rating:
            listRatLogin.insert(END, " " + res[0])
        for res in self.rating:
            listRatWin.insert(END, " " + str(res[1]))
        for res in self.rating:
            listRatLose.insert(END, " " + str(res[2]))
        btnPlay.place(relx=.17, rely=.1)
        btnPlayBot.place(relx=.52, rely=.1)
        btnUpdRat.place(relx=.4, rely=.3)
        listRatLogin.place(relx=.35, rely=.42, width=60, height=140)
        listRatWin.place(relx=.45, rely=.42, width=70, height=140)
        listRatLose.place(relx=.55, rely=.42, width=80, height=140)

    """
            Метод вызова дочерного окна для входа
    """

    def create_child_login(self):
        self.firstLog = ChildWindows(self.root, 500, 300, "Войти", 1)
        self.firstValue = self.firstLog.getUser(1)
        if self.firstValue is True:
            self.firstValue = False
            print("its worked")
            self.firstUserName = self.firstLog.getUserName(1)
            self.secondLog = ChildWindows(self.root, 500, 300, "Войти", 2)
            self.secondValue = self.secondLog.getUser(2)
            if self.secondValue is True:
                self.secondUserName = self.secondLog.getUserName(2)
                self.create_child_game("std")
            else:
                print("2 - its not worked")
        else:
            print("1 - its not worked")

    """
            Создание окна для регистрации игры с боту
    """

    def create_logBot(self):
        self.firstLog = ChildWindows(self.root, 500, 300, "Войти", 1)
        self.firstValue = self.firstLog.getUser(1)
        if self.firstValue is True:
            self.firstValue = False
            print("its worked")
            self.firstUserName = self.firstLog.getUserName(1)
            self.create_child_game("bot")
        else:
            print("1 - its not worked BOOOT")

    """
            Метод для обновления рейтинга
    """

    def update_rating(self):
        db = db_scripts.datebase()
        self.rating = db.getAllRecord()
        self.draw_widgets()

    """
            Метод для вызова окна с игрой
    """

    def create_child_game(self, type):
        print("first player - " + str(self.firstUserName))
        print("second player - " + str(self.secondUserName))
        print("Game started")
        if type == "std":
            self.Game = GameWindow(self.root, 700, 300, "Игра", self.firstUserName, self.secondUserName)
        elif type == "bot":
            self.Game = GameWindow(self.root, 700, 300, "Игра", self.firstUserName, "Bot")
