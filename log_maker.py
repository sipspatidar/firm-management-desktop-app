import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

handler = logging.FileHandler("error.log")
handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger1 = logging.getLogger(__name__)
logger1.setLevel(logging.INFO)

handler1 = logging.FileHandler("error.log")
handler1.setLevel(logging.INFO)

formatter1 = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler1.setFormatter(formatter1)

logger1.addHandler(handler1)

def insert_error(ex):
    template = "{0} {1}"
    message = template.format(type(ex).__name__,ex.args)
    logger.error(message)

def insert_info(ex):
    logger1.info(ex)
	
