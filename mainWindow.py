from tkinter import *

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
        Button(self.root, width=30, height=5, text="Играть").pack()
        Button(self.root, width=30, height=5, text="Рейтинг").pack()
