# Understanding Various aspects of Mello-tron Code

1. **music21.ipynb** : Understanding music21 module used in [this function](https://github.com/NVIDIA/mellotron/blob/master/mellotron_utils.py#L240)

2. The mellotron repo is modified to use librosa to convert the audio to hparams.sampling_rate automatically , and change both float32 and int16 data to int16. See [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/utils.py#L13).

3. And To transliterate to Hindi. See [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/text/cleaners.py#L20) & [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/master/Mellotron/mellotron/text/cleaners.py#L80) & [here](https://github.com/deterministic-algorithms-lab/Speech-Explorations/blob/fdf7ec136ed1f16cf30091592c71234111a357b5/Mellotron/mellotron/text/__init__.py#L46)

4. **mello_train.ipynb** : To train the model in various modes.

5. The model has two kinds of inference. [One](https://github.com/NVIDIA/mellotron/blob/d4746169ea570d3aa8e5c6dfca91b818e7c01eb6/model.py#L621) where attention is calculated. And [another](https://github.com/NVIDIA/mellotron/blob/d4746169ea570d3aa8e5c6dfca91b818e7c01eb6/model.py#L653) where attention is provided. This provided attention acts as rhythm. The ```style_input``` can either be a mel-spectrogram or an integer, in both inference functions. 
