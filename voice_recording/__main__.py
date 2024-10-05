from multiprocessing import Process

from pvrecorder import PvRecorder

from voice_recording.c3.cloud import upload_data
from voice_recording.uttils import write_bytes
from voice_recording.settings import Settings


def listen(config: Settings):
    recorder = PvRecorder(device_index=-1, frame_length=512)
    try:
        recorder.start()
        while True:
            frame = recorder.read()
            upload_data(
                config,
                write_bytes(frame),
            )



    except KeyboardInterrupt:
        recorder.stop()



if __name__ == '__main__':

    config = Settings()

    p = Process(target=listen, args=(config,))
    p.start()
    p.join()


