#!/usr/bin/env python3

import segno # to make qr-codes
from getpass import getuser # to get the username of the user running the script
import os # to run system commands
import datetime # to set a file name for the saved qr-codes in history
from PIL import Image # to open image files
from pyzbar.pyzbar import decode # to decode and scan qr-codes
import warnings
import sys
from colorama import Fore # to colorize the texts

# Suppress standard warnings
warnings.filterwarnings("ignore")


def checkIfHistoryDirExists():
    # gets the path of the script directory and creates a history directory
    currentScriptPath = os.path.dirname(__file__)

    if "history" not in os.listdir(currentScriptPath):
        os.mkdir(f"{currentScriptPath}/history")


def controller(status):
    if (status == "G") or (status == "g"):
        generate_QRcode()
    
    elif (status == "H") or (status == "h"):
        history()

    elif (status == "S") or (status == "s"):
        scan_QRcode()
    
    else:
        print(f"\n{Fore.LIGHTRED_EX}Wrong input, please try again!\nuse \'g\' to generate QR-Code, 's' to scan and \'h\' to see the history.{Fore.RESET}\n")
        controller(input(f"{Fore.LIGHTYELLOW_EX}What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: {Fore.RESET}"))


def generate_QRcode():
    checkIfHistoryDirExists()

    def deleteLinesContainingSpecificString(fileName, targetString):
        #open the history.log file in read mode, read its content and save it to a list
        with open(fileName) as file:
            lines = file.readlines()

        # remove lines containing the target string
        modifiedLines = [line for line in lines if targetString not in line]

        # write the modified lines back to the file
        with open(fileName, "w") as file:
            file.writelines(modifiedLines)


    userInput = input(f"\n{Fore.LIGHTCYAN_EX}Please Enter Your Text, The QR-code Will Be Generated:{Fore.RESET}\n")
    qrcode = segno.make_qr(userInput) # make the qr-code using segno

    #removes the oldest qr-code in the history directory if there is more than 10 of them
    if len(os.listdir(f"{os.path.dirname(__file__)}/history")) > 10: # get the number of files that exists in the history directory
        # get the list of the files in the history directory
        listOfFiles = os.listdir(f"{os.path.dirname(__file__)}/history")
        # This line of code uses the `min()` function with a lambda function as the key to find the oldest file in the `history` directory based on its creation time. The lambda function takes a filename as an argument, joins it with the directory path using `os.path.join()`, and then returns the creation time of the resulting file path using `os.path.getctime()`. The resulting filename is then passed to `os.remove()` to delete the file.
        fileToDeletePath = f"{os.path.dirname(__file__)}/history/{min(listOfFiles, key=lambda x: os.path.getctime(os.path.join(f'{os.path.dirname(__file__)}/history/', x)))}"
        os.remove(fileToDeletePath)

        deleteLinesContainingSpecificString(f"{os.path.dirname(__file__)}/history/history.log", fileToDeletePath.split("/")[-1])
        print(fileToDeletePath.split("/")[-1])

    # gets the path of the script directory and generates a copy of qr-code inside of history directory
    filePathToSave = f"{os.path.dirname(__file__)}/history/{datetime.datetime.now().strftime('%Y_%m_%d')}-{datetime.datetime.now().strftime('%H%M%S')}.png"
    qrcode.save(filePathToSave, scale=20, dark="black", light="white")

    # Add /home/[username]/.local/bin to the PATH variable of the current process
    os.environ["PATH"] += os.pathsep + f"/home/{getuser()}/.local/bin"

    os.system(f'segno --compact "{userInput}"') # to show the qr-code in the terminal

    # log the value of the generated qr-code and its file name to the history.log file
    with open(f"{os.path.dirname(__file__)}/history/history.log", "a") as fileHandel:
        fileHandel.write(f"{filePathToSave.split('/')[-1]}||{userInput}\n")


def scan_QRcode():
    checkIfHistoryDirExists()
    try:
        imageLocation = input(f"\n{Fore.LIGHTCYAN_EX}Enter the QR-Code image location to scan: {Fore.RESET}")
        # check if the given path to the qr-code image is valid
        if imageLocation == "" or os.path.exists(imageLocation) == False:
            print(f"{Fore.LIGHTRED_EX}Wrong path to the image!\nplease provide the absolute path to the image you want to scan for QR-Code.{Fore.RESET}")
            scan_QRcode()
        # Redirect standard output and error streams to hide unwanted messages
        sys.stdout = open ("/dev/null", "w")
        sys.stderr = open ("/dev/null", "w")

        qrImage = Image.open(imageLocation)

        # Restore standard output and error streams
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

        decoded_list = decode(qrImage)
        print(f"\n{decoded_list[0].data.decode()}")
    except:
        print(f"\n{Fore.LIGHTRED_EX}Failed to detect qr-code, you can try the following solutions:\n- crop the image to fit the qr-code better\n- make sure the qr-code is not damaged\n- use image with better quality")
        scan_QRcode()
    

def history():
    checkIfHistoryDirExists()
    
    # check to see if the history.log file even exists
    if os.path.exists(f"{os.path.dirname(__file__)}/history/history.log") == False:
        print(f"\n{Fore.LIGHTRED_EX}--No items/history to display here, because you haven't generated any QR-Codes yet--{Fore.RESET}\n")
        controller(input(f"{Fore.LIGHTYELLOW_EX}What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: {Fore.RESET}"))

    else: # do the following when the history.log exists
        print(f"\n{Fore.LIGHTMAGENTA_EX}<< History of the last 10 generated QR-Codes >>{Fore.RESET}\n")

        # open the history.log file, read and then display the log of the saved qr-codes in the history directory with their name and the date they have generated
        with open(f"{os.path.dirname(__file__)}/history/history.log") as file:
            counter = -1
            for line in file:
                counter += 1
                print(f"{counter}. [{line.strip().split('||')[1]}] {Fore.LIGHTBLUE_EX}Generated in{Fore.RESET} {(line.strip().split('||')[0]).split('-')[0]}")

        # ask the user which item they want to see from the history
        selectedItem = input(f"\n{Fore.LIGHTCYAN_EX}Select the number you want to see QR-Code again\nor press Enter to back to the main menue: {Fore.RESET}")
        
        # check if the user just pressed enter key and want to get back to the main menue
        if selectedItem == "":
            controller(input(f"\n{Fore.LIGHTYELLOW_EX}What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: {Fore.RESET}"))
        else:
            try: # open the selected item image from the history
                with open(f"{os.path.dirname(__file__)}/history/history.log") as file:
                    requestedQRcodeFileName = file.readlines()[int(selectedItem)].split('||')[0]
                os.system(f"xdg-open {os.path.dirname(__file__)}/history/{requestedQRcodeFileName}")
                print(f"{Fore.LIGHTGREEN_EX}Opening item from the history...{Fore.RESET}")
                history()
            except: # warn the user that selected item is not valid
                print(f"\n{Fore.LIGHTRED_EX}--Wrong input!, please only enter the number from the range 1 to 10--{Fore.RESET}")
                history()


controller(input(f"{Fore.LIGHTYELLOW_EX}What do you want to do?\n(G)enerate QR-Code, (S)can a QR-Code or See the (H)istory: {Fore.RESET}"))

# TODO: impliment table to show the scanned qr-code more organized and beautiful