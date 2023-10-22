import librosa
import librosa.display
import numpy as np
import math 
music_file_1 = "MP3s/music_1.mp3"
music, sr = librosa.load(music_file_1)
FRAME_SIZE = 2048
HOP_LENGTH = 512
spec = librosa.stft(music, n_fft=FRAME_SIZE,hop_length=HOP_LENGTH)
def calculate_split_frequency_bin(spectrogram, split_frequency, sample_rate):
    frequency_range = sample_rate / 2
    frequency_delta_per_bin = frequency_range / spectrogram.shape[0]
    split_frequency_bin = np.floor(split_frequency / frequency_delta_per_bin)
    return int(split_frequency_bin) # returns the number of the bin, not the value, which is inputted
def calculate_band_energy_ratio(spectrogram, split_frequency, sample_rate):
    split_frequency_bin = calculate_split_frequency_bin(spectrogram, split_frequency, sample_rate)
    power_spec = np.abs(spectrogram) ** 2
    power_spec = power_spec.T
    band_energy_ratio = []
    for frequencies_in_frame in power_spec:
        sum_power_low_frequencies = np.sum(frequencies_in_frame[:split_frequency_bin])
        sum_power_high_frequencies = np.sum(frequencies_in_frame[split_frequency_bin:])
        ber_current_frame = sum_power_low_frequencies / sum_power_high_frequencies
        band_energy_ratio.append(ber_current_frame)
    return np.array(band_energy_ratio)
print(calculate_band_energy_ratio(spec, 2000, sr))