# OrganisePngFolders.py
## Organize PNG Files into 'Screenshots' Folders

This Python script organizes PNG files into a `Screenshots` folder within each directory under a specified root folder (e.g., OneDrive). It assumes that most PNG files are screenshots and provides a dry-run mode to preview actions before making changes.

## Features

- **Identify PNG Files**: Scans all directories under the specified root folder to find `.png` files.
- **Organize Files**: Moves identified PNG files into a `Screenshots` subfolder within the same directory.
- **Skip Existing 'Screenshots' Folders**: Avoids reprocessing directories already named `Screenshots`.
- **Dry-Run Mode**: Preview folder creation and file moves without making any changes.
- **Conflict Handling**: Warns if a file with the same name already exists in the target folder.

## How It Works

1. The script recursively scans all directories under the specified root folder.
2. For each directory:
   - It identifies all `.png` files.
   - It creates a `Screenshots` folder (if it doesn't already exist).
   - It moves the `.png` files into the `Screenshots` folder.
3. The script provides a dry-run mode to preview actions without making changes.

## Requirements

- Python 3.x
- Standard Python libraries (`os`, `shutil`)

## Usage

1. **Set the Root Folder**: Update the `ROOT` variable in the script to point to your desired root folder (e.g., `c:/onedrive`).
2. **Enable/Disable Dry-Run Mode**:
   - Set `DRY_RUN = True` to preview actions without making changes.
   - Set `DRY_RUN = False` to actually move files.
3. **Run the Script**:
   ```bash
   python OrganisePngFolders.py
   ```

## Example Output

### Dry-Run Mode
```plaintext
Would create (if not exists): c:/onedrive/Folder1/Screenshots
Would move: c:/onedrive/Folder1/image1.png -> c:/onedrive/Folder1/Screenshots/image1.png
Would move: c:/onedrive/Folder1/image2.png -> c:/onedrive/Folder1/Screenshots/image2.png

Total PNG files that are candidates for moving: 2
```

### Actual Run
```plaintext
Created: c:/onedrive/Folder1/Screenshots
Moved: c:/onedrive/Folder1/image1.png -> c:/onedrive/Folder1/Screenshots/image1.png
Moved: c:/onedrive/Folder1/image2.png -> c:/onedrive/Folder1/Screenshots/image2.png

Total PNG files that are candidates for moving: 2
```

## Notes

- The script assumes that most `.png` files are screenshots (80/20 rule).
- It skips directories already named `Screenshots` to avoid reprocessing.
- If a file with the same name already exists in the target folder, the script will issue a warning and skip the file.

## License

This script is provided "as-is" without any warranty. Feel free to modify and use it for your own purposes.