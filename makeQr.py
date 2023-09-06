import segno


userInput = input("Please Enter Your Text, The QR-code Will Be Generated:\n")
qrcode = segno.make(userInput)
qrcode.save("qrCode.png")
qrcode.show(scale=20, dark="yellow", light="#323524")