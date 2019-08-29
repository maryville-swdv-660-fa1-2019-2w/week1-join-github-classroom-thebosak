import colorlog

def main():
    logger = colorlog.getLogger()
    logger.setLevel(colorlog.colorlog.logging.DEBUG)
    handler = colorlog.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter())
    logger.addHandler(handler)

    logger.info("Info message in green")
    logger.warning("Warning message in yellow")
    logger.error("Error message in red")
    logger.critical("Critical message also in red")


main()