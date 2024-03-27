import torch
from TTS.api import TTS
import pygame
# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# # List available 🐸TTS models
# print(TTS().list_models())

# # Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# # Run TTS
# # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# # Text to speech list of amplitude values as output
# # wav = tts.tts(text="Hello world!", speaker_wav="C:/Users/EndUser/Desktop/gaze/GazeTracking/afdr007.wav", language="en")
# # Text to speech to a file
# tts.tts_to_file(text="Hello world!", speaker_wav="C:/Users/EndUser/Desktop/gaze/GazeTracking/afdr007.wav", language="en", file_path="output.wav") device = "cuda" if torch.cuda.is_available() else "cpu"

#List available 🐸TTS models
print(TTS().list_models())

    # Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    # wav = tts.tts(text="Hello world!", speaker_wav="C:/Users/EndUser/Desktop/gaze/GazeTracking/afdr007.wav", language="en")
    # Text to speech to a file
tts.tts_to_file(text="hi this is rithesh", speaker_wav="C:/Users/EndUser/Desktop/gaze/GazeTracking/afdr007.wav", language="en", file_path="output.wav")

pygame.mixer.init()
pygame.mixer.music.load("output.wav")
pygame.mixer.music.play()

    # Wait for playback to finish
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)