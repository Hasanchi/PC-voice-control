from datetime import datetime

from typing import Literal

from .writer import LocalOperator, S3Operator

from ..settings import S3Settings, LocalSettings


def upload_data(config: LocalSettings | S3Settings, command: str):

    absolute_path = config.tmp_path.get_secret_value() + datetime.now().strftime("%Y%m%d_%H%M%S.txt")

    target_storage = LocalOperator if isinstance(config, LocalSettings) else S3Operator

    writer: LocalOperator | S3Operator = target_storage(config)

    bytes_command = command.encode()

    storage_path = writer.write_bytes(absolute_path, bytes_command)

    return writer.read_bytes(storage_path).decode()

