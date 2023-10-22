import librosa 
import librosa.display 
import numpy as np 
music_path = "MP3s/music_1.mp3"
music, sr = librosa.load(music_path)
def magnitude_spectrum(signal): 
    ft = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)
    return magnitude_spectrum
print(magnitude_spectrum(music))