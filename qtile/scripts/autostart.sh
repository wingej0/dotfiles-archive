#!/bin/bash

kanshi &
nm-applet &
swayidle -w timeout 600 'swaylock-f' &
dunst &
blueman-applet &
pcmanfm -d &
wl-paste --type text --watch cliphist store &
wl-paste --type image --watch cliphist store &