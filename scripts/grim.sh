#!/bin/bash

grim -g "$(slurp)" $(xdg-user-dir PICTURES)/screenshots/$(date +'%s_grim.png')
notify-send "Screenshot saved successfully"