#!/usr/bin/env python3

VERSION = "2.0.0"

import os
from os import listdir
from os.path import isfile, join

import subprocess
import random
import pywal
import json

CONFIG_FILE_LOCATION = r'/etc/opt/wallpaper_changer/config.json'

class WallpaperChanger():
    def __init__(self):
        self.WALLPAPER_DIR = None
        self.change_on_reboot = False

    '''
    Reads json config file

    @return json object

    '''
    def read_config_file(self):
        with open(CONFIG_FILE_LOCATION) as config_file:
            return json.loads(config_file.read())

    '''
    Fetches a random wallpaper from the wallpaper directory

    @param config json object of the config file

    '''
    def apply_config_settings(self, config):
        self.WALLPAPER_DIR = config['WALLPAPER_DIR']
        change_on_reboot = config['change_on_reboot']

    def load_config(self):
        config = self.read_config_file()
        self.apply_config_settings(config)

    '''
    Fetches a random wallpaper from the wallpaper directory

    @return wallpaper file location

    '''
    def get_random_wallpaper(self):
        random_wallpaper =  random.choice([f for f in listdir(self.WALLPAPER_DIR) if isfile(join(self.WALLPAPER_DIR, f))])
        return self.WALLPAPER_DIR + random_wallpaper


    '''
    Changes the colors of the terminal 

    @param image    Wallpaper File location
    '''
    def set_color_theme(self, image):
        image = pywal.image.get(image)
        colors = pywal.colors.get(image)
        pywal.wallpaper.change(image)
        pywal.sequences.send(colors)


    '''

    Gets current wallpaper

    @return File location of current wallpaper

    '''
    def get_current_wallpaper(self):
        output = subprocess.run(['gsettings', 'get', 'org.gnome.desktop.background', 'picture-uri'], stdout=subprocess.PIPE)
        decoded_output = output.stdout.decode('utf-8')
        return decoded_output[8:].replace("'", "").strip()

    def change(self):
        self.load_config()
        wallpaper = self.get_random_wallpaper() # Generate random wallpaper
        while wallpaper.replace(" ", "%20") == self.get_current_wallpaper(): # If the random wallpaper is the current wallpaper
            wallpaper = self.get_random_wallpaper() # Generate a new one

        self.set_color_theme(wallpaper) # Apply color theme
    
if __name__ == '__main__':
    W = WallpaperChanger()
    W.change()
