from datasets import load_dataset
from phonemizer import phonemize
from scipy.io import wavfile
from phonemizer.backend.espeak.wrapper import EspeakWrapper

EspeakWrapper.set_library("C:\Program Files\eSpeak NG\libespeak-ng.dll")


# Load the Dutch dataset
dataset = load_dataset("ylacombe/cml-tts", "dutch", split="train", streaming=True)
# Filter for speaker_id = 5809
dataset = dataset.filter(lambda x: x["speaker_id"] == 5809)
iterator = iter(dataset)

# Example format:
# {'audio': {'path': '6892_8912_000729.wav', 'array': array([-1.52587891e-...7344e-05]), 'sampling_rate': 24000}, 'wav_filesize': 601964, 'text': 'Proszę pana, tu pano... zdziwiony', 'transcript_wav2vec': 'proszę pana tu panow... zdziwiony', 'levenshtein': 0.96045197740113, 'duration': 13.648979591836737, 'num_words': 29, 'speaker_id': 6892}


# For all the data:
# 1) Save the array as a wav file according to the path (prepending Data/local/cml-tts_dutch/wavs/)
# 2) Convert the text to phonemes using phonemizer and save it to a file in the format filename.wav|transcription|speaker
print("Saving data...")

# Delete text file if it already exists
with open("Data/train_dutch.txt", "w", encoding="utf-8") as file:
    file.write("")

i = 0
while i < 10000:
    try:
        data = next(iterator)
        # Print out the text and count
        print(i, data["text"])
        audio_path = f"Data/local/cml-tts_dutch/wavs/{data['audio']['path']}"
        # Save the audio using scipy io wavfile write
        wavfile.write(audio_path, data["audio"]["sampling_rate"], data["audio"]["array"])
        # Convert text to phonemes
        phonemes = phonemize(data["text"], language="nl", backend="espeak", preserve_punctuation=True, with_stress=True)
        # Save the phonemes to a file
        with open("Data/train_dutch.txt", "a", encoding="utf-8") as file:
            file.write(f"{data['audio']['path']}|{phonemes}|{data['speaker_id']}\n")
        i += 1
    except StopIteration:
        break

