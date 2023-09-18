#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "UPDATING REPOSITORIES..."
sudo apt update
echo "UPDATING DONE!"

echo "INSTALLING PIP3..."
sudo apt install python3-pip
echo "INSTALLING PIP3... DONE!"

echo "INSTALLING REQUIREMENTS..."
pip install -r requirements.txt --no-warn-script-location
echo "INSTALLING REQUIREMENTS... DONE!"

echo "MOVING THE THE FILES..."
cp -r $SCRIPT_DIR ~/.local/bin/QRious
cd ~/.local/bin/QRious
echo "MOVING... DONE!"

echo "ONE MOMENT... SETTING THINGS UP..."
echo "alias qr='python3 ~/.local/bin/QRious/main.py'" >> ~/.bashrc
echo "alias QRious='python3 ~/.local/bin/QRious/main.py'" >> ~/.bashrc
source ~/.bashrc
echo "ALL DONE!"
echo "Now just type 'QRious' or 'qr' to get started."
