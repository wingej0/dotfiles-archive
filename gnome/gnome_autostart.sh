#!/bin/bash

killall blueman-applet &
cp /home/wingej0/dotfiles/gnome/set_wallpaper /home/wingej0/.config/variety/scripts/set_wallpaper &
emacs --daemon
