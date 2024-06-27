import os
from pydub import AudioSegment
from vosk import Model, KaldiRecognizer
import wave
import json

# Function to convert MP3 to WAV Mono PCM
def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    sound = AudioSegment.from_mp3(mp3_file_path)
    sound = sound.set_channels(1)
    sound.export(wav_file_path, format="wav")

# Function to transcribe WAV using Vosk
def transcribe_wav(wav_file_path, model):
    wf = wave.open(wav_file_path, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError("Audio file must be WAV format mono PCM.")
    
    rec = KaldiRecognizer(model, wf.getframerate())
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))
    transcription = " ".join([res.get("text", "") for res in results])
    return transcription

# Paths
input_directory = "./mp3_files"  # Replace with the path to your input directory
output_directory = "./txt_files"  # Replace with the path to your output directory
model_path = "vosk-model-en-us-0.42-gigaspeech"  # Replace with the path to your Vosk model directory

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Load the Vosk model
model = Model(model_path)

# Process all MP3 files in the input directory
for file_name in os.listdir(input_directory):
    if file_name.endswith(".mp3"):
        mp3_file_path = os.path.join(input_directory, file_name)
        
    
        wav_file_path = "static-monochannel-wave-file--delete-after-if-needed.wav"
        txt_file_name = file_name.replace(".mp3", ".txt")
        txt_file_path = os.path.join(output_directory, txt_file_name)

        if os.path.exists(txt_file_path):
            print(f"{txt_file_path} already exists. Skipping transcription.")
            continue

        # Convert MP3 to WAV
        convert_mp3_to_wav(mp3_file_path, wav_file_path)

        # Transcribe WAV to text
        transcription = transcribe_wav(wav_file_path, model)

        # Save the transcription to a text file
        with open(txt_file_path, "w") as txt_file:
            txt_file.write(transcription)

        print(f"Processed {file_name} and saved transcription to {txt_file_name}")

