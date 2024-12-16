# Tide Times
# A workflow to capture tide times for a single location

December 2024

## Dictation is consigned to legacy - using EasyTide data now

https://easytide.admiralty.co.uk/

<img width="386" alt="image" src="https://github.com/user-attachments/assets/86c55678-77d9-49d0-8c09-82de7093dcaf">

<img width="770" alt="image" src="https://github.com/user-attachments/assets/987f5e7b-a93a-4c40-ac34-cef7bcbd56b2">

<img width="778" alt="image" src="https://github.com/user-attachments/assets/2a811b55-0961-41d1-94b5-058f14fd8494">

<img width="767" alt="image" src="https://github.com/user-attachments/assets/13b7f0bc-f0a6-4dd2-8f24-de1132351015">

<img width="242" alt="image" src="https://github.com/user-attachments/assets/780ddfcc-b44e-474e-9940-9361fc4f8180">

<img width="216" alt="image" src="https://github.com/user-attachments/assets/3a6dec05-1dc9-4b7d-a170-6f4bbdeee6fc">

<img width="894" alt="image" src="https://github.com/user-attachments/assets/e0dc6aa6-743e-45d0-9ee5-91665c266fb7">


I then grab everything between say GMT and predictions, inclusive, and paste that into Notepad++.

Processing after that assumes some consistency in what EasyTide deliver

June 2024

The dictation files should be stored here ```D:\onedrive\Transcribed Files``` and then loaded into Word.

February 2024

See the video here for notes just recording the middle 2 tidetimes for the day. Note that this fails to include the "Bravo" morpheme. The next picture, which begins "0828...", which is the time and tide height for a given day, shows each day being punctuated by a "Bravo".
https://www.youtube.com/watch?v=M5XcVtQ3uUw

<hr>
November 2023

## New format - as 10.2023, plus uses 2 tide times per day, not 4.

The 2 big changes are:

* As generally only 2 tides are usable in a day, just dictate those 2, given how long it takes to dictate the required data.
* No need to determine the High and Low tides as part of the dictation - that can be handled by the code.

Example of dictated data

Taking line 99, 082838145008:  
Note that there is no date. This is deduced by the script.  
The total digits represent all the data required for a single day. In this case, that means:  
At [0828] there is a high or low tide - the script determines which it is.  
That tide height is [3.8] metres - note the implicit decimal point.  
At [1450] there is a further high or low tide. And so on.  

<img width="600" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/7dce7f24-f81f-4591-980d-7c817466cd6b">

This is then pasted into mid-times.py:  

<img width="657" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/6651a113-9c54-470a-8c9c-86587bacc65e">


Example of the output from the processing of that data, ready for input to spreadsheet

<img width="400" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/809d3018-fa76-497b-ba0a-8cd868523ade">

How to call the code, and get the output  
<b>!! YOU CAN NO LONGER JUST CALL PYTEST. IT MUST BE THIS COMMAND !!</b>

```output_text = format_tide_dictation(test_text_1, "12/2023")```  
```print(output_text)```

# Saving the dictated transcription

An example of the name of one of these dictated files:  
```tide_dictated_2023_03.csv```  
Save one copy under  
```(OD)\data\Sea\TideData\tidetimes_dictated```  
So the data is independent of the current dev box, save another copy in the development environment,  here:  
```PythonSandboxAA\TideTimes\test_tide\data```  

October 2023

## New format - excludes commas and dates

<img width="400" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/32aa5111-553e-4a81-8c7b-65ba8b296802">

The video has the detail: https://www.youtube.com/watch?v=KH81r8RIdN0

The new format takes advantage of what I perceive to be Microsoft's improved text to speech engine.

## Python post-processing script

I no longer dictate the date - that is handled by a Python script:

https://youtube.com/shorts/z_AkFMrkiYM

<img width="300" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/2e5af12e-9b3c-418b-94f5-43b51f312761">


March 2023  

# Formatting the source
The source for the monthly tide times is a document like this:

<img width="200" alt="image" src="https://user-images.githubusercontent.com/11707983/227743954-d0ab25bd-84da-4497-8e14-912efcfbab16.png">

You dictate from there into a csv like this:

<img width="299" alt="image" src="https://user-images.githubusercontent.com/11707983/227744089-caca9eab-b75e-48af-ac21-d846f66cb5af.png">
(snip)

<img width="306" alt="image" src="https://user-images.githubusercontent.com/11707983/227744121-f03d6906-ed69-4b51-afef-36c1b8e6c007.png">

"High" means that for every tide listed after "High" the first tide after midnight is High. Until you hit "Low".  
"Low" means that for every tide listed after "Low" the first tide after midnight is Low. Until you hit "High".  
And so on.   
The first column is the date of the month. The next four columns each consist of 4 digits, (for instance, 2133 means the time 21:33), then 2 digits (for instance, 33 means a tide height of 3.3 metres).  4 + 2 = 6 digits per column. The exception to 6 digits per column is the special value "9", which means "just 3 high and low tides today". It is not a null value.  

# Saving the dictated transcription

An example of the name of one of these dictated files:  
```tide_dictated_2023_03.csv```  
Save one copy under  
```(OD)\data\Sea\TideData\tidetimes_dictated```  
So the data is independent of the current dev box, save another copy in the development environment,  here:  
```PythonSandboxAA\TideTimes\test_tide\data```   

# Transforming the transcription to the formatted output

This test file takes the dictated file, and transforms it to the format that the spreadsheet will accept as input:   
```PythonSandboxAA\TideTimes\test_tide\test_tidemonth.py```   

The function in this file that does the transform:
```test_read_monthfile```  

