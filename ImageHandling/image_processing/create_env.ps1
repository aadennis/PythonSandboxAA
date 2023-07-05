# Create and activate the virtual env named in the 
# variable $venv_folder.
# To deactivate, the command is "deactivate". This is picked up by 
# the existing path, so no need to specify the path explicitly.
# (However, if you want to activate again, you do have to specify the 
# full path again, e.g. ".\.env_image_p\Scripts\activate ")
$venv_folder = ".env_image_p"

py -m venv $venv_folder
Start-Sleep 2
& .\$venv_folder\Scripts\activate