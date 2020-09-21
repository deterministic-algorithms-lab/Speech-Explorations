# Understanding Various aspects of Mello-tron Code

1. **music21.ipynb** : Understanding music21 module used in [this function](https://github.com/NVIDIA/mellotron/blob/master/mellotron_utils.py#L240)

2. The mellotron repo is modified to use librosa to convert the audio to hparams.sampling_rate automatically , and change both float32 and int16 data to int16. See [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/utils.py#L13).

3. To transliterate to Hindi. See [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/text/cleaners.py#L20) & [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/text/cleaners.py#L80)