import librosa 
import librosa.display 
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np 
music_file_1 = "MP3s/music_1.mp3"
FRAME_SIZE = 1024
HOP_LENGTH = 512
file_1, sr = librosa.load(music_file_1)
def ae(signal, frame_size, hop_length):
    return np.array([max(signal[i:i+frame_size]) for i in range(0, signal.size, hop_length)]) 
print(ae(file_1, FRAME_SIZE, HOP_LENGTH))