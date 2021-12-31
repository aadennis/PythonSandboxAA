"""
Save a screenshot every DELAY seconds passing a unique string for the session, 
resulting in shots named e.g. "c:/temp/thelist_MySession_1.png",
"c:/temp/thelist_MySession_2.png", etc.
python -m pip install pyautogui
Note that pyautogui will not work on wsl because of the absence of a gui.
python.exe -m pip install --upgrade pip
python -m pip install pillow
"""
import pyautogui
import time
import configparser

def get_config():
    """
        Return a dictionary of key/values from a configuration (.ini) file.

    """
    config = configparser.ConfigParser()
    # config.read(r"\\wsl$\Ubuntu-20.04\home\dennis\PythonSandbox\ImageHandling\src\example.ini")
    # This relative path does not work in VS Code, perhaps because execution is from parents.
    # It does work from py command line
    config.read("./image_handling.ini")
    # A config file must have sections, and any property must be read via its parent section.
    # It will not infer even if unique.
    target_folder = config['save_screenshot']['target_folder']
    delay = int(config['save_screenshot']['delay'])
    file_template = config['save_screenshot']['file_template']
    max_images = int(config['save_screenshot']['max_images'])

    config_dict = []
    config_dict = {
        'target_folder':target_folder,
        'delay':delay,
        'file_template':file_template,
        'max_images':max_images
    }
    print(".ini values for section 'save_screenshot'")
    print(config_dict)
    return config_dict

ctr = 0

config = get_config()


while ctr < config['max_images']:
    ctr += 1
    print(ctr)
    time.sleep(config['delay'])
    file_template = "{}/{}_{}.png".format(config['target_folder'], config['file_template'], ctr)
    print(file_template)
    pyautogui.screenshot(file_template)
