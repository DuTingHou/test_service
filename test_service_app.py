from flask import Flask, make_response, jsonify, request
from utils.log_conf_parse import get_log_conf
from utils.logger_helper import logger_helper
from test_service import test_service

log_conf = get_log_conf("./conf/log.conf")
apploger = logger_helper(log_conf, "base_logger")
app = Flask(__name__)
app.config.from_pyfile("./conf/app_conf_prod.py",silent=True)
ts = test_service()


@app.route("/service/test_service", methods=['POST'])
def test_service():
    try:
        request_data = request.get_json()
    except Exception as exp:
        apploger.logger.info("request json error ! Exception:{} request_json:{}".format(exp, request))
        return make_response(jsonify({}), 400)
    if "inp" not in request_data:
        apploger.logger.info("inp not in request json")
        return make_response(jsonify({}), 400)

    result_str = ts.process(request_data["inp"])
    result_json = {"inp": request_data["inp"], "out": result_str}
    return make_response(jsonify(result_json), 200)


if __name__ != '__main__':
    # port = app.config.get("APP_PORT")
    apploger.logger.info("flask app is started!")

if __name__ == '__main__':
    port = app.config.get("APP_PORT")
    apploger.logger.info("flask app port {}".format(port))
    apploger.logger.info("flask app is starting!")
    app.run(threaded=True, host="0.0.0.0", port=port, debug=False)
