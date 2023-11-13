#!/bin/bash

wal -q -i ~/.wallpapers

wallpaper=`awk '{print $0}' ~/.cache/wal/wal`

cp $wallpaper ~/.cache/current_wallpaper.jpg

qtile cmd-obj -o cmd -f reload_config

notify-send "Wallpaper and theme changed"
