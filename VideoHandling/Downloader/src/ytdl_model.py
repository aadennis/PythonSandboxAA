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
import string


def save_video(link, single_or_list, sub_folder:str = "default"):
    ytexe = "yt-dlp.exe"
    yt_prefix = ""
    playlist_parameter = ""

    if not link:
        return ["Please put an entry in the 'identifier...' box, before clicking [Download]."]

    print(f"subfolder: {sub_folder}")
    if sub_folder == None:
        sub_folder = "default"
    # Only make changes to the case if there is more than 1 word...
    words = sub_folder.split()
    print(words)
    print(len(words))
    if len(words) > 1:
        sub_folder = sub_folder.title().replace(' ','')
    data_folder = f"data/{sub_folder}"
    
    print(f"!!!!!!!!!!!!!!data_folder: {data_folder}")
    if not os.path.exists(ytexe):
        # non-checked-in static copy: D:\software\VideoSoftware\YoutubeDownloader\yt-dlp 
        raise FileNotFoundError("no file found: [{}]. Exiting...".format(ytexe))
    
    search_link = ""
    # this is largely about the output template...
    # https://github.com/yt-dlp/yt-dlp#output-template
    if (is_single_video(single_or_list)): # todo - change labels for Tiktok support
        yt_prefix = "https://www.youtube.com/watch?v="
        output_template = f"{data_folder}/%(title)s-%(id)s"
        search_link = link
    else:  # Tiktok - whole of url...
        yt_prefix = ""
        playlist_parameter = ""
        output_template = f"{data_folder}/%(creator)s-%(id)s"
        search_link = link.split('/')[-1] # for Tiktok just want the creator and the long id

    command_line = f"{ytexe} {yt_prefix}{link} {playlist_parameter} --write-description -o {output_template}.mp4"
    print(f"!!!!!!!!!![cmd line]: {command_line}")
    start_time = datetime.datetime.now()
    status = os.system(command_line)
    if status != 0:
        return ["Unable to download this video. Please check the id."]

    end_time = datetime.datetime.now()
    gap = end_time - start_time
    search_path = f"{data_folder}/*{search_link}*.mp4"
    print(f"!!!!!!!!!!!!!!search_path: {search_path}")

    video_file = (glob.glob(search_path))[0].replace('\\','/')
    duration_in_seconds = gap.seconds
    # testing on my network shows that a) a minimum of 2 seconds is needed to pull down a file.
    # b) a 1 second duration points to an already-downloaded file.
    # Later... this may not be true for TikTok, given the files are so small - todo.
    if duration_in_seconds < 2:
        return [f"(This file has already been downloaded to the server.)", f"File is [{video_file}]."]
    return [f"Completed download to the server in [{duration_in_seconds}] seconds.", f"File is [{video_file}]."]


def is_single_video(download_type):
    """
    A single video has been requested (true) or...
    A list has been requested (false).
    """
    if (download_type == "single"):
        return True
    return False


