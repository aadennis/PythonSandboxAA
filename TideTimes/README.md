# Tide Times
## A UI to capture tide times for a single location

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

This could be created in 2 stages:
Firstly, voice dictation that moves from e.g. 

01/06/2022,3.15,Low,02:29:00,0.54,High,08:31:00,3.51,Low,14:43:00,0.6,High,20:41:00,3.69  

02/06/2022,3.0,Low,02:59:00,0.62,High,09:02:00,3.41,Low,15:10:00,0.7,High,21:12:00,3.62  

Note the first column (tide date), the second column (tidal range), and the references to Low and High

Tide date: this could be replaced by 1 instead of 01/06/2022 etc, with 6 and 2022 being passed in, in a post-dictation stage. Indeed the number is redundant, but helps me keep my place in the physical booklet.  
Tidal range: again, do this is a second stage
Low and High: record this only on when the first tide type (Low or High) of the day differs from the previous day.

Those points give this, as an example for the dictation output using the sample records above:  
Low  
1,0229054,0831351,1443060,2041369 
2,0259062,0902341,1510070,2112362  
...
High
15,etc...
16, etc...

Then the second stage takes the first stage output using command line options. This means that the GUI is now redundant. Shame, but I learnt a bit, and this is more efficient, if I am doing it every month, as I have been, and intend to keep doing, as long as I use the sea :-)


