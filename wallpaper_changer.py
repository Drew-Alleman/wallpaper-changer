import os
from os import listdir
from os.path import isfile, join

import random

WALLPAPER_DIR = r'/home/drew/Wallpaper/'

"""
Gets a random wallpaper 

@return Returns a random file path from the WALLPAPER_DIR
"""
def get_random_wallpaper():
    return [f for f in listdir(WALLPAPER_DIR) if isfile(join(WALLPAPER_DIR, f))]


"""
Changes the wallpaper to a random image

@return true/false depending if it succeeded
"""
def random_wallpaper():
    wallpaper = random.choice(get_random_wallpaper())
    return os.system(f'./wal -i "{WALLPAPER_DIR}{wallpaper}"')


if __name__ == '__main__':
    random_wallpaper()
