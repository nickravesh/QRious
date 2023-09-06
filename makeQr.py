import segno # to make qr-codes
from getpass import getuser # to get the username of the user running the script
import os # to run system commands
import sys

userInput = input("Please Enter Your Text, The QR-code Will Be Generated:\n")
qrcode = segno.make(userInput)

# gets the path of the script directory and generates a colorful copy of qr-code inside of history directory
qrcode.save(f"{os.path.dirname(__file__)}/history/qrCode.png", scale=20, dark="yellow", light="#323524")

# Add /home/zed/.local/bin to the PATH variable of the current process
os.environ["PATH"] += os.pathsep + "/home/zed/.local/bin"

os.system(f'segno --compact "{userInput}"') # to show the qr-code in the terminal