import librosa 
import librosa.display 
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np 
FRAME_LENGTH = 1024
HOP_LENGTH = 512
music_file_1 = "MP3s/music_1.mp3"
file_1, _ = librosa.load(music_file_1)
def rms_1(signal, frame_length, hop_length):
    return np.array([np.sqrt(np.sum(signal[i:i+frame_length]**2)/frame_length) for i in range(0, len(signal), hop_length)])
print(rms_1(file_1, FRAME_LENGTH, HOP_LENGTH))