from tkinter import *

import db_scripts
import random

from EndGameWindow import EndGameWindow

"""
        DO: window with text about win o lose anf pause betwen different game and pause between bot and player step
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
        self.startpos = 1
        self.motionUser = 1 # 1 - left user, 2 - right user
        self.arrTextBut=["","","","","","","","","",""]
        self.life = False

        self.gameEnd = False
        self.draw = False

        self.firUserName = fUserName
        self.secUserName = sUserName
        fres = self.getRecords(self.firUserName)
        self.fWinScore = fres[0]
        self.fLoseScore = fres[1]
        if self.secUserName != "Bot":
            fres = self.getRecords(self.secUserName)
            self.sWinScore = fres[0]
            self.sLoseScore = fres[1]
        if self.secUserName == "Bot":
            self.sWinScore = 0
            self.sLoseScore = 0
        self.draw_widgets_child()
        self.grab_focus()

    """
            Метод отрисовки всех элементов
    """

    def draw_widgets_child(self):
        self.lblFirstUser = Label(self.root, text=str("1. " + self.firUserName + " " + self.checkSymb))
        self.lblSecondUser = Label(self.root, text=str("2. " + self.secUserName + " " + self.revcheckSymb))
        self.lblMotionIs = Label(self.root, text="Ход игрока " + str(self.motionUser))
        self.lblfUserWin = Label(self.root, text="Победы - " + str(self.fWinScore))
        self.lblfUserLose = Label(self.root, text="Поражения - " + str(self.fLoseScore))
        self.lblsUserWin = Label(self.root, text="Победы - " + str(self.sWinScore))
        self.lblsUserLose = Label(self.root, text="Поражения - " + str(self.sLoseScore))

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

    """
            Метод ставящий кнопкам крестик или нолик
    """

    def setSymbBoard(self, posi):
        if not self.gameEnd:
            if self.motionUser == 1 and self.arrTextBut[posi] == "":
                self.arrTextBut[posi] = self.checkSymb
                self.motionUser = 2
                if self.secUserName == "Bot":
                    self.checkWin()
            elif self.motionUser == 2 and self.arrTextBut[posi] == "" and self.secUserName != "Bot":
                self.arrTextBut[posi] = self.revcheckSymb
                self.motionUser = 1
            if self.motionUser == 2 and self.secUserName == "Bot" and not self.draw:
                self.botRecFind()
                self.motionUser = 1
            self.draw_widgets_child()
            self.checkWin()

    """
            Метод определяющий победу после каждого хода
    """

    def checkWin(self):
        winner = ""
        if self.arrTextBut[0] == self.arrTextBut[1] == self.arrTextBut[2] and self.arrTextBut[0] != "":
            self.gameEnd = True
            winner = self.arrTextBut[0]
        if self.arrTextBut[3] == self.arrTextBut[4] == self.arrTextBut[5] and self.arrTextBut[3] != "":
            self.gameEnd = True
            winner = self.arrTextBut[3]
        if self.arrTextBut[6] == self.arrTextBut[7] == self.arrTextBut[8] and self.arrTextBut[6] != "":
            self.gameEnd = True
            winner = self.arrTextBut[6]
        if self.arrTextBut[0] == self.arrTextBut[3] == self.arrTextBut[6] and self.arrTextBut[0] != "":
            self.gameEnd = True
            winner = self.arrTextBut[0]
        if self.arrTextBut[1] == self.arrTextBut[4] == self.arrTextBut[7] and self.arrTextBut[1] != "":
            self.gameEnd = True
            winner = self.arrTextBut[1]
        if self.arrTextBut[2] == self.arrTextBut[5] == self.arrTextBut[8] and self.arrTextBut[2] != "":
            self.gameEnd = True
            winner = self.arrTextBut[2]
        if self.arrTextBut[0] == self.arrTextBut[4] == self.arrTextBut[8] and self.arrTextBut[0] != "":
            self.gameEnd = True
            winner = self.arrTextBut[0]
        if self.arrTextBut[2] == self.arrTextBut[4] == self.arrTextBut[6] and self.arrTextBut[2] != "":
            self.gameEnd = True
            winner = self.arrTextBut[2]
        j = 0
        for i in range(0,9):
            if self.arrTextBut[i] != "":
                j = j + 1
        if j == 9:
            self.draw = True
            self.gameEnd = True
        if self.gameEnd:
            self.clearBoard()
            if not self.draw:
                self.setWinner(winner)
                self.endGame()
            if self.draw:
                self.final = EndGameWindow(self.root, 200, 150, "Итог", 3, self.firUserName, self.secUserName)
                self.endGame()

    """
            Метод отчищения поля
    """

    def clearBoard(self):
        for i in range(0,9):
            self.arrTextBut[i] = ""
        self.draw_widgets_child()

    """
            Метод записи победителя в бд
    """

    def setWinner(self, whom):
        if whom == "X":
            self.fWinScore = self.fWinScore + 1
            self.setRecords(self.firUserName, 1)
            self.sLoseScore = self.sLoseScore + 1
            if self.secUserName != "Bot":
                self.setRecords(self.secUserName, 0)
            self.final = EndGameWindow(self.root, 200, 150, "Итог", 1, self.firUserName, self.secUserName)
        if whom == "O":
            self.sWinScore = self.sWinScore + 1
            if self.secUserName != "Bot":
                self.setRecords(self.secUserName, 1)
            self.fLoseScore = self.fLoseScore + 1
            self.setRecords(self.firUserName, 0)
            self.final = EndGameWindow(self.root, 200, 150, "Итог", 2, self.firUserName, self.secUserName)
        self.draw_widgets_child()

    """
            Метод перестановки значений начального игрока при конце игры
    """

    def endGame(self):

        if self.startpos == 1:
            self.startpos = 2
            self.motionUser = 2
        elif self.startpos == 2:
            self.startpos = 1
            self.motionUser = 1

        self.draw_widgets_child()
        self.gameEnd = False
        self.draw = False
        db = db_scripts.datebase()
        db.printRecords()

        if self.startpos == 2 and self.secUserName == "Bot" and self.checkBoardEmpty():
            self.botRecFind()
            self.motionUser = 1
            self.draw_widgets_child()

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

    """
            Метод бота для выборки всех позиций 
    """

    def botRecFind(self):
        # Проверка горизонтальных линий
        for i in range(0, 2):
            if self.botFindMove(self.arrTextBut[0], 0, self.arrTextBut[1], 1, self.arrTextBut[2], 2, self.checkSymb, self.revcheckSymb, i):
                return
            if self.botFindMove(self.arrTextBut[3], 3, self.arrTextBut[4], 4, self.arrTextBut[5], 5, self.checkSymb, self.revcheckSymb, i):
                return
            if self.botFindMove(self.arrTextBut[6], 6, self.arrTextBut[7], 7, self.arrTextBut[8], 8, self.checkSymb, self.revcheckSymb, i):
                return
            # Проверка вертикальных линий
            if self.botFindMove(self.arrTextBut[0], 0, self.arrTextBut[3], 3, self.arrTextBut[6], 6, self.checkSymb, self.revcheckSymb, i):
                return
            if self.botFindMove(self.arrTextBut[1], 1, self.arrTextBut[4], 4, self.arrTextBut[7], 7, self.checkSymb, self.revcheckSymb, i):
                return
            if self.botFindMove(self.arrTextBut[2], 2, self.arrTextBut[5], 5, self.arrTextBut[8], 8, self.checkSymb, self.revcheckSymb, i):
                return
            # Проверка диагональных линий
            if self.botFindMove(self.arrTextBut[0], 0, self.arrTextBut[4], 4, self.arrTextBut[8], 8, self.checkSymb, self.revcheckSymb, i):
                return
            if self.botFindMove(self.arrTextBut[2], 2, self.arrTextBut[4], 4, self.arrTextBut[6], 6, self.checkSymb, self.revcheckSymb, i):
                return

        while True:
            row = int(random.randint(0, 8))
            if self.arrTextBut[row] == "":
                self.arrTextBut[row] = self.revcheckSymb
                break

    """
            Метод бота для проверки выбранных позиций
    """

    def botFindMove(self, a1, pos1, a2, pos2, a3, pos3, symbop, symbmy, type):
        res = False
        if type == 0:
            if a1 == symbmy and a2 == symbmy and a3 == '':
                self.arrTextBut[pos3] = self.revcheckSymb
                res = True
            if a1 == symbmy and a2 == '' and a3 == symbmy:
                self.arrTextBut[pos2] = self.revcheckSymb
                res = True
            if a1 == '' and a2 == symbmy and a3 == symbmy:
                self.arrTextBut[pos1] = self.revcheckSymb
                res = True
        if type == 1:
            if a1 == symbop and a2 == symbop and a3 == '':
                self.arrTextBut[pos3] = self.revcheckSymb
                res = True
            if a1 == symbop and a2 == '' and a3 == symbop:
                self.arrTextBut[pos2] = self.revcheckSymb
                res = True
            if a1 == '' and a2 == symbop and a3 == symbop:
                self.arrTextBut[pos1] = self.revcheckSymb
                res = True

        return res

    """
            Метод для определения пусто ли игровое поле
    """

    def checkBoardEmpty(self):
        j = 0
        for i in range(0,9):
            if self.arrTextBut[i] == "":
                j = j + 1
        if j == 9:
            return 1
        else:
            return 0




