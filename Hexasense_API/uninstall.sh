#!/bin/bash

echo Uninstalling Hexasense API

echo Stopping Hexasense Service
sudo systemctl stop hexaboot

echo Removing Service Files
sudo rm /etc/systemd/system/hexaboot.service
sudo rm /etc/systemd/system/hexaboot.sh

echo Removing Program Files
sudo rm -rf /usr/Hexasense

echo UNINSTALL COMPLETE - PLEASE REBOOT NOW