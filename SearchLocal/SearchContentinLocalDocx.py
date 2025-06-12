# SearchContentinLocalDocx.py
# This script searches for a specific phrase in all .docx files within a specified folder.
# It extracts text from the .docx files, caches the results, and checks for matches with the given phrase.  

import os
import sys
import json
import zipfile
import xml.etree.ElementTree as ET

DEBUG_ON = True

# Enable or disable debug output
def debug(text):
    """
    Prints debug information if DEBUG_ON is set to True.    
    Args:
        text (str): The debug message to print.
    """
    if DEBUG_ON:
        print(f'DEBUG: {text}')

# Function to extract text from a .docx file
def extract_text_from_docx(file_path):
    """
    Extracts text from a .docx file.    
    Args:
        file_path (str): The path to the .docx file.    
    Returns:
        str: The extracted text from the .docx file, or None if extraction fails.
    """
    try:
        with zipfile.ZipFile(file_path) as docx_zip:
            with docx_zip.open('word/document.xml') as doc_xml:
                xml_content = doc_xml.read()
                # Parse XML and extract all text nodes
                tree = ET.fromstring(xml_content)
                text = ' '.join([node.text for node in tree.iter() if node.text])
                # Normalize whitespace
                text = ' '.join(text.split())
                return text
    except Exception as e:
        print(f"Failed to extract text from {file_path}: {e}")
        return None

# Find all .docx files in a given folder and its subfolders
def find_docx_files(folder):
    """
    Finds all .docx files in the specified folder and its subfolders.
    Args:  folder (str): The folder to search for .docx files.
    Returns:    
        list: A list of paths to .docx files found in the folder.
    """
    docx_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith('.docx'):
                docx_files.append(os.path.join(root, file))
    return docx_files

def get_search_parameters():
    """
    Prompt the user for the folder to search and the phrase to look for.
    Returns:
        tuple: (folder, cache_file, phrase)
    """
    folder_input = input("Enter folder to search (default: D:/OneDrive): ").strip()
    folder = folder_input if folder_input else "D:/OneDrive"

    cache_dir = os.environ.get("TEMP", "/tmp")
    cache_file = os.path.join(cache_dir, "DocxTextCache.json")

    phrase = input("Enter the phrase to search for in .docx files: ").strip()
    if not phrase:
        print("No phrase entered. Exiting...")
        sys.exit(1)
    
    print(f"Searching for Phrase: {phrase}")

    return folder, cache_file, phrase

def load_cache(cache_file) -> dict:
    """
    Loads the cache from the specified file if it exists, otherwise returns an empty dict.
    """
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            print("Failed to load cache file, starting fresh.")
            return {}
    else:
        return {}
    
def process_docx_files(docx_files, cache, phrase) -> list:
    """
    Processes the list of .docx files, updates the cache, and finds matches for the phrase.
    Returns a list of matched file paths.
    """
    matched_files = []
    for file_path in docx_files:
        cache_key = file_path.lower()
        last_write = str(os.path.getmtime(file_path))

        cached_entry = cache.get(cache_key)
        text = None
        if cached_entry and cached_entry.get("LastWriteTime") == last_write and cached_entry.get("Text"):
            text = cached_entry["Text"]
        else:
            text = extract_text_from_docx(file_path)
            if text:
                cache[cache_key] = {"Text": text, "LastWriteTime": last_write}
            elif cache_key in cache:
                del cache[cache_key]

        if text:
            debug(f"[{file_path}] Text: {text[:100]}...")
        else:
            print(f"No text extracted from {file_path}")

        if text and phrase.lower() in text.lower():
            print(f"MATCH: {file_path}")
            matched_files.append(file_path)
    return matched_files    

def main():
    folder, cache_file, phrase = get_search_parameters()

    cache = load_cache(cache_file)

    docx_files = find_docx_files(folder)
    print(f"Found {len(docx_files)} .docx files.")

    # Use the new function
    matched_files = process_docx_files(docx_files, cache, phrase)    

    # Save updated cache
    try:
        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Failed to save cache file: {e}")

    print("\n=========================")
    print(f"Matched Files for phrase: '{phrase}'")
    print("=========================")
    if not matched_files:
        print("No matches found.")
    else:
        for f in matched_files:
            print(f)
    input("Press Enter to exit")

if __name__ == "__main__":
    main()