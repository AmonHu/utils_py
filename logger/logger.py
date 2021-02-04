import logging


def __log_config__():
    logger = logging.getLogger()
    logger.setLevel('DEBUG')
    basic_format = "%(asctime)s:%(filename)s[line:%(lineno)d]:%(levelname)s:%(message)s"
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(basic_format, date_format)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel('INFO')
    file_handler = logging.FileHandler(f'./log.txt')
    file_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


__log_config__()


# logging.basicConfig(
#     filename=f'{LOG_PATH}/log.txt',
#     level=logging.INFO,
#     format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s'
# )


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def debug(message):
    logging.debug(message)


def error(message):
    logging.error(message)


def fatal(message):
    logging.fatal(message)
