# https://github.com/yt-dlp/yt-dlp
# Todo - redo docs
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
# https://docs.yt-dlp.org/en/latest/README.html?highlight=stdout#embedding-yt-dlp

import datetime
import glob
from sys import platform
import os


def save_video(link, single_or_list, sub_folder:str = "default"):
    ytexe = "yt-dlp.exe"
    yt_prefix = ""
    playlist_parameter = ""

    if not link:
        return ["Please put an entry in the 'identifier...' box, before clicking [Save]."]

    print(f"subfolder: {sub_folder}")
    if sub_folder == None:
        sub_folder = "default"
    sub_folder = sub_folder.title().replace(' ','')
    data_folder = f"data/{sub_folder}"
    
    print(data_folder)
    if not os.path.exists(ytexe):
        # non-checked-in static copy: D:\software\VideoSoftware\YoutubeDownloader\yt-dlp 
        raise FileNotFoundError("no file found: [{}]. Exiting...".format(ytexe))
    
    if (is_single_video(single_or_list)):
        yt_prefix = "https://www.youtube.com/watch?v="
        output_template = f"{data_folder}/%(title)s-%(id)s"
    else:  # list...
        yt_prefix = "https://www.youtube.com/watch?list="
        playlist_parameter = "--yes-playlist"
        output_template = f"{data_folder}/%(playlist_index)s-%(title)s-%(id)s"

    command_line = f"{ytexe} {yt_prefix}{link} {playlist_parameter} --write-description -o {output_template}.mp4"
    print(f"[cmd line]: {command_line}")
    status = os.system(command_line)
    if status != 0:
        return ["Unable to download this video. Please check the id."]

    search_path = f"{data_folder}/*{link}*.mp4"
    print(f"video_filepath is {search_path}")
    video_file = (glob.glob(search_path))[0].replace('\\','/')
    print(video_file)
    dt = datetime.datetime.now().strftime("%H:%M:%S")
    return [f"Completed download to the server at {dt}.", f"File is [{video_file}]."]


def is_single_video(download_type):
    """
    A single video has been requested (true) or...
    A list has been requested (false).
    """
    if (download_type == "single"):
        return True
    return False


