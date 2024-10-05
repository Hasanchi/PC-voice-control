import io
from wave import Wave_write
import wave

def write_bytes(frame):
    bytes_object = io.BytesIO()
    num_channels = 2  # Количество каналов (1 = моно; 2 = стерео)
    sample_width = 2  # Ширина выборки в байтах (2 = 16 бит)
    frame_rate = 44100  # Частота дискретизации в Гц
    num_frames = 0  # Количество кадров (можно оставить 0 до добавления данных)

    # Создаем объект wave
    with wave.open(bytes_object, 'wb') as wave_writer:
        # Устанавливаем параметры формата
        wave_writer.setnchannels(num_channels)
        wave_writer.setsampwidth(sample_width)
        wave_writer.setframerate(frame_rate)
        wave_writer.setnframes(num_frames)

        # Если вам нужны данные для записи, вы можете сгенерировать их или прочитать из другого источника:
        # Пример: создаем синусоиду
        import numpy as np

        duration = 1  # длительность в секундах
        t = np.linspace(0, duration, int(frame_rate * duration), endpoint=False)
        frequency = 440  # частота в Гц (ла)
        audio_data = 0.5 * np.sin(2 * np.pi * frequency * t)
        audio_data = (audio_data * 32767).astype(np.int16)  # Преобразуем в целые числа
        wave_writer.writeframes(audio_data.tobytes())
    return bytes_object.read()