from .get_theme import colors

from libqtile import layout
from libqtile.config import Match

# Define layouts and layout themes
layout_theme = {
        "margin":8,
        "border_width": 4,
        "border_focus": colors['color11'],
        "border_normal": colors['color0']
    }

layouts = [
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.MonadThreeCol(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]
