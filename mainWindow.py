from tkinter import *
from ChildWindow import ChildWindows

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
        btn2 = Button(self.root, width=30, height=5, text="Рейтинг")
        btn1.pack()
        btn2.pack()

    """
            Метод вызова дочерного окна для входа
    """
    def create_child_login(self):
        ChildWindows(self.root, 300, 200, "Войти")
