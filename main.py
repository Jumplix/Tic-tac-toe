from logInfo import Logger
from mainWindow import Window

log = Logger().runLog()
log.info("Программа запущена")

window = Window()
log.info("Создано основное окно программы")

window.run()
log.info("Запущено основное окно программы")
