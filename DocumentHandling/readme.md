# Document handling: infer headings and styles from a plain text document

## Requirement
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
The Book I Nearly Wrote

First Header
Header Two

Some body and then some repeat all that until more than max for header
2 First Header
2 Header Two

And then some body and then some repeat all that until more than max for header
```
_After:_
```
The Book I Nearly Wrote
1. First Header
1.1 Header Two
Some body and then some repeat all that until more than max for header
2. First Header
2.1 Header Two
2.2 Header again
And then some body and then some repeat all that until more than max for header
```

In "After", note that:
1. Empty lines are ignored and removed - that is assumed in the remaining points
2. The first line is always the Title, regardless of length
3. A Heading1 (e.g. 1.) or a Heading2 (e.g. 1.1) is a paragraph that has 10 words or less. This is arbitrary, but generally works for my needs
4. A Heading that is immediately followed by another Heading with no text between the 2 headings is a Heading1
5. If it is a Heading, but does not qualify as a Heading1, then it is a Heading 2
6. All other text is body text

## Setup
### Prerequisites
- checkout this repo 
- Windows (todo: Linux )   
- Python 3 to transform the content
- Google Docs account to apply the styles using Javascript

## Usage
##### no gui yet
- Open Terminal/PowerShell
- cd to your checkout area for this project. For example:
  - ```cd D:\Sandbox\git\aadennis\PythonSandboxAA\DocumentHandling ```   
- ``` py src/DocumentRunner.py ```
- The command line offers defaults (right now, to change those, edit ```DocumentRunner.py``` :
![image](https://user-images.githubusercontent.com/11707983/160231858-a610e336-9b77-4788-b2f6-20f00e0ba5c1.png)
- If you choose to enter your own locations, make sure they are valid. 
  - Example of an error message:

![image](https://user-images.githubusercontent.com/11707983/160232313-dfe2cefb-25d9-4839-af16-a28f60eb0e52.png)

-   input and output locations are valid, as there is no error handling right now:  
<img width="667" alt="image" src="https://user-images.githubusercontent.com/11707983/160231918-aaaa44dc-5b2b-4d20-add1-eefcd27c6faa.png">

![image](https://user-images.githubusercontent.com/11707983/160232012-1ca4d6ee-87eb-494a-b654-281d3dd2c332.png)

Once everything is right, you get this:
![image](https://user-images.githubusercontent.com/11707983/160232583-ca77a164-d9c6-4dd7-a754-67a2c7b9789d.png)

There is no feedback. Go to the target location, where your file is waiting for you...

![image](https://user-images.githubusercontent.com/11707983/160202268-033faac2-56fd-4039-9082-6195b44d6462.png)

That concludes the content transformation.
- Todo: Styling using JavaScript/Google Docs API








