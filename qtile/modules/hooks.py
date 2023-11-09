from libqtile import hook

import subprocess
import os

# Startup applications
@hook.subscribe.startup_once
def autostart():
   home = os.path.expanduser('~/dotfiles/qtile/scripts/autostart.sh')
   subprocess.run([home])