# Custom defined exceptions

class InvalidEventTypeException(Exception):
    """Thrown when event type in not defined or defined wrong."""


class EmailIsNotSentException(Exception):
    """Throw when email sending process catches an exception."""


class SlackMessageIsNotSentException(Exception):
    """Throw when slack message sending process catches an exception."""


class MessageBodyIsInvalidException(Exception):
    """Throw when body is not string or is empty string."""


class SerializationFailedException(Exception):
    """Throw when serialization is failed."""


class DeserializationFailedException(Exception):
    """Throw when deserialization is failed."""
