'''
Brad Bosak
SWDV 660 Week 1 Assignment
08/29/2019
'''

#import packages
import colorlog
from datetime import *

#logger setup
logger = colorlog.getLogger()
logger.setLevel(colorlog.colorlog.logging.DEBUG)
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter())
logger.addHandler(handler)

#logger statements
logger.info("Green color for info message")
logger.warning("Yellow color for warning message")
logger.error("Red color for error message")
logger.critical("Also red color for critical message")

#date statement
today = date.today()
print("Today's date is ", today)

input('Thank you for running my program!  Press ENTER to continue')