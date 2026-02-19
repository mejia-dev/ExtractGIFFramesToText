# GIF to ASCII Converter

A simple Python desktop app that extracts keyframes from a GIF and converts them into ASCII art saved as RTF files.

## Why
This is a recreation of one of my original Python scripts. I originally wrote the script in 2022 to convert a gif into individual rtf files that could be rendered in a PowerShell window. The original script was written before I had much Python experience, so I decided to recreate it to be a little more refined.

## How It Works

1. Select a `.gif` file using the **Upload GIF** button.
2. Click **Convert to ASCII** to process the file.
3. The app extracts 20 evenly-spaced keyframes from the GIF, converts each to ASCII art, and saves them as `.rtf` files in the `asciitemp/` folder.

## Output

- `asciitemp/0.rtf` through `asciitemp/19.rtf` - ASCII art for each extracted keyframe.
- Intermediate `.png` frame images are deleted automatically after conversion.

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`:
  - ascii-magic `2.7.4`
  - Pillow `12.1.1`

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Configuration

The following constants in `main.py` can be adjusted:

| Constant | Default | Description |
|---|---|---|
| `num_keyframes` | `20` | Number of frames to extract from the GIF |
| `columns` | `100` | Width of the ASCII output in characters |
