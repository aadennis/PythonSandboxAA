# GUI for Youtube Downloader
* What: A video downloader
* How:  A GUI-based wrapper to the excellent yt-dlp utility

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

<hr/>

## 1. Usage
As you will need to do setup before you can use this wrapper, this may seem the wrong sequence. However, I figured that first reading how you use it, would help you decide whether it was for you, before moving on to setup.  

<hr/>

### 1.1 Start the Uvicorn server 

<img width="593" alt="image" src="https://user-images.githubusercontent.com/11707983/158346284-c9064547-b696-4304-a7b8-46710034157c.png">  
<hr/>

### 1.2 Open a browser at http://127.0.0.1:8000/video  

<img width="424" alt="image" src="https://user-images.githubusercontent.com/11707983/161426344-19da7fe8-3880-43a3-bf14-f50e0ed88129.png">
<hr/>

### 1.3 Choose Youtube video or Tiktok video

<img width="380" alt="image" src="https://user-images.githubusercontent.com/11707983/161426460-9ea5d1a2-89ea-4e3c-a918-c56b953f9f5c.png">
<hr/>

### 1.4 Enter a video id (expand Click for Help for more on this)

*Note that the video id ```FFs4JIUbXJU``` can be used for testing Youtube: I wrote it, so no copyright issues, and it is only a few mb.*

<img width="407" alt="image" src="https://user-images.githubusercontent.com/11707983/161426493-01847035-94cd-4504-a15a-779b0498396e.png">

<hr/>

### 1.5 Click [Save]

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158347717-94f17b1e-82c6-4e81-ad69-5d7b3b4a0fe8.png">

<hr/>

### 1.6 After a few seconds (assuming a file size of less than say 1gb), the download location is confirmed:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348220-f0dacb0f-4648-46b4-9276-49cdfd410b5f.png">

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348689-cb916436-e6e2-415b-bf71-55b05a30825c.png">

<hr/>

### 1.7 And from there you can play the mp4:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158348987-f772f8f5-8c7d-43f7-b090-eb045400e196.png">

<hr/>

### 1.8 As mentioned above, expanding Click for Help gives some more detail:

<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158351609-7cb7b4e1-84b6-4052-bf88-ab77f664474f.png">

<hr/>

## 2. Setup
### 2.1 Pre-requisites  
**2.1.1 Server**  
* Windows - _todo - make it Windows/Linux agnostic_  
* Python3    
* clone the parent repo of this readme
* ```pip install ‑r requirements.txt``` - preferably into a virtualenv  
  * If you have a virtual env, then if in PowerShell, you can...
    *  cd D:\Sandbox\git\aadennis
    *  . ./virtualenvs/venv/Scripts/activate
* ```cd (your working root - the root of this repo)  ```
* ```cd .\PythonSandboxAA\VideoHandling\Downloader  ```
* ```uvicorn src.ytdl_view:app --reload ``` 

**2.1.2 Browser**  
http://127.0.0.1:8000/video  

If all of that is successful, you will see this or similar in your server log:    

![image](https://user-images.githubusercontent.com/11707983/158587891-bf5740d4-d8f3-484e-b895-d898fafec416.png)  

and this in your browser:  
<img width="470" alt="image" src="https://user-images.githubusercontent.com/11707983/158637484-d8dfdbfe-e169-448d-a9a2-8c172ae333cc.png">  

## 3. Item dependencies

* "Item" is used very loosely, simply to convey dependencies.  
  * It can be a browser, a binary executable, a Python Module, and so on.  
* Convention: the item on the left-hand side, or source, of the arrow depends on the item on the right-hand side, or target. 
  * As an example, ```ytdl_model.py``` depends on ```yt-dlp.exe```.
  * <small> (I would have preferred a top down dependency shape, but cannot get that right now in Mermaid. But just having Mermaid at all is great - thank you Git Engineering!)</small>

```mermaid
flowchart LR
      v[ytdl_view.py]
      m[ytdl_model.py]
      x[yt-dlp.exe]
      u[uvicorn call]
      b[browser]
      h[ytdl.html]
      v --> m --> x
      b --> h
      h --> v
      u --> v
```

## 4. Tests  
* No automated tests yet.
* For manual testing, note that the video id ```FFs4JIUbXJU``` can be used for testing: I wrote it, so no copyright issues, and it is only a few mb.
## 5. Performance notes
* todo
## 6. Language stack
* Python 3
* FastApi
  * Jinja2 templating
* Uvicorn
* HTML
  * BootStrap
* JavaScript






