# GUI for Youtube Downloader
A GUI-based wrapper to the excellent yt-dlp utility.

## Motivation

* **As** a viewer of community videos 
* **I want** a download utility [1] 
* With a user interface that allows me to focus on the important points [2]
* And which has sensible defaults for options that I don't need to change [3]
* **So that** I can spend more time downloading and viewing
* And less time fighting with the command line  

###### [1] This is [yt-dlp](https://github.com/yt-dlp/yt-dlp#readme), of course. It is an excellent utility, and in doing...  
###### [2] my sad little GUI, I am taking liberties with the shoulders of giants. Certainly there are other wrappers out there, with better coding than mine, but this gave me a chance to practise a number of languages in a small way that is useful to me. 
###### [3] Really, all I want to change between runs is the video id. OK, there are options for sub-folders to save to, and to save a list of videos (this right now 03.2022 a bit iffy), but if you took those options away, I would still be happy

## Usage
As you will need to do setup before you can use this wrapper, this may seem the wrong sequence. However, I figured that first reading how you use it would help you decide whether it was for you, before moving on to setup.  

<hr/>

### Start the Uvicorn server 

<img width="593" alt="image" src="https://user-images.githubusercontent.com/11707983/158346284-c9064547-b696-4304-a7b8-46710034157c.png">  
<hr/>

### Open a browser at http://127.0.0.1:8000/video  

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158349683-20dfde7a-e02b-44b3-8b17-1f45c771bb8e.png">  
<hr/>



### Enter a video id (expand Click for Help for more on this)

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158350010-feee0a9b-383a-4e0b-b1f2-80337cd95fe9.png">

<hr/>

### Click [Save]

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158347717-94f17b1e-82c6-4e81-ad69-5d7b3b4a0fe8.png">

<hr/>

### After a few seconds (assuming a file size of less than say 1gb), the download location is confirmed:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348220-f0dacb0f-4648-46b4-9276-49cdfd410b5f.png">

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348689-cb916436-e6e2-415b-bf71-55b05a30825c.png">

<hr/>

### And from there you can play the mp4:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348987-f772f8f5-8c7d-43f7-b090-eb045400e196.png">

<hr/>

### As mentioned above, expanding Click for Help gives some more detail:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158351609-7cb7b4e1-84b6-4052-bf88-ab77f664474f.png">

<hr/>

## Setup
tbd
## Tests  
tbd  
## Performance notes
tbd
## Language stack
tbd


