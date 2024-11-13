from datetime import datetime
import re
import json
from multiprocessing import Process

import httpx
from pvrecorder import PvRecorder

from .c3.cloud import upload_data
from .settings import Settings


SAMPLE_RATE = 16000
DURATION = 5 # Длительность записи в секундах


def request(frames: list[int]):
    response = httpx.post(
        'http://127.0.0.1:8000/transcription',
        json={
            "array": frames
        }
    )

    try:
        response.raise_for_status()
    except httpx.HTTPError as e:
        print(e)

    return json.loads(response.content)


def listen(config):

    recorder = PvRecorder(frame_length=512)

    frames = []
    recorder.start()
    print('Start')

    try:
        while True:
            frame = recorder.read()
            frames.extend(frame)

            if len(frames) > 80000:
                print('Start transcribations')
                response = request(frames)
                frames.clear()

                command: str = response['text']

                if re.search('бор', command) or True:
                    print('Выполяю')
                    storage_command = upload_data(config, command)

    finally:
        recorder.stop()
        recorder.delete()



if __name__ == '__main__':

    config = Settings()


    listen(config.local)
    # p = Process(target=listen, args=(config.local,))
    # p.start()
    # p.join()


