'''
Brad Bosak
SWDV 660 Week 1 Assignment
08/29/2019
'''

#import packages
import colorlog
from datetime import *

def main():
    #logger setup
    logger = colorlog.getLogger()
    logger.setLevel(colorlog.colorlog.logging.DEBUG)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    #logger statements
    logger.info("Green info")
    logger.warning("Yellow warning")
    logger.error("Red error")
    logger.critical("Red critical")

    #date statement
    today = date.today()
    print('Todays date is ', today)

main()