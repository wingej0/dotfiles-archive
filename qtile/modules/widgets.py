import subprocess

from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

from .get_theme import colors
from .widget_defaults import widget_defaults

powerline_left = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_left",
        )
    ]
}

powerline_right = {
    "decorations": [
        PowerLineDecoration(
            path="rounded_right",
        )
    ]
}

def init_widgets():
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            **powerline_right,
        ),
        widget.TextBox(
            background=colors['color11'],
            font="FontAwesome6Free",
            fontsize=18,
            foreground=colors['color15'],
            text=""
        ),
        widget.TextBox(
            background=colors['color11'],
            font="Fira Code Nerd Font Bold",
            fontsize=14,
            foreground=colors['color15'],
            text="Qtile",
            **powerline_left
        ),
        widget.WindowName(
            background=colors['color15'],
            empty_group_string=' ',
            foreground=colors['color0'],
            margin=0,
            padding=8,
            scroll=True,
            width=200,
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            text='',
            background=colors['color15'],
            foreground=colors['color0'],
            margin=0,
            padding=0,
            **widget_defaults
        ),        
        widget.Memory(
            background=colors['color15'],
            foreground=colors['color0'],
            format= '{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}',
            measure_mem="G",
            margin=0,
            padding=0,
            **widget_defaults
        ),
        widget.Sep(
            background=colors['color15'],
            foreground=colors['color0'],
            padding=10,
            size_percent=60
        ), 
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            padding=5,
            text="",
            **widget_defaults
        ),
        widget.ThermalSensor(
            background=colors['color15'],
            foreground=colors['color0'],
            **widget_defaults
        ),
        widget.Sep(
            background=colors['color15'],
            foreground=colors['color0'],
            padding=10,
            size_percent=60
        ), 
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            padding=5,
            text="",
            **widget_defaults
        ),
        widget.Volume(
            background=colors['color15'],
            foreground=colors['color0'],
            get_volume_command="~/dotfiles/qtile/scripts/volume.sh",
            **widget_defaults
        ),
        widget.Sep(
            background=colors['color15'],
            linewidth=0,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            text="",
            background=colors['color1'],
            foreground=colors['color15'],
            **widget_defaults
        ),
        widget.CheckUpdates(
            background=colors['color1'],
            foreground=colors['color15'],
            distro='Arch_paru',
            display_format='{updates}',
            initial_text='0',
            no_update_string='0',
            **widget_defaults,
            **powerline_left
        ),
        widget.Spacer(),
        widget.Sep(
            linewidth = 0,
            **powerline_right,
        ),
        widget.GroupBox(
            active=colors['color15'],
            background=colors['color11'],
            foreground=colors['color15'],
            disable_drag=True,
            font="FontAwesome6Free",
            fontsize=14,
            hide_unused=False,
            highlight_color=[colors['color1'],colors['color1']],
            highlight_method="line",
            inactive=colors['color6'],
            this_current_screen_border=colors['color15'],
            this_screen_border=colors['color15'],
        ),
        widget.Sep(
            background=colors['color11'],
            linewidth = 0,
            **powerline_left,
        ),
        widget.Spacer(),
        widget.Sep(
            foreground='#00000000',
            linewidth=20,
            **powerline_right
        ),
        widget.TextBox(
            background=colors['color1'],
            foreground=colors['color15'],
            text="󰃞",
            **widget_defaults
        ),
        widget.GenPollText(
            background=colors['color1'],
            foreground=colors['color15'],
            func=lambda: subprocess.check_output("/home/wingej0/dotfiles/scripts/brightness.sh").decode("utf-8").strip(),
            update_interval=30,
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            text="",
            **widget_defaults
        ),
        widget.Battery(
            background=colors['color15'],
            foreground=colors['color0'],
            format="{percent:2.0%}",
            **widget_defaults,
        ),
        widget.GenPollText(
            background=colors['color15'],
            foreground=colors['color0'],
            func=lambda: subprocess.check_output("/home/wingej0/dotfiles/scripts/power-profile.sh").decode("utf-8").strip(),
            update_interval=30,
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
        ),
        widget.StatusNotifier(
            background=colors['color15'],
        ),
        widget.Sep(
            background=colors['color15'],
            linewidth = 0,
            **powerline_right,
        ),
        widget.Clock(
            background=colors['color11'],
            foreground=colors['color15'],
            font="Fira Code Nerd Font Bold",
            fontsize=14,
            format=' %b %d | %I:%M %p',
        ),
        widget.Sep(
            background=colors['color11'],
            linewidth = 0,
            **powerline_left,
        ),
    ]

    return widgets_list