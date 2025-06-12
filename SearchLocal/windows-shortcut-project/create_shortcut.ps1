# filepath: windows-shortcut-project/windows-shortcut-project/create_shortcut.ps1
$pythonPath = "C:\Python311\python.exe"  # <-- Update this to your Python path
$scriptPath = "d:\Sandbox\git\aadennis\PythonSandboxAA\SearchLocal\SearchContentinLocalDocx.py"
$shortcutPath = "$([Environment]::GetFolderPath('Desktop'))\SearchContentinLocalDocx.lnk"

$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut($shortcutPath)
$Shortcut.TargetPath = $pythonPath
$Shortcut.Arguments = "`"$scriptPath`""
$Shortcut.WorkingDirectory = Split-Path $scriptPath
$Shortcut.Save()
