import logging
import re

def test_loggingDemo():

    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler('logfile.log')

    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s ")

    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)

    logger.setLevel(logging.INFO)
    logger.debug(" debug statemenet is -----")
    logger.info("information messages")
    logger.warning("wardingnikndingfi")
    logger.error("error messafe")
    logger.critical("set issue")

