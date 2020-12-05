from conf.project_conf import LOG_DIR, APP_PORT, PID_FILE
import os

pidfile = PID_FILE
bind = "0.0.0.0:{}".format(APP_PORT)
works = 1
threads = 1
backlog = 512
timeout = 500

loglevel = "info"
accesslog = os.path.join(LOG_DIR, "access.log")
errorlog = os.path.join(LOG_DIR, "error.log")