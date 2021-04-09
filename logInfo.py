import logging

log = logging.getLogger("Tic-tac-toe")
log.setLevel(logging.INFO)
fPath = logging.FileHandler("log/server.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fPath.setFormatter(formatter)
log.addHandler(fPath)
