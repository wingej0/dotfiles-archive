#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

#starting utility applications at boot time
run nm-applet &
numlockx &
picom &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
blueman-applet &
greenclip daemon &
cp ~/dotfiles/qtile/scripts/variety-x11.sh ~/.config/variety/scripts/set_wallpaper &
variety &
fusuma