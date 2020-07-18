
import os

from .input_reader import InputReader


class FileInputReader(InputReader):
    def __init__(self, path):
        self.path = path

    def read(self):
        if not os.path.exists(self.path):
            raise ValueError(f'Path not exist {self.path}')

        with open(self.path, 'r') as file:
            content = file.read()
            file.close()
            return content
