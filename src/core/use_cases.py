import abc


class BaseUseCase(abc.ABC):

    @abc.abstractmethod
    def execute(self):
        pass


class NotifierUseCase(BaseUseCase):

    def __init__(self):
        pass

    def execute(self):
        pass
