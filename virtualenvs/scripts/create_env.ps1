# Create and activate a virtual env whose name is based on the 
# current working directory. 
# So execute this from the project folder, e.g. PythonSandbox/FaceDetection.
# To emphasise: you do not specify your own folder name for the venv.
# To deactivate, the command is "deactivate". This is picked up by 
# the existing path, so no need to specify the path explicitly.
# (However, if you want to activate again, you do have to specify the 
# full path again, e.g. ".\.env_image_p\Scripts\activate ")

# Usage:
# (go to project directory, then)
# ..\virtualenvs\scripts\create_env.ps1

$currentDirectory = Split-Path -Path $pwd -Leaf
"Current directory: [$currentDirectory]"
$working_folder = ".env_$currentDirectory"

# no editing below...
$root_venv_folder = "D:\Sandbox\git\aadennis\PythonSandboxAA\virtualenvs\envs"
$root_venv_folder
$venv_folder = "$root_venv_folder\$working_folder"
"Creating venv in [$venv_folder]"

$python_instance = "C:\Users\Dennis\AppData\Local\Programs\Python\Python312\python.exe"
& $python_instance -m venv $venv_folder
Set-Location $venv_folder

# Now from command line, run 
./Scripts/activate
