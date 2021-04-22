from tkinter import *

import db_scripts

"""
        Для создания дочернего окна используется класс ChildWindows
        Вызов окна осуществляется по кнопке в основном окне
"""

class GameWindow:
    """
            Конструктор класса GameWindows
            fUserName = f - first, s - second
    """
    def __init__(self, parent, width, height, title="Игра", fUserName="First player", sUserName="Second player"):
        self.root = Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+300")
        self.root.resizable(False, False)

        self.checkSymb = "X"
        self.revcheckSymb = "O"

        self.motionUser = 1 # 1 - left user, 2 - right user
        self.arrTextBut=["","","","","","","","","",""]

        self.gameEnd = False
        self.draw = False

        self.firUserName = fUserName
        self.secUserName = sUserName
        fres = self.getRecords(self.firUserName)
        self.fWinScore = fres[0]
        self.fLoseScore = fres[1]
        fres = self.getRecords(self.secUserName)
        self.sWinScore = fres[0]
        self.sLoseScore = fres[1]

        self.draw_widgets_child()
        self.grab_focus()

    """
            Метод отрисовки всех элементов
    """

    def draw_widgets_child(self):
        self.lblFirstUser = Label(self.root, text=str("1. " + self.firUserName + " " + self.checkSymb))
        self.lblSecondUser = Label(self.root, text=str("2. " + self.secUserName + " " + self.revcheckSymb))
        self.lblMotionIs = Label(self.root, text="Ход игрока " + str(self.motionUser))
        self.lblfUserWin = Label(self.root, text="Победы игрока - " + str(self.fWinScore))
        self.lblfUserLose = Label(self.root, text="Поражения игрока - " + str(self.fLoseScore))
        self.lblsUserWin = Label(self.root, text="Победы игрока - " + str(self.sWinScore))
        self.lblsUserLose = Label(self.root, text="Поражения игрока - " + str(self.sLoseScore))
        gameButton1 = Button(self.root, text=self.arrTextBut[0], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(0))
        gameButton2 = Button(self.root, text=self.arrTextBut[1], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(1))
        gameButton3 = Button(self.root, text=self.arrTextBut[2], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(2))
        gameButton4 = Button(self.root, text=self.arrTextBut[3], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(3))
        gameButton5 = Button(self.root, text=self.arrTextBut[4], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(4))
        gameButton6 = Button(self.root, text=self.arrTextBut[5], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(5))
        gameButton7 = Button(self.root, text=self.arrTextBut[6], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(6))
        gameButton8 = Button(self.root, text=self.arrTextBut[7], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(7))
        gameButton9 = Button(self.root, text=self.arrTextBut[8], bg="white", fg="red", bd=0, command=lambda: self.setSymbBoard(8))
        self.arrButtons = [[gameButton1, gameButton2, gameButton3],
                           [gameButton4, gameButton5, gameButton6],
                           [gameButton7, gameButton8, gameButton9]]
        self.lblFirstUser.place(relx=.05, rely=.1)
        self.lblfUserWin.place(relx=.05, rely=.16)
        self.lblfUserLose.place(relx=.05, rely=.23)

        self.lblSecondUser.place(relx=.75, rely=.1)
        self.lblsUserWin.place(relx=.75, rely=.16)
        self.lblsUserLose.place(relx=.75, rely=.23)

        self.lblMotionIs.place(relx=.4, rely=.1)

        for i in range(0,3):
            for j in range(0,3):
                self.arrButtons[i][j].place(relx=.35+(.1*j), rely=.2+(.2*i),
                                            height=50, width=50)

    """
            Метод определяющий фокус дочернего окна
    """

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus()
        self.root.wait_window()

    # def setSymbUser(self, posiUser, typeSymb):
    #     pass

    """
            Метод ставящий кнопкам крестик или нолик
    """
    def setSymbBoard(self, posi):
        if not self.gameEnd:
            if self.motionUser == 1 and self.arrTextBut[posi] == "":
                self.arrTextBut[posi] = self.checkSymb
                self.motionUser = 2
            elif self.motionUser == 2 and self.arrTextBut[posi] == "":
                self.arrTextBut[posi] = self.revcheckSymb
                self.motionUser = 1
            self.draw_widgets_child()
            self.checkWin()

    """
            Метод определяющий победу после каждого хода
    """

    def checkWin(self):
        if self.arrTextBut[0] == self.arrTextBut[1] == self.arrTextBut[2] and self.arrTextBut[0] != "":
            self.gameEnd = True
        if self.arrTextBut[3] == self.arrTextBut[4] == self.arrTextBut[5] and self.arrTextBut[3] != "":
            self.gameEnd = True
        if self.arrTextBut[6] == self.arrTextBut[7] == self.arrTextBut[8] and self.arrTextBut[6] != "":
            self.gameEnd = True
        if self.arrTextBut[0] == self.arrTextBut[3] == self.arrTextBut[6] and self.arrTextBut[0] != "":
            self.gameEnd = True
        if self.arrTextBut[1] == self.arrTextBut[4] == self.arrTextBut[7] and self.arrTextBut[1] != "":
            self.gameEnd = True
        if self.arrTextBut[2] == self.arrTextBut[5] == self.arrTextBut[8] and self.arrTextBut[2] != "":
            self.gameEnd = True
        if self.arrTextBut[0] == self.arrTextBut[4] == self.arrTextBut[8] and self.arrTextBut[0] != "":
            self.gameEnd = True
        if self.arrTextBut[2] == self.arrTextBut[4] == self.arrTextBut[6] and self.arrTextBut[2] != "":
            self.gameEnd = True
        j = 0
        for i in range(0,9):
            if self.arrTextBut[i] != "":
                j = j + 1
        if j == 9:
            self.draw = True
        if self.gameEnd and not self.draw:
            self.clearBoard()
        if self.draw:
            self.clearBoard()

    """
            Метод отчищающий поле и меняющий пользователя в начале игры
    """

    def clearBoard(self):
        for i in range(0,9):
            self.arrTextBut[i] = ""

        if not self.draw:
            if self.motionUser == 1:
                self.motionUser = 2
                self.sWinScore = self.sWinScore + 1 # писать анологию с бд
                self.setRecords(self.secUserName, 1)
                self.fLoseScore = self.fLoseScore + 1
                self.setRecords(self.firUserName, 0)
            else:
                self.motionUser = 1
                self.fWinScore = self.fWinScore + 1
                self.setRecords(self.firUserName, 1)
                self.sLoseScore = self.sLoseScore + 1
                self.setRecords(self.secUserName, 0)
        self.draw_widgets_child()
        self.gameEnd = False
        self.draw = False
        db = db_scripts.datebase()
        db.printRecords()

    """
            Метод записывающий результаты игры игроков
    """

    def setRecords(self, numUser, typeGame):
        db = db_scripts.datebase()
        db.setRecord(numUser, typeGame)

    """
            Метод для получения всех записей из бд рейтинга
    """

    def getRecords(self, login):
        db = db_scripts.datebase()
        res = db.getRecord(login)
        return res
