#USE tran.py and transcribe.py
import os
import whisper

# Path to your .wav file
wav_file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'gang.wav')  # Update the path

# Load the Whisper model
print("Loading Whisper model...")
model = whisper.load_model("base")  # You can use "tiny", "base", "small", "medium", or "large"

# Transcribe the audio
print("Transcribing audio...")
result = model.transcribe(wav_file_path)

# Print the transcription
print("Transcription:")
print(result['text'])

# Save transcription to a text file
output_path = r"os.path.join(os.environ['USERPROFILE'], 'Downloads', 'gan.txt')"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(result['text'])

print(f"Transcription saved to {output_path}")