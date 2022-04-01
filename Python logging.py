import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="logger.log",  filemode='w', encoding="utf-8", level=logging.INFO,
                    format='%(asctime)s %(message)s')

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

fh = logging.FileHandler(filename="logger.log", encoding="utf-8")
fh.setLevel(logging.INFO)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

def my_func():
    logger.info("Something happend")
    logger.warning("%s started! Watch out!", __name__)

my_func()



