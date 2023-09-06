import segno # to make qr-codes
import os # to run system commands

userInput = input("Please Enter Your Text, The QR-code Will Be Generated:\n")
qrcode = segno.make(userInput)

# gets the path of the script directory and generates a colorful copy of qr-code inside of history directory
qrcode.save(f"{os.path.dirname(__file__)}/history/qrCode.png", scale=20, dark="yellow", light="#323524")

os.system(f'/home/zed/.local/bin/segno --compact "{userInput}"')