#!/bin/bash

export \
	NO_AT_BRIDGE=1 \
	ELM_SCALE=1.5 \
	ELM_ENGINE=wayland_egl \
	GDK_SCALE=2 \
	GDK_DPI_SCALE=1 \
	GDK_BACKEND=wayland \
	MOZ_ENABLE_WAYLAND=1 \
	WLR_BACKENDS=headless \
	CLUTTER_BACKEND=wayland \
	SDL_VIDEODRIVER=wayland \
	CLUTTER_BACKEND=wayland \
	QT_QPA_PLATFORM=wayland-egl \
	QT_AUTO_SCREEN_SCALE_FACTOR=1 \
	ECORE_EVAS_ENGINE=wayland-eglexport

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
kanshi &
# nm-applet &
# swayidle -w timeout 600 'swaylock-f' &
# dunst &
# blueman-applet &
# pcmanfm -d &
# system76-power daemon &
# /usr/lib/system76-driver/system76-user-daemon &
# sh -c "systemctl --user start xfce4-notifyd.service 2>/dev/null || exec /usr/lib/xfce4/notifyd/xfce4-notifyd" &
# xfsettingsd
# wl-paste --type text --watch cliphist store &
# wl-paste --type image --watch cliphist store &