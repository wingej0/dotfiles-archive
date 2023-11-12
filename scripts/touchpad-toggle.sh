#!/bin/bash

status=`hyprctl getoption device:elan0412:00-04f3:3240-touchpad:enabled | awk '/int/{print $2}'`

if [ $status == "1" ]
then
  hyprctl keyword device:elan0412:00-04f3:3240-touchpad:enabled false
  notify-send -u normal "Touchpad Disabled"
else
  hyprctl keyword device:elan0412:00-04f3:3240-touchpad:enabled true
  notify-send -u normal "Touchpad Enabled"
fi