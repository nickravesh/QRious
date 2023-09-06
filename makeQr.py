import segno
from subprocess import Popen # to run shell commands
import os

userInput = input("Please Enter Your Text, The QR-code Will Be Generated:\n")
qrcode = segno.make(userInput)
qrcode.save("qrCode.png", scale=20, dark="yellow", light="#323524")

os.system(f'/home/zed/.local/bin/segno --compact "{userInput}"')