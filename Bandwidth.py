import numpy as np  
import librosa
import librosa.display
music_file_1 = "MP3s/music_1.mp3"
music, sr = librosa.load(music_file_1)
FRAME_SIZE = 1024
HOP_LENGTH = 512
ban = librosa.feature.spectral_bandwidth(y=music, sr=sr, n_fft=FRAME_SIZE, hop_length=HOP_LENGTH)