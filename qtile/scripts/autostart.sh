#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

picom &
run nm-applet &
numlockx &
firewall-applet &
/usr/lib/polkit-kde-authentication-agent-1 &
dunst &
blueman-applet &
caffeine &
pcmanfm -d &



#starting utility applications at boot time
# swww init &
# run nm-applet &
# numlockx &
# clipit &
# firewall-applet &
# /usr/lib/polkit-kde-authentication-agent-1 &
# dunst &
# waybar &
# blueman-applet &
# caffeine &
# pcmanfm -d &
# wl-paste --type text --watch cliphist store &
# wl-paste --type image --watch cliphist store
