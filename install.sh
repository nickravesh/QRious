echo "UPDATING REPOSITORIES..."
apt update
echo "UPDATING DONE!"

echo "INSTALLING PIP3..."
apt install python3-pip
echo "INSTALLING PIP3... DONE!"

echo "MOVING THE THE FILES TO /usr/local/bin/QRious"
mkdir /usr/local/bin/QRious
cp * /usr/local/bin/QRious
cd /usr/local/bin/QRious
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
