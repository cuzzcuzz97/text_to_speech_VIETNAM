# Text-to-Speech (TTS) for Vietnamese using FPT.AI

This repository provides a Python script for generating speech from text using FPT.AI, a Vietnamese text-to-speech service. The generated audio can be downloaded and saved as an MP3 file.

## Requirements

To run the script, you need to have Python installed on your computer. If you don't have it already, you can download and install it from [here](https://www.python.org/downloads/).

You also need to install the required Python packages listed in the `requirements.txt` file. To do this, open a terminal and navigate to the directory where you downloaded the repository. Then, enter the following command:
```
  pip3 install -r requirements.txt
```

## Usage

Before running the script, you need to provide the input text you want to convert to speech. You can do this by editing the `input.txt` file and replacing the sample text with your own text.

To generate speech from the input text, run the following command in the terminal:
```
python3 tts.py
```
Please note that this script should only be used for learning purposes and should not be used for scraping or other unethical activities.

The script will send the input text to FPT.AI, which will generate an audio file. The link to download the file will be printed in the terminal and also saved in the `output.txt` file.

Alternatively, you can uncomment the `download_audio` function in the `tts.py` file to automatically download the audio file to your local machine.

## License

This repository is licensed under the [MIT License](LICENSE).
