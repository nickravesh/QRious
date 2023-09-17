echo "UPDATING REPOSITORIES..."
sudo apt update
echo "UPDATING DONE!"

echo "INSTALLING PIP3..."
sudo apt install python3-pip
echo "INSTALLING PIP3... DONE!"

echo "MOVING THE THE FILES TO /usr/local/bin/QRious"
sudo mkdir /usr/local/bin/QRious
sudo cp * /usr/local/bin/QRious
sudo cd /usr/local/bin/QRious
echo "MOVING... DONE!"

echo "INSTALLING REQUIREMENTS..."
pip install -r requirements.txt
cd ~
echo "INSTALLING REQUIREMENTS... DONE!"

echo "ONE MOMENT... SETTING THINGS UP..."
echo "alias qr='python3 /usr/local/bin/QRious/main.py'" >> ~/.bashrc
echo "alias QRious='python3 /usr/local/bin/QRious/main.py'" >> ~/.bashrc
echo "ALL DONE!"
echo "Now just type 'QRious' or 'qr' to get started."
