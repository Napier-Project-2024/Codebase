#!/bin/bash

echo Installing Hexasense API

echo Update and Upgrade packages
sudo apt update -y && sudo apt upgrade -y

echo Installing dependencies
sudo apt install git python3 python3-installer python3-build python3-fastapi python3-uvicorn python3-smbus2 -y

echo Removing any previous installation
sudo rm -rf /usr/Hexasense

echo Make home the working directory
cd ~

echo Cloning Hexasense branch to ~/Hexasense
git clone -b hexasense-v0.1 --single-branch https://github.com/Napier-Project-2024/Codebase.git /usr/Hexasense

echo Change to Codebase dir
cd /usr/Hexasense

echo Cloning AB Electronics Python Libraries
git clone https://github.com/abelectronicsuk/ABElectronics_Python_Libraries.git


echo Copying ADCPi Library to API Folder
cp /usr/Hexasense/ABElectronics_Python_Libraries/ADCPi/ADCPi.py /usr/Hexasense/Hexasense_API

echo Moving to API directory
cd /usr/Hexasense/Hexasense_API

echo Giving boot script executable permission
sudo chmod +x hexaboot.sh

echo Copying hexaboot.sh startup script to systemd directory
sudo cp hexaboot.sh /etc/systemd/system

echo Copying hexaboot.service descriptor file to systemd
sudo cp hexaboot.service /etc/systemd/system

echo Enabling hexaboot service autostart at system boot
sudo systemctl enable hexaboot

echo INSTALL COMPLETE - PLEASE REBOOT TO BEGIN NORMAL OPERATION
echo Navigate to http://localhost:5000 to view the Hexasense API live output
