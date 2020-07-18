from abc import ABCMeta, abstractmethod


class InputReader(metaclass=ABCMeta):
    @abstractmethod
    def read(self):
        raise NotImplementedError('Not implemented yet')