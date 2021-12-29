# https://github.com/yt-dlp/yt-dlp
# python3 ./yt-dlp.py

import datetime
from sys import platform
import os


def download_yt_video():
    ytexe = "./yt-dlp"
    yt_prefix = "https://www.youtube.com/watch?v="

    if (platform == 'linux'):
        SAVE_PATH = "/tmp" 
        #\\wsl$\Ubuntu-20.04\tmp
    else: # assume win32
        raise ValueError

    if not os.path.exists(ytexe):
        # non-checked in static copy: D:\software\VideoSoftware\YoutubeDownloader\yt-dlp 
        raise FileNotFoundError("no file found: [{}]. Exiting...".format(ytexe))

    link = input("Paste the YouTube URL (only the part aafter 'v='): ")        
    command_line = f"{ytexe} {yt_prefix}{link} -o '{SAVE_PATH}/%(title)s-%(id)s'.mp4"
    print(f"[cmd line]: {command_line}")

    os.system(command_line)

    print("Completed download at {}".format(datetime.datetime.now()))
    print("See '[download] Destination' above for output folder and video name")


download_yt_video()
