# QRious
Generate and scan QR-Codes offline.

Reliable local QR code image generation and scanning with automated history tracking.

![QRiousGif](https://github.com/nickravesh/QRious/blob/master/assets/demo.gif)

### The motivation behind it
> In various instances, I found myself in a situation where I needed a quick and secure way to transfer essential text information, such as passwords, keys and URLs, from my computer to my phone. However, the available options were either reliant on an internet connection or involved online services for QR code generation, which raised concerns about security and privacy.  
To address this need, I developed this program—a versatile tool that enables both QR code generation and scanning, completely offline. Whether I'm without an internet connection or simply prefer not to rely on external services, this program allows me to seamlessly create and scan QR codes anytime, ensuring a convenient and privacy-focused solution for my offline data transfer requirements.

## Features

- **QR Code Generation:** Easily create QR codes by entering text through the command line interface.

- **QR Code Scanning:** Scan existing QR codes by providing the absolute path to the image, leveraging powerful decoding capabilities.

- **History Tracking:** Keep track of the last 10 generated QR codes in a log file (`history.log`) with corresponding filenames and timestamps, you can select and open them without leaving the program.

- **User-Friendly Interface:** Navigate through options seamlessly with color-coded prompts and messages for a straightforward user experience.

- **QR Code Display:** View generated QR codes within the terminal, offering quick visual verification.

## One-Liner install for Debian-based distros
```
curl -Ls https://github.com/nickravesh/QRious/archive/master.tar.gz | tar -xz && cd QRious-master && bash install.sh
```

## Usage
After install, use the commands "QRious" or "qr" at any time to generate or scan QR-Codes.

1. After install use the commands "QRious" or "qr" at any time to run QRious.
2. Choose an option: Generate QR code (G), Scan QR code (S), or View History (H).
3. Follow the prompts to generate, scan, or view QR codes.
4. For scanning, provide the absolute path to the QR code image.

## Manual install
Navigate to QRious directory and Install the requirements:
```
pip3 install -r requirements.txt
```
and then run the QRious.py file `python3 QRious.py`

## Contributing	

Contributions are always welcome!  
Whether you're fixing a bug, improving documentation, or implementing a new feature, your contributions are highly valued.

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://opensource.org/licenses/)

[![](https://visitcount.itsvg.in/api?id=QRious&label=Repository%20Views&icon=0&pretty=true)](https://visitcount.itsvg.in)