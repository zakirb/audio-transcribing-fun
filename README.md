
# Audio Transcription Project

## Setup Instructions

### 1. Clone the Repository

First, clone the repository to your local machine:

```sh
git clone https://github.com/zakirb/audio-transcribing-fun
cd audio-transcribing-fun
```

### 2. Create and Activate a Virtual Environment

Create a virtual environment to manage dependencies:

```sh
python -m venv venv
```

Activate the virtual environment:

- On Windows:
  ```sh
  venv\Scripts\activate
  ```

- On macOS and Linux:
  ```sh
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required Python packages using `pip`:

```sh
pip install -r requirements.txt
```

### 4. Download Vosk Model

Download the Vosk model from [Vosk Models](https://alphacephei.com/vosk/models) and extract it to your project directory. Update the `model_path` in the `transcribe_from_mp3.py` script to point to the downloaded model.

Use (if on MacOS or Unix based system, if Windows then fuck you, get it there somehow): 
```sh
curl -O https://alphacephei.com/vosk/models/vosk-model-en-us-0.42-gigaspeech.zip
unzip vosk-model-en-us-0.42-gigaspeech.zip
```

### 5. Usage

- **Convert MP4 files to MP3**

  Place your MP4 files in the `mp4_files` directory. Run the following command to convert them to MP3:

  ```sh
  python convert_mp4_to_mp3.py
  ```

- **Transcribe MP3 files to TXT**

  Ensure your MP3 files are in the `mp3_files` directory. Run the following command to transcribe them to TXT:

  ```sh
  python transcribe_from_mp3.py
  ```

### 6. Directory Structure

Your project directory should look like this:

```
/project_directory
│
├── mp3_files/                 # Directory containing mp3 files
│
├── txt_files/                 # Directory to save txt files
│
├── venv                       # Virtual Environment directory
│
├── convert_mp4_to_mp3.py      # Script to convert mp4 to mp3
│
├── transcribe_from_mp3.py     # Script to transcribe mp3 to txt
│
├── requirements.txt           # List of required packages
│
└── README.md                  # Instructions for setting up the project
```

## Additional Information

- **Deactivating the Virtual Environment**

  To deactivate the virtual environment, simply run:

  ```sh
  deactivate
  ```

- **Updating Dependencies**

  If you add new packages to your project, update the `requirements.txt` file:

  ```sh
  pip freeze > requirements.txt
  ```

## Troubleshooting

If you encounter any issues, ensure that all paths are correct and that the Vosk model is properly downloaded and extracted. For further assistance, refer to the Vosk documentation or create an issue in the project repository.

---

This README provides detailed instructions on setting up a virtual environment, installing dependencies, downloading the Vosk model, and using the provided scripts to convert and transcribe audio files.

It was written with ChatGPT and edited by ya boi, buyer beware.
