#!/bin/bash

nmcli -t -f active,ssid dev wifi | awk -F ':' '/yes/{print $2}'
