# Requirement

- I want to hear the clock time spoken every n minutes  
- So that I maintain focus while using a desktop computer

# How

- A Python program ```pomodoro.py``` is executed from PowerShell (but could be any shell that supports Python).  
- This runs forever, or until it is cancelled or the host computer is shut down.
- Every n minutes (currently hard-coded as 15 minutes, on the hour), a synthetic voice reads out (for example),   
```It is 11 15 am```

# Deployment

- Dependencies: Python 3 on the Path
- Check out the ```PythonSandboxAA``` github repo

# Usage
- Navigate to the ```PomodoroStuff``` folder at the command line  
  - For example ```cd D:\Sandbox\git\aadennis\PythonSandboxAA\PomodoroStuff```
  - ```python pomodoro.py  ```
    - The script will sit there until zero, 15, 30 or 45 minutes past the hour is reached
    - It will then call out the time every 15 minutes
    - If you want to cancel the time announcements, then for a Powershell session, press ctrl-c
    - The script is sensitive to exactly when the run was started, so you may have to wait up to 59 seconds past the minute for the time to be called out (bug)
   
      
<img width="556" alt="image" src="https://github.com/aadennis/PythonSandboxAA/assets/11707983/10e8819f-d140-4b73-b8c5-fc936ac3e512">




