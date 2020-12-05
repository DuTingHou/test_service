from utils.logger_helper import logger_helper
from utils.log_conf_parse import get_log_conf
import time
from tqdm import tqdm


log_conf = get_log_conf("./conf/log.conf","base_logger")
myloger = logger_helper(log_conf)

def test():
    for i in tqdm(range(0, 2000)):
        myloger.logger.info("test base logger {}".format(i))
        time.sleep(0.05)


if __name__ == '__main__':
    test()
