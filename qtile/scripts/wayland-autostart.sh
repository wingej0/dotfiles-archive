#!/bin/bash

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP &

/usr/libexec/polkit-gnome-authentication-agent-1 &
swayidle -w timeout 600 'swaylock -f' &
dunst &
system76-power daemon &
# /usr/lib/system76-driver/system76-user-daemon &
wl-paste --type text --watch cliphist store &
wl-paste --type image --watch cliphist store &
cp ~/dotfiles/qtile/scripts/variety-wayland.sh ~/.config/variety/scripts/set_wallpaper &
variety &
emacs daemon
