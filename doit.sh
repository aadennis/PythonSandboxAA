#!/bin/bash

# Change to the root directory where your virtual environments are located
# cd /mnt/d/Sandbox/git/aadennis/PythonSandboxAA

# Find directories containing "Scripts/Activate.ps1" and delete them
find . -type d -name 'Scripts' -exec test -f '{}/Activate.ps1' ';' -print | while read dir
do
    # Navigate to the directory containing "Scripts"
    env_dir=$(dirname "$dir")
    echo "Deleting virtual environment: $env_dir"
    rm -rf "$env_dir"
done

