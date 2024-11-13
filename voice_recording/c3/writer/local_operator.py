from voice_recording.c3.writer.base import Operator, log_decorator, BaseOverridesOperator
from voice_recording.settings import Settings, S3Settings, LocalSettings


class LocalOperator(Operator, BaseOverridesOperator):

    def __init__(self, settings: LocalSettings):
        super().__init__(settings)

    @log_decorator
    def write_bytes(self, file_name: str, data: bytes) -> str:
        with open(file_name, 'wb+') as file:
            file.write(data)

        return file_name

    @log_decorator
    def read_bytes(self, absolute_path: str) -> bytes:
        with open(absolute_path, 'rb') as file:
            return file.read()
