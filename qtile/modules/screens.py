from .get_theme import colors, get_wallpaper
from .widgets import init_widgets

from qtile_extras import widget
from libqtile import bar
from libqtile.config import Screen

screens = [
    Screen(
        top=bar.Bar(
            widgets=init_widgets(),
            background='#00000000',
            margin=8,
            size=30,
            opacity=0.9
        ),
        wallpaper=get_wallpaper(),
        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets=init_widgets(),
            background='#00000000',
            margin=8,
            size=30,
            opacity=0.9
        ),
        wallpaper=get_wallpaper(),
        wallpaper_mode="fill"
    ),
    Screen(
        top=bar.Bar(
            widgets=init_widgets(),
            background='#00000000',
            margin=8,
            size=30,
            opacity=0.9
        ),
        wallpaper=get_wallpaper(),
        wallpaper_mode="fill"
    ),
    Screen(
        wallpaper='/home/wingej0/Pictures/kids1.jpg',
        wallpaper_mode="fill"
    ),
]
