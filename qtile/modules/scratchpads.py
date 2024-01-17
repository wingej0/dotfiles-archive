from .groups import groups

from libqtile.config import ScratchPad, DropDown, Match

# Define Scratchpads
groups.append(ScratchPad("scratchpad", [
    DropDown("term", "alacritty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("volume", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.8),
    DropDown("newTask", "alacritty -e /home/wingej0/scripts/tasks/tasks.py",
        width=0.7, height=0.05, x=0.15, y=0.475, opacity=1),
    DropDown("angular", "alacritty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
    DropDown("notebook", "alacritty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))