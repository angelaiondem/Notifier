import abc


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def get_one(self):
        pass
