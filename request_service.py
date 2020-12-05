import os, sys
import requests
import json


def request_test_service(url):
    par = {}
    head = {"Content-Type": "application/json", "charset": "UTF-8"}
    par["inp"] = "hello"
    r = requests.post(url, data=json.dumps(par).encode("utf-8"), headers=head)
    return r.text

result = request_test_service("http://0.0.0.0:7500/service/test_service")
print(result)