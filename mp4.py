from youtube_dl import YoutubeDL
from youtube_search import YoutubeSearch
import ffmpeg
import os, json 
import asyncio
from mutagen.easyid3 import EasyID3
from time import strftime
from time import gmtime

ydl_opts = {
          'format': 'best/bestvideo',
          'outtmpl': '/sdcard/ytdl/%(title)s.%(ext)s',
      }


ydl_opts_SD = {
          'format': 'worst/worstvideo',
          'outtmpl': '/sdcard/ytdl/%(title)s.%(ext)s',
      }
      

print("\n\n                   Downloader YouTube\n\n")

search = input("Masuk kan Keyword Pencarian atau Link YT : ")


if search.startswith("https://"):
    yt_url = search
    
if not search.startswith("https://"):
    yt = YoutubeSearch(search, max_results=1).to_json()
    print(f'Search a "{search}"')
    try:
        yt_id = str(json.loads(yt)['videos'][0]['id'])
    except PermissionError:
        print('Error')
    yt_url = 'https://www.youtube.com/watch?v=' + yt_id
    print(yt_url)

quality = input("Pilih Resolusi Video (SD/HD) : ")

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(yt_url, download=False)
    video_url = info_dict.get("url", None)
    video_id = info_dict.get("id", None)
    video_title = info_dict.get('title', None)
    video_uploader = info_dict.get('uploader', None)
    video_duration = info_dict.get('duration', None)

duration = strftime("%H:%M:%S", gmtime(video_duration))
print(f"Title : {video_title}\nDuration : {duration}\nURL : {yt_url}\nUploader : {video_uploader}")


if quality == "HD":
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])
if quality == "SD":
    with YoutubeDL(ydl_opts_SD) as ydl:
        ydl.download([yt_url])