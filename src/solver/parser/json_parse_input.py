
import json
from .parse_input import ParseInput


class JsonParseInput(ParseInput):
    def __init__(self, input_reader):
        self.input_reader = input_reader

    def parse(self):
        content = self.input_reader.read()
        return json.loads(content)
