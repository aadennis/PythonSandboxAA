# I am not using Git Bash because there is no feedback...
# or I do not know how to redirect it.
$rootDir = "D:/Sandbox/git/aadennis"
Set-Location $rootDir
. ./virtualenvs/venv/Scripts/activate
Set-Location $rootDir/PythonSandboxAA/VideoHandling/Downloader
Write-Output "**** open url [ http://127.0.0.1:8000/video ] ****"
uvicorn src.ytdl_view:app --reload
