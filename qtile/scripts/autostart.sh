#!/bin/bash

dbus-update-activation-environment --systemd \
	WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=$XDG_CURRENT_DESKTOP

# Authentication dialog
pkill -f /usr/lib/polkit-kde-authentication-agent-1
/usr/lib/polkit-kde-authentication-agent-1 &

# Start xdg-desktop-portal-wlr  
pkill -f /usr/lib/xdg-desktop-portal-wlr
/usr/lib/xdg-desktop-portal-wlr &

kanshi &
nm-applet &
swayidle -w timeout 600 'swaylock-f' &
dunst &
blueman-applet &
pcmanfm -d &
wl-paste --type text --watch cliphist store &
wl-paste --type image --watch cliphist store &