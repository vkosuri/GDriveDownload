import logging

def logging_cfg(filename):
    """ Create a FileHandler based logfile for logging """
    global logger

    file_path = os.path.join(os.getcwd(), filename)

    logging.basicConfig(datefmt='%H:%M:%S',
                        format='%(asctime)s.%(msecs)-03d  %(name)-12s \
                        %(levelname)-8s %(message)s',
                        filename=file_path, level=logging.NOTSET)

    logger = logging.getLogger(__name__)