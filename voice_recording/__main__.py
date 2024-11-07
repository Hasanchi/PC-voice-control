from multiprocessing import Process

from pvrecorder import PvRecorder

from voice_recording.c3.cloud import upload_data
from voice_recording.uttils import write_bytes
from voice_recording.settings import Settings

from datetime import datetime

def listen(config: Settings):
    recorder = PvRecorder(frame_length=20000)
    try:
        recorder.start()
        while recorder.is_recording:
            frame = recorder.read()

            absolute_path = config.local.tmp_path.get_secret_value() + datetime.now().strftime("%Y%m%d_%H%M%S.wav")
            bytes_frame = write_bytes(frame, absolute_path)
            upload_data(
                config,
                absolute_path,
            )

    except KeyboardInterrupt:
        recorder.stop()



if __name__ == '__main__':

    config = Settings()

    p = Process(target=listen, args=(config,))
    p.start()
    p.join()


