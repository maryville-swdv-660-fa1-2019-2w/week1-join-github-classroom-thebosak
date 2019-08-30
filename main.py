import colorlog
from datetime import *

def main():
    logger = colorlog.getLogger()
    logger.setLevel(colorlog.colorlog.logging.DEBUG)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    logger.info("Green info")
    logger.warning("Yellow warning")
    logger.error("Red error")
    logger.critical("Red critical")

    today = date.today()

    print('Todays date is ', today)

main()