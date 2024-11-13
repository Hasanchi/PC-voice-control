from datetime import datetime

from typing import Literal
from spellchecker import SpellChecker

from .writer import LocalOperator, S3Operator
from ..settings import S3Settings, LocalSettings

spell = SpellChecker(language='ru')

def correct_command(command: str) -> str:
    return ' '.join([spell.correction(item) for item in command.split()])

def upload_data(config: LocalSettings | S3Settings, command: str):

    absolute_path = config.tmp_path.get_secret_value() + datetime.now().strftime("%Y%m%d_%H%M%S.txt")

    target_storage = LocalOperator if isinstance(config, LocalSettings) else S3Operator

    writer: LocalOperator | S3Operator = target_storage(config)

    correct = correct_command(command)

    storage_path = writer.write_bytes(absolute_path, correct.encode())

    return writer.read_bytes(storage_path).decode()

