#!/bin/bash

STATUS=`xinput list-props "ELAN0412:00 04F3:3240 Touchpad" | awk '/Device Enabled/{print $4}'`

if [ $STATUS == 1 ]
then
    xinput disable "ELAN0412:00 04F3:3240 Touchpad"
    notify-send "Touchpad Disabled"
else
    xinput enable "ELAN0412:00 04F3:3240 Touchpad"
    notify-send "Touchpad Enabled"
fi