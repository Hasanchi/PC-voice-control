from loguru import logger
from boto3 import Session

from voice_recording.c3.writer.base import Operator
from voice_recording.settings import Settings, S3Settings, LocalSettings
from voice_recording.c3.writer.base import BaseOverridesOperator
from io import BytesIO

import numpy as np
from moviepy.audio.AudioClip import AudioArrayClip

class LocalOperator(Operator, BaseOverridesOperator):

    def __init__(self, settings: LocalSettings):
        super().__init__(settings)

    def write_bytes(self, file_name: str, wav: list[int]) -> str:
        audio_array = np.array(wav, dtype=np.int16)

        # Нормализация аудиоданных в диапазон [-1, 1]
        audio_array = audio_array / np.max(np.abs(audio_array))

        # Создание AudioArrayClip
        audio_clip = AudioArrayClip(audio_array.reshape(-1, 1), fps=44100)

        # Сохранение в MP3
        audio_clip.write_audiofile(file_name, codec='libmp3lame')

        return file_name

    def read_bytes(self, absolute_path: str) -> bytes:

        buffer = BytesIO()

        with open(absolute_path, 'rb') as read_file:
            buffer.write(read_file.read())

        return buffer.getvalue()
