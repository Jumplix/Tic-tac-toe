from tkinter import *
from ChildWindow import ChildWindows
from GameWindow import GameWindow

"""
    Для создания основного окна используется класс Window
    В основном модуле для работы выполнить следующую кнструкцию:
    window = Window()
"""


class Window:
    """
        Конструктор класса Window
    """
    def __init__(self, title="Крестики-нолики", width=700, height=400):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+400+200")
        self.root.resizable(width=False, height=False)

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
        btn1 = Button(self.root, width=30, height=5, text="Играть", command=self.create_child_login)
        btn2 = Button(self.root, width=30, height=5, text="Рейтинг", command=self.create_child_rat)
        btn1.pack()
        btn2.pack()

    """
            Метод вызова дочерного окна для входа
    """
    def create_child_login(self):
        self.firstLog = ChildWindows(self.root, 300, 200, "Войти", 1)
        self.firstValue = self.firstLog.getUser(1)
        if self.firstValue is True:
            self.firstValue = False
            print("its worked")
            self.firstUserName = self.firstLog.getUserName(1)
            self.secondLog = ChildWindows(self.root, 300, 200, "Войти", 2)
            self.secondValue = self.secondLog.getUser(2)
            if self.secondValue is True:
                self.secondUserName = self.secondLog.getUserName(2)
                self.create_child_game()
            else:
                print("2 - its not worked")
        else:
            print("1 - its not worked")

    def create_child_rat(self):
        print("Rating started")

    def create_child_game(self):
        print("first player - " + str(self.firstUserName))
        print("second player - " + str(self.secondUserName))
        self.Game = GameWindow(self.root, 300, 200, "Игра", self.firstUserName, self.secondUserName)
        print("Game started")