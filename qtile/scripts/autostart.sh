#!/bin/bash

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
# kanshi &
# nm-applet &
swayidle -w timeout 600 'swaylock-f' &
dunst &
# blueman-applet &
system76-power daemon &
/usr/lib/system76-driver/system76-user-daemon &
# sh -c "systemctl --user start xfce4-notifyd.service 2>/dev/null || exec /usr/lib/xfce4/notifyd/xfce4-notifyd" &
# xfsettingsd
# wl-paste --type text --watch cliphist store &
# wl-paste --type image --watch cliphist store &