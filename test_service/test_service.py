from test_service.preprocess import get_text


class test_service(object):
    def __init__(self):
        self.mode = "test"

    def process(self, inp):
        text = get_text(inp)
        return text
