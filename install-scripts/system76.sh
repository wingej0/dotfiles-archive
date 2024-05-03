#!/bin/bash

# Install System76 software
yay -S system76-firmware-daemon-git firmware-manager-git system76-driver system76-acpi-dkms system76-power

# Start services for S76
sudo systemctl enable --now system76-firmware-daemon
sudo gpasswd -a $USER adm
sudo systemctl enable --now system76
sudo systemctl enable --now com.system76.PowerDaemon.service

