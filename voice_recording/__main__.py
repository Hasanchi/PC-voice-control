
from multiprocessing import Process
from pvrecorder import PvRecorder

async def listen():
    recorder = PvRecorder(device_index=-1, frame_length=512)
    try:
        while True:
            recorder.start()
    except KeyboardInterrupt:
        recorder.stop()



if __name__ == '__main__':
    l = Process(target=listen).start()

