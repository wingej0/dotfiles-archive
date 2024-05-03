#!/bin/bash

rm -r ~/.config/neofetch/

# Install gtk and icon themes
mkdir ~/.local/src
cd ~/.local/src
git clone https://github.com/vinceliuice/Orchis-theme.git 
cd Orchis-theme/
./install.sh -t default -c standard -s standard -l --shell 44
cd ..
git clone https://github.com/vinceliuice/Tela-icon-theme.git 
cd Tela-icon-theme/ 
./install.sh 
cd 

# Clone dotfiles and link to .config files
git clone https://github.com/wingej0/dotfiles 
ln -s /home/wingej0/dotfiles/alacritty ~/.config
ln -s /home/wingej0/dotfiles/dunst ~/.config
ln -s /home/wingej0/dotfiles/neofetch ~/.config
ln -s /home/wingej0/dotfiles/qtile ~/.config
ln -s /home/wingej0/dotfiles/rofi ~/.config
ln -s /home/wingej0/dotfiles/swappy ~/.config
ln -s /home/wingej0/dotfiles/swaylock ~/.config
ln -s /home/wingej0/dotfiles/wal ~/.config
ln -s /home/wingej0/dotfiles/wlogout ~/.config

# Configure git
git config --global user.email "jeff@3dgradebook.com"
git config --global user.name "Jeff Winget"

# Enable cronie
sudo systemctl enable --now cronie
