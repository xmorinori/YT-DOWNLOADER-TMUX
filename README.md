# YT DOWNLOADER
YouTube Downloader (Python) – for Android/Termux

## USAGE

### SETUP
Run the Following Commands to Install All The Required Libraries:
```bash
cd yt-downloader
bash install.sh
```

### DOWNLOAD MP3
```bash
cd yt-downloader
python mp3.py
```

### DOWNLOAD MP4
```bash
cd yt-downloader
python mp4.py
```

## MODIFY THE CODE MIT

Make Sure to **First Create A Folder in Your Internal Storage** Before Cloning the Repository.  
Example Path:
```
/sdcard/your_folder_name
```
Then Clone the Repository Into that Folder:
```bash
cd /sdcard/your_folder_name
git clone https://github.com/your-username/yt-downloader.git
```

---

## FILE STRUCTURE

### `install.sh`
```bash
#!/bin/bash

# Update packages and install Python & pip
pkg update -y
pkg install python -y

# Install required Python libraries
pip install pytube
```

### `mp3.py`
```python
from pytube import YouTube
import os

url = input("Enter YouTube video URL: ")
yt = YouTube(url)

print(f"Downloading audio: {yt.title}")
audio_stream = yt.streams.filter(only_audio=True).first()

output = audio_stream.download()
base, ext = os.path.splitext(output)
new_file = base + '.mp3'
os.rename(output, new_file)

print("Download completed:", new_file)
```

### `mp4.py`
```python
from pytube import YouTube

url = input("Enter YouTube video URL: ")
yt = YouTube(url)

print(f"Downloading video: {yt.title}")
video_stream = yt.streams.get_highest_resolution()

video_stream.download()

print("Download completed!")
```

---

✅ TESTED ON TERMUX / ANDROID  
📜 DEVELOPED BY PYTHON & PYLIB

Xmorinori®
