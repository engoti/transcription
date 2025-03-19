# transcription

**Audio Transcription using OpenAI Whisper**


**Overview**

This script utilizes OpenAI's Whisper model to transcribe audio from a .wav file and save the resulting text to a file. The script is designed to process an audio file located in the user's Downloads folder and generate a transcription.

**Prerequisites**

Before running the script, ensure you have the following:

1.Python installed (>=3.7 recommended)

2.whisper library installed

3.ffmpeg installed (required by Whisper for audio processing)

**Installation**

1.Install the Whisper library using pip:

pip install openai-whisper

2.Install ffmpeg:

Windows: Download from ffmpeg.org and add it to your system PATH.

MacOS: Install via Homebrew:

brew install ffmpeg

Linux: Install using the package manager:

sudo apt install ffmpeg  # Debian/Ubuntu
sudo dnf install ffmpeg  # Fedora

**Usage**

Place the .wav file (gang.wav) in the Downloads folder.

Run the script using:

python tran.py

The script will:

Load the Whisper model (default: base model).

Transcribe the provided .wav file.

Print the transcription to the console.

Save the transcription to gan.txt in the Downloads folder.

**Customization**

Change the model size by modifying:

model = whisper.load_model("base")

Available models: tiny, base, small, medium, large.

Modify the input file path:

wav_file_path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'your_audio.wav')

Adjust the output file name:

output_path = os.path.join(os.environ['USERPROFILE'], 'Downloads', 'your_output.txt')

**Troubleshooting**

Ensure gang.wav exists in the specified directory.

Check if ffmpeg is installed correctly.

Verify that the Whisper library is installed and up to date.

**License**

This project is licensed under the MIT License.

