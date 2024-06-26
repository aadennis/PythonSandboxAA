# https://github.com/yt-dlp/yt-dlp
# python3 ./yt-dlp.py
# If target_leaf (see code) does not exist, it will be created.
# 
# In wsl/linux, to create a symlink to the usual place...
# 1. ln_target='/mnt/e/Zoolz/C/Videos/YouTube/Others'
# 2. sudo ln -s $ln_target /wintemp
# So... ls -l /wintemp 
# lrwxrwxrwx 1 root root 36 Dec 29 16:36 /wintemp -> /mnt/e/Zoolz/C/Videos/YouTube/Others
#
# The script requires these binaries (not checked-in) in the same folder as yt-dlp.py:
# yt-dlp for linux
# yt-dlp.exe for windows
# These are here: https://github.com/yt-dlp/yt-dlp#installation
# Or static version are here: D:\onedrive\Software\Utilities\VideoTools\yt-dlp
# 
# Testing:
# My own Youtube video (6mb) is here: FFs4JIUbXJU
# See here for the download options, and more generally within that, look for "playlist":
# https://github.com/yt-dlp/yt-dlp#download-options

import datetime
from sys import platform
import os


def get_download_type():
    """
    This is one of V(single video), or L(list)
    """
    ans = input("Enter L/l to download a list, else a (single) video is assumed: ").capitalize()
    if ans == "L":
        return "L"
    return "V"

def is_single_video(download_type):
    """
    A single video has been requested (true) or...
    A list has been requested (false).
    """
    if (download_type == "V"):
        return True
    return False


def download_yt_video():
    ytexe = "yt-dlp.exe"
    yt_prefix = "https://www.youtube.com/watch?list="

    if (platform == 'linux'):
        SAVE_PATH = "/wintemp" 
    else: # assume win32
        SAVE_PATH = "E:/ScratchVideos"

    if not os.path.exists(ytexe):
        # non-checked-in static copy: D:\software\VideoSoftware\YoutubeDownloader\yt-dlp 
        raise FileNotFoundError("no file found: [{}]. Exiting...".format(ytexe))

    download_type = get_download_type()
    playlist_parameter = ""
    output_template = ""
   
    link = input("Paste the YouTube URL (only the part after 'v=' or after 'list='): ")  
    target_leaf = input(f"What is the folder under {SAVE_PATH} to save the video? (return = none): ")     

    if (is_single_video(download_type)):
        yt_prefix = "https://www.youtube.com/watch?v="
        output_template = f"{SAVE_PATH}/{target_leaf}/%(title)s-%(id)s"
    else:  # list...
        yt_prefix = "https://www.youtube.com/watch?list="
        playlist_parameter = "--yes-playlist"
        output_template = f"{SAVE_PATH}/{target_leaf}/%(playlist_index)s-%(title)s-%(id)s"

    do_debug = input("Debug On? (Yy for Yes; else No): ").capitalize()
    verbose = "-v"
    if do_debug != "Y":
        verbose = ""

    command_line = f"{ytexe} {verbose} {yt_prefix}{link} {playlist_parameter} -o {output_template}.mp4"
    print(f"[cmd line]: {command_line}")

    os.system(command_line)

    print("Completed download at {}".format(datetime.datetime.now()))
    print("See '[download] Destination' above for output folder and video name")


download_yt_video()
