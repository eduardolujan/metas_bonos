from abc import ABCMeta, abstractmethod


class ParseInput(metaclass=ABCMeta):
    @abstractmethod
    def parse(self):
        raise NotImplementedError('Not implemented yet')