<img width="543" alt="image" src="https://user-images.githubusercontent.com/11707983/227745501-b112e83f-a7c8-4949-a29e-e5ffbe69b3ea.png">

Yes, this is dirty, smelly and lazy, but I can't imagine anyone other than me wants this.

Continuing, edit the month (and year) within the green as appropriate.  

This is the location and command to run:  
<img width="358" alt="image" src="https://user-images.githubusercontent.com/11707983/227745462-22892656-595b-4aaf-a78b-1bf6fad5ff0e.png">

In the source file, there must be only 1 newline at the end, else it fails:  
<img width="222" alt="image" src="https://user-images.githubusercontent.com/11707983/227745323-69705393-34e5-4276-afaa-2cd001095053.png">

The output goes to the screen. Ignore the assert 1 == 2 failure - that is just to force the screen output.   
<img width="572" alt="image" src="https://user-images.githubusercontent.com/11707983/227745557-974b7801-2523-4da7-8167-d605358687c4.png">  
Copy and paste that into a csv file in Notepad++ etc.    
<img width="408" alt="image" src="https://user-images.githubusercontent.com/11707983/227745719-24d36970-5fcc-467f-b845-baa078598b8a.png">
  
Then save that to ``` (OD)\data\Sea\TideData\spreadsheet_input``` before reading it into the Google Sheets Tides 2023 spreadsheet.    

<hr/>
Everything under here is archive - ignore and put somewhere else

https://youtu.be/p9PPx82QUo0 

### Usage

# Server

Raw data - D:\onedrive\data\Sea\TideData

```cd D:\Sandbox\git\aadennis``` 

```.\virtualenvs\venv\Scripts\activate```

```cd .\PythonSandboxAA\TideTimes```

```uvicorn src.tidetimes:app --reload```



![image](https://user-images.githubusercontent.com/61011995/154820525-7fd9ad67-4415-4244-84d3-b751ca733978.png)

# Browser

```http://127.0.0.1:8000/tidetimes```

<hr/>

![image](https://user-images.githubusercontent.com/61011995/154820578-08082d60-8e95-48da-8bb0-61a0ada9d5dc.png)  

<hr/>  

![image](https://user-images.githubusercontent.com/61011995/154820694-9f63ed07-68fe-4845-bc8e-c44046d56e97.png)  

<hr/>

![image](https://user-images.githubusercontent.com/61011995/154849038-dd625cef-ef09-4fa5-ae78-e743c7137e4f.png)

<hr/>

![image](https://user-images.githubusercontent.com/61011995/154820701-fddff4da-7d1c-401a-be73-612fcdb56953.png)

<hr/>  

# Thoughts - June 2022  
Actually voice dictation may be the way to go with this.  
This is the file as created by the app right now:  
<img width="854" alt="image" src="https://user-images.githubusercontent.com/11707983/171927182-2110640c-16c4-490a-9483-42bdaa6d162d.png">

Limited example of current output:

```
01/06/2022,3.15,Low,02:29:00,0.54,High,08:31:00,3.51,Low,14:43:00,0.6,High,20:41:00,3.69  

02/06/2022,3.0,Low,02:59:00,0.62,High,09:02:00,3.41,Low,15:10:00,0.7,High,21:12:00,3.62  
```  

Note the first column (tide date), the second column (tidal range), and the references to Low and High

Tide date: this could be replaced by 1 instead of 01/06/2022 etc, with 6 and 2022 being passed in, in a post-dictation stage. Indeed the number is redundant, but helps me keep my place in the physical booklet.  
Tidal range: again, do this as a second stage function
Low and High: record this only when the first tide type (Low or High) of the day differs from the previous day.

Those points give this, as an example for the dictation output using the sample records above:  
```
Low  
1,0229054,0831351,1443060,2041369 
2,0259062,0902341,1510070,2112362  
...
High
15,etc...
16, etc...
```

Then the second stage takes the first stage output using command line options, to get us back to the original output, so the spreadsheet can take and display as currently. That is, repeating the current output from above...
```
01/06/2022,3.15,Low,02:29:00,0.54,High,08:31:00,3.51,Low,14:43:00,0.6,High,20:41:00,3.69  

02/06/2022,3.0,Low,02:59:00,0.62,High,09:02:00,3.41,Low,15:10:00,0.7,High,21:12:00,3.62  
```  

This all means that the GUI becomes redundant. Shame, but I learnt a bit, and this is more efficient, if I am doing it every month, as I have been, and intend to keep doing, as long as I use the sea :-)

An example of the source document, from which I read the data:

<img width="421" alt="image" src="https://user-images.githubusercontent.com/11707983/171932968-b13250a1-a13e-4c65-87d4-5ff3a985ee14.png">

I aim to use Microsoft Word for the dictation. In the next shot, note the mis-hearing of "new line" even though it was fine for record 1. However, it is picking up the digits, and the commas correctly:

<img width="844" alt="image" src="https://user-images.githubusercontent.com/11707983/171958930-75857711-e3f9-4ed2-8cd2-8c752aa414c2.png">


A working example of a file dictated in MS Word on a pc. Some tidy up was required. For example, [newline] was sometimes interpreted
as a command, sometimes as the literal "new line". And single digits were sometimes spelt out. For example "1" -> "One".

<img width="522" alt="image" src="https://user-images.githubusercontent.com/11707983/176112621-cc19378c-63cb-4f57-a720-a04edbef061d.png">

Dictated files are stored here:

```OD/data/Sea/tidedata/dictated_tides```

Final output for use in the spreadsheet (not discussed here?) - those are here:

```OD/data/Sea/tidedata/spreadsheet_input```

Video of issues when using MS Word Dictation for data entry:

https://www.youtube.com/watch?v=Dzir2im7N7o






