import logging, logging.handlers

basic_format = "[%(asctime)s-%(levelname)s-%(name)s-%(filename)s-%(lineno)d] %(message)s"
formater = logging.Formatter(basic_format)


class logger_helper(object):
    def __init__(self, conf):
        self.logger = logging.getLogger(conf["name"])
        self.logger.setLevel(logging.INFO)
        log_handler = logging.handlers.TimedRotatingFileHandler(
            filename=conf["outfile"], interval=conf["interval"]
            , when=conf["when"], backupCount=conf["backupcount"])
        log_handler.setFormatter(formater)
        self.logger.addHandler(log_handler)
