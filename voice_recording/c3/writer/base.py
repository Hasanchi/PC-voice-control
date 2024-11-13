from abc import ABC, abstractmethod

from voice_recording.settings import LocalSettings, S3Settings

class BaseOverridesOperator(ABC):

    @abstractmethod
    def write_bytes(self, file_name: str, wav: list[int]) -> str:
        raise NotImplementedError

    @abstractmethod
    def read_bytes(self, absolute_path: str) -> bytes:
        raise NotImplementedError


class Operator:
    def __init__(self, settings: LocalSettings | S3Settings):
        for key, item in settings.model_dump().items():
            setattr(self, key, item.get_secret_value())

