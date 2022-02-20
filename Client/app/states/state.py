from abc import ABCMeta, abstractmethod

class State(metaclass=ABCMeta):
    STATE = 'state'

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_data(self):
        pass