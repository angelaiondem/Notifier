import abc


class BaseRepository(abc.ABC):

    @abc.abstractmethod
    def get_one(self, key: str) -> str:
        """
        By providing the key, the function gets and returns
        the value of the entity under the mentioned key.
        """
