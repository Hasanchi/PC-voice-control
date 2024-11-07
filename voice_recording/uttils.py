import wave

import numpy as np


def write_bytes(frames: list[int], path):

    num_channels = 2  # Количество каналов (1 = моно; 2 = стерео)
    sample_width = 2  # Ширина выборки в байтах (2 = 16 бит)
    frame_rate = 44100  # Частота дискретизации в Гц
    num_frames = 0  # Количество кадров (можно оставить 0 до добавления данных)

    with (wave.open(path, 'wb') as wave_writer):
        wave_writer.setnchannels(num_channels)
        wave_writer.setsampwidth(sample_width)
        wave_writer.setframerate(frame_rate)
        wave_writer.setnframes(num_frames)

        frames = [bytes(item) for item in frames if item > 0]
        wave_writer.writeframes(b''.join(frames))
