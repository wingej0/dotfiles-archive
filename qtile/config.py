import os

from modules.get_theme import get_wallpaper, colors
from modules.groups import groups
from modules.hooks import *
from modules.keys import keys, mod
from modules.layouts import layouts, floating_layout
from modules.screens import screens
from modules.scratchpads import *

from libqtile import qtile
from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from libqtile.backend.wayland import InputConfig

# Set xdg variables in Wayland to enable screensharing
if qtile.core.name == "wayland":
    os.environ["XDG_SESSION_DESKTOP"] = "qtile:wlroots"
    os.environ["XDG_CURRENT_DESKTOP"] = "qtile:wlroots"

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?from libqtile.backend.wayland import InputConfig
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = {
    "type:touchpad": InputConfig(tap=True, natural_scroll=True, dwt=True),
    # "type:keyboard": InputConfig(kb_numlock=True),
}

# Name of the window manager
wmname = "qtile"
