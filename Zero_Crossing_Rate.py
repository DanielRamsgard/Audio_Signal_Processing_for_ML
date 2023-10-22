import librosa 
import librosa.display 
import IPython.display as ipd
import matplotlib.pyplot as plt
import numpy as np 
music_file_1 = "MP3s/music_1.mp3"
file_1, _ = librosa.load(music_file_1)
FRAME_LENGTH = 1024
HOP_LENGTH = 512
zcr_file_1 = librosa.feature.zero_crossing_rate(y=file_1, frame_length=FRAME_LENGTH, hop_length=HOP_LENGTH) # multiply by FRAME_LENGTH to get actual, non-normalized values of zcr
print(zcr_file_1)
print(zcr_file_1*FRAME_LENGTH) 