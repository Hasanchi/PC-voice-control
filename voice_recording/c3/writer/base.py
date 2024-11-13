from abc import ABC, abstractmethod

from loguru import logger

from voice_recording.settings import LocalSettings, S3Settings



def log_decorator(func):

    def wrapped(*args, **kwargs):
        logger.info(f"Method {func.__name__} called with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"Method {func.__name__} returned: {result}")
        return result

    return wrapped


class BaseOverridesOperator(ABC):

    @log_decorator
    @abstractmethod
    def write_bytes(self, file_name: str, data: bytes) -> str:
        raise NotImplementedError

    @log_decorator
    @abstractmethod
    def read_bytes(self, absolute_path: str) -> bytes:
        raise NotImplementedError


class Operator:
    def __init__(self, settings: LocalSettings | S3Settings):
        for key, item in settings.model_dump().items():
            setattr(self, key, item.get_secret_value())

