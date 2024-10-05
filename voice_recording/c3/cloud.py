from voice_recording.c3.writer import Writer

from voice_recording.settings import Settings


def upload_data(config: Settings, frame: bytes):

    with Writer(config) as writer:
        writer.write_frame(frame)
