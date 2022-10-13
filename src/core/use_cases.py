import abc


class BaseUseCase(metaclass=abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class NotifierUseCase(BaseUseCase):

    def __init__(self, get_parameters):

        pass

    def execute(self):
        pass
