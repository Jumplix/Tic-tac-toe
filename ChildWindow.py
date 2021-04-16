from tkinter import *

"""
    Для создания дочернего окна используется класс ChildWindows
    Вызов окна осуществляется по кнопке в основном окне
"""


class ChildWindows:
    """
            Конструктор класса ChildWindows
    """
    def __init__(self, parent, width, height, title="Войти"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)

        """
            TODO:Сделать класс, который будет получать инофрмацию об активных пользователях
        """
        self.firstUser = False
        self.secondUser = False

        self.labelLogin = Label(self.root, text='Логин')
        self.textLogin = Entry(self.root, width=30)
        self.labelPassword = Label(self.root, text='Пароль')
        self.textPassword = Entry(self.root, width=30, show="*")
        self.signIn = Button(self.root, text='Войти')
        self.signUp = Button(self.root, text='Зарегестрироваться')

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

        if self.firstUser is False:
            self.labelLogin = Label(self.root, text='Игрок 1')
        elif self.secondUser is False:
            self.labelLogin = Label(self.root, text='Игрок 2')

        self.labelLogin.pack()
        self.textLogin.pack()
        self.labelPassword.pack()
        self.textPassword.pack()
        self.signIn.pack()
        self.signUp.pack()
