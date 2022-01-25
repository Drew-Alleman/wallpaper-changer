#!/bin/bash
sudo apt update
sudo apt upgrade
sudo apt install python3
sudo apt install python3-pip
pip3 install -r requirements.txt
sudo mkdir /etc/opt/wallpaper_changer/
sudo -k chmod u+x wpc.py 
sudo cp  wpc.py /usr/local/bin/wpc.py

read -p "[?] Directory to pull wallpaper images: " WALLPAPER_DIR
echo {\"WALLPAPER_DIR\": \""$WALLPAPER_DIR"\",\"change_on_reboot\": false} > config.json
sudo mv config.json /etc/opt/wallpaper_changer/config.json
