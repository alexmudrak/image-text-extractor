# Image Text Extractor (ITE)


This Python script allows users to take a screenshot of a selected screen
region and perform Optical Character Recognition (OCR) on it to extract text.
The text is then printed to the console and can be copied to the clipboard.
The script supports both English and Russian text recognition and is designed
to work with the X11 window system.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- Python libraries: `PIL`, `pytesseract`, and `Xlib`
- Tesseract OCR with the Russian and English language data
- An X11 environment

You can install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

For Tesseract OCR, please follow the installation instructions for your
operating system and make sure to install the language data for
Russian (`rus`) and English (`eng`).

## Usage

To use the script, run it from the terminal within an X11 session. Follow the
on-screen instructions to select the screen region for capturing the
screenshot.

```bash
python3 src/main.py
```

1. Click on the start point of the region you want to capture.
2. Click on the end point of the region.
3. The script will take a screenshot of the selected region, perform OCR, and
print the recognized text to the console.
4. The image is also copied to the clipboard.

## Features

- Easy to use with simple clicks to define the screenshot region.
- Supports text recognition in Russian and English.
- Prints the recognized text to the console.
- Copies the screenshot image to the clipboard.
- Compatible only with the X11 window system.

## License

This project is open-sourced under the MIT License. See the LICENSE file for
more information.

## Disclaimer

This tool is for educational purposes only. Please do not use it for
unauthorized screen captures or text recognition. It is designed to work only
with the X11 window system and may not function correctly in other
environments.

