from datetime import datetime

from voice_recording.c3.writer import LocalOperator

from voice_recording.settings import Settings


def upload_data(config: Settings, absolute_path, wav):

    file_name = datetime.now().strftime("%Y%m%d_%H%M%S.mp3")

    writer: LocalOperator = LocalOperator(config.local)

    writer.write_bytes(absolute_path, wav)
