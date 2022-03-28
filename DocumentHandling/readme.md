# Document handling: infer headings and styles from a plain text document

<!-- vscode-markdown-toc -->
* 1. [Requirement](#Requirement)
* 2. [Setup](#Setup)
	* 2.1. [Prerequisites](#Prerequisites)
* 3. [Usage](#Usage)
	* 3.1. [Content Phase](#ContentPhase)
	* 3.2. [Styling Phase](#StylingPhase)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->




##  1. <a name='Requirement'></a>Requirement
- As an editor  
- Given I have an unformatted document that includes shorter lines that can be inferred as Headings  
- I want to apply rules that result in those Headings being numbered as Level 1 or Level 2  
- So that I can pass it to a Document api (e.g. Google Docs API) to apply Styles  


The project has:  
1. a part to update the content - Python which receives and outputs text with the numbered headings  
1. a part to update the presentation - upload the document from the previous step into Google Docs, and apply JavaScript using the GDocs API   

Example - content stage  
_Before:_
```
The Hare and the Tortoise
The Hare
His amusement
The Hare was much amused at the idea of running a race with the Tortoise
The Tortoise
Slow and steady
The Tortoise did not feel it was a done deal, and ambled slowly along the road
In passing
In the distance, he saw an outline rising and falling, being the silhouette of the hare, as he slept.
```
_After:_
```
The Hare and the Tortoise
1. The Hare
1.1 His amusement
The Hare was much amused at the idea of running a race with the Tortoise
2. The Tortoise
2.1 Slow and steady
The Tortoise did not feel it was a done deal, and ambled slowly along the road
2.2 In passing
In the distance, he saw an outline rising and falling, being the silhouette of the hare, as he slept.
```

In "After", note that:
1. Empty lines are ignored and removed - that is assumed in the remaining points
2. The first line is always the Title, regardless of length. Although not enforced, there must be a Title line, else the numbering will be out of sync
3. A Heading1 (e.g. 1.) or a Heading2 (e.g. 1.1) is a paragraph that has 10 words or less. This is arbitrary, but generally works for my needs
4. A Heading that is immediately followed by another Heading with no text between the 2 headings is a Heading1
5. If it is a Heading, but does not qualify as a Heading1, then it is a Heading 2
6. All other text is body text

##  2. <a name='Setup'></a>Setup
###  2.1. <a name='Prerequisites'></a>Prerequisites
- checkout this repo 
- Windows (todo: Linux )   
- Python 3 to transform the content
- Google Docs account to apply the styles using Javascript

##  3. <a name='Usage'></a>Usage
###  3.1. <a name='ContentPhase'></a>Content Phase  
##### no gui yet
- Open Terminal/PowerShell
- cd to your checkout area for this project. For example:
  - ```cd D:\Sandbox\git\aadennis\PythonSandboxAA\DocumentHandling ```   
- ``` py DocumentHandling/src/DocumentRunner.py ```
- The command line offers defaults for the file folder, and for the source file (right now, to change those, edit ```DocumentRunner.py``` :
- 
<img width="509" alt="image" src="https://user-images.githubusercontent.com/11707983/160418765-c53a425f-f334-470d-9b06-d002c06a0531.png">

- If you choose to enter your own locations, make sure they are valid. 
  - Example of an error message:

<img width="673" alt="image" src="https://user-images.githubusercontent.com/11707983/160419106-53de77f9-a6af-4784-80a2-6b99cbbe4530.png">


Once everything is right, you get this:
![image](https://user-images.githubusercontent.com/11707983/160232583-ca77a164-d9c6-4dd7-a754-67a2c7b9789d.png)

Go to the target location, where your file is waiting for you...

<img width="718" alt="image" src="https://user-images.githubusercontent.com/11707983/160232768-e3689d90-95af-4068-9bbe-1dc98b157f7d.png">

That concludes the content transformation.


###  3.2. <a name='StylingPhase'></a>Styling Phase

You will now upload the content output ("target.txt", say) into Google Docs:


![image](https://user-images.githubusercontent.com/11707983/160234827-21fed24e-cb57-463b-8d30-701ee8e4bb2a.png)

At this stage, the Google document is not styled, other than the default of "Normal text".

<img width="532" alt="image" src="https://user-images.githubusercontent.com/11707983/160234851-7663fcbc-fb9a-44dd-b257-2289e1b6c6fc.png">

Find the Script Editor:  
![image](https://user-images.githubusercontent.com/11707983/160234920-bf3ec899-1ef9-4ed8-86a4-327bb923d60e.png)

Opening Scripts gives a default function in the default Code.gs, in an Untitled project: 

![image](https://user-images.githubusercontent.com/11707983/160234974-98e048bc-8520-47fc-b0bc-fd3f0caa86e3.png)

In GitHub, locate and copy the content of this JS file...  
https://github.com/aadennis/PythonSandboxAA/tree/master/DocumentHandling/GoogleDocsApi

![image](https://user-images.githubusercontent.com/11707983/160235031-f3279f23-f43b-4a3c-919c-361d5b4d60d4.png)

Paste that content over the default function, and press the Save icon:

![image](https://user-images.githubusercontent.com/11707983/160235122-8345c892-4699-48af-91e7-489df2d61f34.png)

Saving updates the content in the dropdown on the menu. Select ```formatHeadings``` :  

![image](https://user-images.githubusercontent.com/11707983/160235167-40b4074c-bef4-4096-80dc-7bf57fb3b8b3.png)

Then press Run:  
![image](https://user-images.githubusercontent.com/11707983/160235177-e1ec9060-cb2c-41cb-8d38-b0b368aa6e47.png)

You will be prompted to authorise the script. Those steps are outside the scope, right now: 

<img width="411" alt="image" src="https://user-images.githubusercontent.com/11707983/160235213-27eb7285-b338-422f-b82d-296a59d30556.png">

Once authorisation is complete, you see this in the AppsScript tab:  
![image](https://user-images.githubusercontent.com/11707983/160235237-574db0f3-57cc-4783-b043-17176c690182.png)


You can now go back to the document tab:  
![image](https://user-images.githubusercontent.com/11707983/160235286-7f3a37eb-fa0b-49eb-b727-665db4e9371c.png)

The content has now been styled based on the functions in the JavaScript:  
![image](https://user-images.githubusercontent.com/11707983/160236201-2343a065-15d2-4fbb-964d-0cc210f3c880.png)

Compare that again with the pre-foramtted version:  
<img width="600" alt="image" src="https://user-images.githubusercontent.com/11707983/160236280-b1582468-e7c5-4d50-8132-368439bd761c.png">











