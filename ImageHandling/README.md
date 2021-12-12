# PythonSandbox - ImageHandling
### Requirements
* These notes assume:  
  * Python 3
  * a Windows environment

* To make sure each module works, if not already up-to-date / installed, run...  
  * ``python -m pip install --upgrade pip``   
  * ``python -m pip install pyautogui``  
  * ``python -m pip install pillow``  
  * ``python -m pip install opencv-python``  (for video rendering)

###### Note to self: these scripts are typically downloaded to \\wsl$\Ubuntu-20.04\home\dennis\PythonSandbox\ImageHandling\src and D:/Sandbox/PythonSandbox/ImageHandling
---

## 🟢 resize_image.py 🟢  
Resize a set of pictures to a default width of 600 pixels, or to a specified width. Adjust the height proportionately, relative to that width.

### Motivation
When sending multiple photos by email, you may hit a total volume limit imposed by the ISP.
If you do not need to send the full size photos, reducing their size may avoid you hitting that limit.

### Usage  
``py resize_image.py dir  ``  
where dir is a folder with the set of images to be resized.  

Files in the folder which have the extension [.txt, .mp4] are skipped.  
Resized photos are saved to the folder ``temp`` under the folder passed as the argument, with ``_600`` added to the name.  
For example, ``c:/Photos/MyPhoto.jpg`` is saved as ``c:/Photos/Temp/MyPhoto_600.jpg``.  
(But if you asked, for example,  for the target width to be 800px, then ```_800``` would be added to the name).

The original photos are not updated.

### Example 1 - specify the folder containing the images to be processed
``$dir = 'C:/Photos'``    
``py resize_image.py $dir  ``

### Example 2 - as Example 1, plus specify a width of 800 pixels
``$dir = 'C:/Photos'``    
``py resize_image.py $dir 800  ``

---

## 🟢 save_screenshot.py 🟢  
Save a screenshot every few seconds, passing a unique string for the session, to be included in the filename for the output image file, resulting in shots named e.g.  
* "c:/temp/thelist_MySession_1.png",  
* "c:/temp/thelist_MySession_2.png", etc.

### Motivation
If I view a video, a good way of retaining key information without copying the whole of the video, is to save screenshots every few seconds. While this may result in high volumes, that volume is way less than the size of the original video.

### Usage
If you have 2 screens, the images are those of the master screen. For me right now, that is the right-hand screen.  
``py save_screenshot.py ``

### Example 1 - every n seconds, save a screenshot to folder y  
Right now, you must edit the script before running it. todo - parameterize.   
So right now, the only example is as for Usage, that is..  
``py save_screenshot.py ``  
In practice for now, the interval between saving screenshots is 10 seconds, and the root save folder is /temp  

---
## 🟢 imageset_to_video.py 🟢 
Given a set of images in a single folder, create a video from those images.

### Requirements
The configuration file ```image_handling.ini``` must exist, in the same folder as ```imageset_to_video.py``` and have values for (the values are just examples here - adjust for your setup):  
  * src_template = D:\exampleroot\examplesubfolder
  * file_template = myfile_

The entry for ```file_template``` in ```image_handling.ini``` allows the module to determine what set of filenames to expect.  
For example, given an entry of  ```file_template = myfile_```, then the scripts expects a set of files like this:
```
myfile_1.png  
myfile_2.png  
...  
myfile_10.png  
etc  
```
The files will be processed in numerical sequence. The module allows breaks in the sequence, and the number part of the first image can be greater than 1.  
Note that there are no trailing zeroes before the numbers.  
🔴 Todo - expect any extension (png, etc), but no mix of extensions. For example, png and jpg in the same batch is not allowed.  


### Usage
``py .\imageset_to_video.py ``   
---
## 🟢 image_slideshow.py 🟢 
Given a set of images in a single folder, display them as a slideshow, with a configurable delay.  
The images are sorted by modified date ascending, given that the screenshots will have been recorded in sequence,  
at least for the scenario where the screenshots were saved when following a video along.  
There are no parameters available to the UI, as configuration is stored in image_handling.ini, in the same folder as this .py.  

#### image_handling.ini

**src_folder**: the folder containing the set of images to be displayed.    
(**file_template**: deprecated - to be removed)  
**slide_show_delay**: the delay between image display in seconds. This can be changed, before, and during the run.  
**start_iteration**: example - if start_iteration is [1], the display will start at the image with the oldest modified (sic) datetime in the folder. If start_iteration is [10], the display will skip the 9 oldest images, and begin the display at the 10th oldest image.  
**pause_slideshow_ind**: the default of False means "Do not pause". Changing to true/True causes the display to freeze until the indicator is changed back to False, or to any value that is not True/true.

![image](https://user-images.githubusercontent.com/61011995/141142480-45827050-b60b-4bea-bdbd-0d2164224d5e.png)



### Usage
``py .\image_slideshow.py `` 
---


