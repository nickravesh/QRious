#!/usr/bin/env python3

import segno # to make qr-codes
from getpass import getuser # to get the username of the user running the script
import os # to run system commands
import datetime

userInput = input("Please Enter Your Text, The QR-code Will Be Generated:\n")
qrcode = segno.make_qr(userInput) # make the qr-code using segno

if len(os.listdir(f"{os.path.dirname(__file__)}/history")) == 10: # get the number of files that exists in the history directory
    # get the list of the files in the history directory
    listOfFiles = os.listdir(f"{os.path.dirname(__file__)}/history")
    # This line of code uses the `min()` function with a lambda function as the key to find the oldest file in the `history` directory based on its creation time. The lambda function takes a filename as an argument, joins it with the directory path using `os.path.join()`, and then returns the creation time of the resulting file path using `os.path.getctime()`. The resulting filename is then passed to `os.remove()` to delete the file.
    os.remove(f"{os.path.dirname(__file__)}/history/{min(listOfFiles, key=lambda x: os.path.getctime(os.path.join(f'{os.path.dirname(__file__)}/history/', x)))}")


# gets the path of the script directory and generates a colorful copy of qr-code inside of history directory
qrcode.save(f"{os.path.dirname(__file__)}/history/{datetime.datetime.now().strftime('%Y_%m_%d')}-{datetime.datetime.now().strftime('%H%M%S')}.png", scale=20, dark="yellow", light="#35155D")

# Add /home/zed/.local/bin to the PATH variable of the current process
os.environ["PATH"] += os.pathsep + "/home/zed/.local/bin"

os.system(f'segno --compact "{userInput}"') # to show the qr-code in the terminal