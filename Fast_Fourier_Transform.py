import librosa 
import librosa.display 
import scipy as sp
import numpy as np 
music_file_1 = "MP3s/music_1.mp3"
file_1, sr = librosa.load(music_file_1)
ft = sp.fft.fft(file_1)
magnitude = np.absolute(ft)
frequency = np.linspace(0, sr, len(magnitude))
print(magnitude)
print(frequency)