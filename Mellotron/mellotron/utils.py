import numpy as np
from scipy.io.wavfile import read
import torch
import soundfile as sf


def get_mask_from_lengths(lengths):
    max_len = torch.max(lengths).item()
    ids = torch.arange(0, max_len, out=torch.cuda.LongTensor(max_len))
    mask = (ids < lengths.unsqueeze(1)).bool()
    return mask

def load_wav_to_torch(full_path, final_sr=22050):
        audio, sampling_rate = sf.read(full_path, dtype='int16')
    if sampling_rate!=final_sr:
        print("Sampling rate ", sampling_rate, "is not equal to hparams.sampling_rate. Using librosa to convert.")
        audio = librosa.resample(audio.astype(np.float32), sampling_rate, final_sr)
    data = audio.astype(np.int16)
    return torch.FloatTensor(data.astype(np.float32)), final_sr


def load_filepaths_and_text(filename, split="|"):
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(split) for line in f]
    return filepaths_and_text


def files_to_list(filename):
    """
    Takes a text file of filenames and makes a list of filenames
    """
    with open(filename, encoding='utf-8') as f:
        files = f.readlines()

    files = [f.rstrip() for f in files]
    return files


def to_gpu(x):
    x = x.contiguous()

    if torch.cuda.is_available():
        x = x.cuda(non_blocking=True)
    return torch.autograd.Variable(x)
