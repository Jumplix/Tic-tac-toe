import logging

"""
    Для логирование всех действий пользователя используем библиотеку logging и класс Logger.
    В основном модуле для работы выполнить следующую кнструкцию:
    log = logger().runLog()
    
    Для записи лога использовать конструкцию:
    log.info(<Сообщение>)
"""


class Logger:
    """
        Конструктор класса Logger
    """
    def __init__(self):
        self.log = logging.getLogger("Tic-tac-toe")
        self.log.setLevel(logging.INFO)
        fPath = logging.FileHandler("log/server.log")
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fPath.setFormatter(formatter)
        self.log.addHandler(fPath)

    """
        Метод получения лога
    """
    def runLog(self):
        return self.log
