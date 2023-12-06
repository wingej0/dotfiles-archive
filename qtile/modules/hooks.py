from libqtile import hook, qtile

import subprocess
import os

# Startup applications
@hook.subscribe.startup_once
def autostart():
   if qtile.core.name == "x11":
      autostartscript = "~/dotfiles/qtile/scripts/x11-autostart.sh"
   elif qtile.core.name == "wayland":
      autostartscript = "~/dotfiles/qtile/scripts/wayland-autostart.sh"
   
   home = os.path.expanduser(autostartscript)
   subprocess.Popen([home])
   