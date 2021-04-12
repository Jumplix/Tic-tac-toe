from tkinter import *


class ChildWindows:
    def __init__(self, parent, width, height, title="Войти"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)

        self.firstUser = False
        self.secondUser = False

        self.draw_widgets_child()
        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus()
        self.root.wait_window()

    def draw_widgets_child(self):
        self.labelLogin = Label(self.root, text='Логин')
        self.labelLogin.pack()
        self.textLogin = Entry(self.root, width=30)
        self.textLogin.pack()
        self.labelPassword = Label(self.root, text='Пароль')
        self.labelPassword.pack()
        self.textPassword = Entry(self.root, width=30, show="*")
        self.textPassword.pack()
        self.signIn = Button(self.root, text='Войти')
        self.signIn.pack()
        self.signUp = Button(self.root, text='Зарегестрироваться')
        self.signUp.pack()
