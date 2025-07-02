# yt-downloader  
YouTube Downloader (Python) – for Android/Termux

## 📦 Usage

### 🔧 First-time Setup
Run the following commands to install all the required libraries:
```bash
cd yt-downloader
bash install.sh
```

### 🎵 Download MP3
```bash
cd yt-downloader
python mp3.py
```

### 📹 Download MP4
```bash
cd yt-downloader
python mp4.py
```

## ✏️ Modify the Code

If you plan to edit the code, make sure to **first create a folder in your internal storage** before cloning the repository.  
Example path:
```
/sdcard/your_folder_name
```
Then clone the repository into that folder:
```bash
cd /sdcard/your_folder_name
git clone https://github.com/your-username/yt-downloader.git
```

---

## 📂 File Structure

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

✅ Tested on Termux (Android)  
📜 Developed with Python & Pytube

Xmorinori®
