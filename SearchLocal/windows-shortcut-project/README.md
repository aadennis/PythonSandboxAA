# Windows Shortcut Project

This project contains a PowerShell script that creates a Windows desktop shortcut to a specified Python script. 

## Files

- **create_shortcut.ps1**: A PowerShell script that generates a desktop shortcut pointing to the Python script located at `d:\*(mumble)\SearchContentinLocalDocx.py`. The script allows you to set properties such as the target path, working directory, and icon.

## Prerequisites

- Windows operating system
- PowerShell (comes pre-installed with Windows)
- Permissions to create shortcuts on the desktop

## Usage

If all is working ok, double-click the icon that has been created on your desktop. It should run the Python script specified in the PowerShell script.