from multiprocessing import Process

from pvrecorder import PvRecorder

# from voice_recording.c3.cloud import upload_data
# from voice_recording.uttils import write_bytes
# from voice_recording.settings import Settings

from datetime import datetime
import json

import httpx

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

import re

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

                if re.search('бор', command):
                    print('Выполяю')


    finally:
        recorder.stop()
        recorder.delete()

    print("")
            # if all(element == 0 for element in frame):
            # else:
            #     frames.extend(frame)


            # absolute_path = config.local.tmp_path.get_secret_value() + datetime.now().strftime("%Y%m%d_%H%M%S.wav")
            # write_bytes(frame, absolute_path)

            # import httpx
            #
            # response = httpx.post(
            #     'http://127.0.0.1:8000/transcription',
            #     json={
            #         "array": frames
            #     }
            # )
            # print(response.content)

            # upload_data(
            #     config,
            #     absolute_path,
            #     frame,
            # )

    # except KeyboardInterrupt:
    #     recorder.stop()


    print(f'Res {text}')
    frames.clear()

if __name__ == '__main__':

    config = 1

    p = Process(target=listen, args=(config,))
    p.start()
    p.join()


