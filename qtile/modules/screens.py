from .get_theme import colors, get_wallpaper

from qtile_extras import widget
from libqtile import bar
from libqtile.config import Screen

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(),
                widget.WindowName(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            background=colors['color0'],
            size=36,
        ),
        wallpaper=get_wallpaper(),
        wallpaper_mode="fill"
    ),
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.GroupBox(),
    #             widget.WindowName(),
    #             widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    #             widget.QuickExit(),
    #         ],
    #         size=36,
    #     ),
    #     wallpaper=get_wallpaper(),
    #     wallpaper_mode="fill"
    # ),
    # Screen(
    #     top=bar.Bar(
    #         [
    #             widget.GroupBox(),
    #             widget.WindowName(),
    #             widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
    #             widget.QuickExit(),
    #         ],
    #         size=36,
    #     ),
    #     wallpaper=get_wallpaper(),
    #     wallpaper_mode="fill"
    # ),
]
