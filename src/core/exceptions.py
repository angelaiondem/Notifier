# Custom defined exceptions

class InvalidEventTypeException(Exception):
    """Thrown when event type in not defined or defined wrong."""


class EmailIsNotSentException(Exception):
    """Throw when email sending process catches an exception."""


class SlackMessageIsNotSentException(Exception):
    """Throw when email sending process catches an exception."""


class SlackBodyKeysAreInvalidException(Exception):
    """Throw when slack body keys don't are wrong."""


class SerializationFailedException(Exception):
    """Throw when serialization is failed."""


class DeserializationFailedException(Exception):
    """Throw when deserialization is failed."""
