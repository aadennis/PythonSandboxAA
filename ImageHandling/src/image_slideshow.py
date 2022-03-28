# credit: https://www.daniweb.com/programming/software-development/
#   code/468841/tkinter-image-slide-show-python for the basic
#   slideshow principle.
"""
    Run a slideshow of a set of images, with a configurable delay between each image
"""

from itertools import cycle
import tkinter as tk
import configparser
import os
import glob
import time

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
    src_template = config['image_slideshow']['src_folder']
    delay = int(config['image_slideshow']['slide_show_delay']) * 1000
    start_iteration = int(config['image_slideshow']['start_iteration'])
    pause_slideshow_ind = bool(config['image_slideshow']['pause_slideshow_ind'].lower() == "true")

    config_dict = []
    config_dict = {
        'src_template':src_template,
        'delay':delay,
        'start_iteration':start_iteration,
        'pause_slideshow_ind':pause_slideshow_ind
    }
    return config_dict


def get_image_list():
    """
    Get the list of images to be displayed.
    Do not start including images in the list until the current image count is >=
    the start_iteration value in the config file.
    Sleep for n seconds so the user sees the count in the cmd line before tk kicks in.
    """
    #https://stackoverflow.com/questions/6773584/how-is-pythons-glob-glob-ordered
    image_list = []
    config = get_config()
    src_template = config['src_template']
    _filter = "{}/*.*".format(src_template)
    sorted_files = sorted(glob.glob(_filter), key=os.path.getmtime)
    image_count = len(sorted_files)
    file_count = 0
    for file in sorted_files:
        file_count += 1
        if file_count >= config['start_iteration']:
            image_list.append(file)
    print("There are [{}] images in the list.".format(image_count))
    time.sleep(4)
    return image_list

class App(tk.Tk):
    """
    Manage the display of images as a slideshow.
    """
    src_template = None
    file_template = None
    delay = None
    current_image = 0
    image_count = None
    start_iteration = 1
    pause_slideshow_ind = None

    def __init__(self):
        tk.Tk.__init__(self)
        config = get_config()
        self.delay = config['delay']
        image_list = get_image_list()
        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in image_list)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def pause_slideshow(self):
        """
        Pause the slideshow for n seconds.
        The pause/resume is triggered by a change in the ['pause_slideshow_ind']
        in the .ini.
        """
        if not self.pause_slideshow_ind:
            return
        seconds_paused = 0
        while self.pause_slideshow_ind:
            config = get_config()
            self.pause_slideshow_ind = config['pause_slideshow_ind']
            time.sleep(1) # yes I know you shouldn't
            seconds_paused += 1
            if seconds_paused%10 == 0:
                print("Display has been paused for the last [{}] seconds".format(seconds_paused))
        print("Pause complete - resuming display.")

    def show_config(self):
        config = get_config()
        print("-------------------\n*** Configuration ***")
        for i in config:
            print("{}:[{}]".format(i,config.get(i)))
        print("-------------------\n*** Configuration ***")        

    def show_slides(self):
        """
        Loop over the set of images got in __init__, checking on each iteration
        whether to pause the slide show.
        """
        self.current_image += 1
        old_delay = self.delay
        config = get_config()
        self.delay = config['delay']
        self.pause_slideshow_ind = config['pause_slideshow_ind']
        if self.delay != old_delay:
            print("Changing delay from {}ms to {}ms".format(old_delay, self.delay))
            self.show_config()
        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title("{} (delay: [{}] seconds)(number in sequence: [{}/{}])".format(img_name,
            (self.delay/1000), self.current_image + self.start_iteration, self.image_count))
        self.pause_slideshow()
        self.after(self.delay, self.show_slides)

   

    def run(self):
        """
        Enter tk main loop.
        """
        self.mainloop()

# main
app = App()
app.show_config()
app.show_slides()
app.run()
