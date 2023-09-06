#!/usr/bin/env python3

import segno # to make qr-codes
from getpass import getuser # to get the username of the user running the script
import os # to run system commands
import datetime # to set a file name for the saved qr-codes in history
from qreader import QReader
from cv2 import cvtColor, imread, COLOR_BGR2RGB
import warnings
import sys

# Suppress warnings
warnings.filterwarnings("ignore")


def controller(status):
    if (status == "G") or (status == "g"):
        generate_QRcode()
    
    elif (status == "H") or (status == "h"):
        history()

    elif (status == "S") or (status == "s"):
        scan_QRcode()
    
    else:
        print("\nWrong input, please try again!\nuse \'g\' to generate QR-Code and \'h\' to see the history.\n")
        controller(input("What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: "))


def generate_QRcode():
    userInput = input("\nPlease Enter Your Text, The QR-code Will Be Generated:\n")
    qrcode = segno.make_qr(userInput) # make the qr-code using segno

    #removes the oldest qr-code in the history directory if there is more than 10 of them
    if len(os.listdir(f"{os.path.dirname(__file__)}/history")) >= 10: # get the number of files that exists in the history directory
        # get the list of the files in the history directory
        listOfFiles = os.listdir(f"{os.path.dirname(__file__)}/history")
        # This line of code uses the `min()` function with a lambda function as the key to find the oldest file in the `history` directory based on its creation time. The lambda function takes a filename as an argument, joins it with the directory path using `os.path.join()`, and then returns the creation time of the resulting file path using `os.path.getctime()`. The resulting filename is then passed to `os.remove()` to delete the file.
        os.remove(f"{os.path.dirname(__file__)}/history/{min(listOfFiles, key=lambda x: os.path.getctime(os.path.join(f'{os.path.dirname(__file__)}/history/', x)))}")


    # gets the path of the script directory and generates a colorful copy of qr-code inside of history directory
    qrcode.save(f"{os.path.dirname(__file__)}/history/{datetime.datetime.now().strftime('%Y_%m_%d')}-{datetime.datetime.now().strftime('%H%M%S')}.png", scale=20, dark="black", light="white")

    # Add /home/[username]/.local/bin to the PATH variable of the current process
    os.environ["PATH"] += os.pathsep + f"/home/{getuser()}/.local/bin"

    os.system(f'segno --compact "{userInput}"') # to show the qr-code in the terminal


def scan_QRcode():
    imageLocation = input("\nEnter the QR-Code image location to scan: ")

    # Redirect standard output and error streams to hide unwanted messages
    sys.stdout = open ("/dev/null", "w")
    sys.stderr = open ("/dev/null", "w")

    qrImage = cvtColor(imread(imageLocation), COLOR_BGR2RGB)
    decodedText = QReader().detect_and_decode(image=qrImage)

    # Restore standard output and error streams
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__

    print(f"\n{str(decodedText)[2:-3]}")




def history():
    print("\n<< History of the last 10 generated QR-Codes >>\n")



controller(input("What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: "))