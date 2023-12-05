import subprocess

from libqtile import qtile
from libqtile.command import lazy
from libqtile.widget import TextBox
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration
from qtile_extras.widget.mixins import TooltipMixin

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

# Tooltip definitions for wifi widget
class WifiTextBox(TextBox, TooltipMixin):

    def __init__(self, *args, **kwargs):
        TextBox.__init__(self, *args, **kwargs)
        TooltipMixin.__init__(self, **kwargs)
        self.add_defaults(TooltipMixin.defaults)

        # The tooltip text is set in the following variable
        self.tooltip_background = colors['color0']
        self.tooltip_color = colors['color15']
        self.tooltip_padding = 10
        self.tooltip_font = "Fira Code Nerd Font"
        self.tooltip_text = subprocess.check_output("/home/wingej0/dotfiles/scripts/wifi.sh").decode("utf-8").strip()

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
        ),
        widget.Sep(
            background=colors['color11'],
            linewidth = 0,
            **powerline_left,
        ),
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
            margin=0,
            padding=5,
        ),        
        widget.Memory(
            background=colors['color15'],
            foreground=colors['color0'],
            format='{MemPercent}%',
            # format= '{MemUsed: .0f}{mm}/{MemTotal:.0f}{mm}',
            measure_mem="M",
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
            text='',
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
            margin=0,
            padding=5,
        ),        
        widget.CPU(
            background=colors['color15'],
            foreground=colors['color0'],
            format='{load_percent}%',
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
            text='',
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
            padding=5,
        ),
        widget.ThermalSensor(
            background=colors['color15'],
            foreground=colors['color0'],
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ), 
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
        ),
        widget.GenPollText(
            background=colors['color15'],
            foreground=colors['color0'],
            func=lambda: subprocess.check_output("/home/wingej0/dotfiles/scripts/brightness.sh").decode("utf-8").strip(),
            update_interval=30,
            **widget_defaults
        ),
        widget.Sep(
            background=colors['color15'],
            foreground=colors['color0'],
            padding=10,
            size_percent=60
        ), 
        widget.TextBox(
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
            text="",
        ),
        widget.Volume(
            background=colors['color15'],
            foreground=colors['color0'],
            get_volume_command="/home/wingej0/dotfiles/qtile/scripts/volume.sh",
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
        widget.CurrentLayoutIcon(
            background=colors['color1'],
            foreground=colors['color15'],
            scale=0.55,
        ),
        widget.CurrentLayout(
            background=colors['color1'],
            foreground=colors['color15'],
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
            other_current_screen_border=colors['color1'],
            other_screen_border=colors['color0'],
            use_mouse_wheel=False,
        ),
        widget.Sep(
            background=colors['color11'],
            linewidth = 0,
            **powerline_left,
        ),
        widget.Spacer(),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            font="FontAwesome6Free",
            text="",
            background=colors['color1'],
            foreground=colors['color15'],
        ),
        widget.CheckUpdates(
            background=colors['color1'],
            foreground=colors['color15'],
            distro='Arch_checkupdates',
            display_format='{updates}',
            initial_text='0',
            no_update_string='0',
            **widget_defaults,
            **powerline_left
        ),
        widget.Sep(
            foreground='#00000000',
            linewidth=10,
            **powerline_right
        ),
        widget.TextBox(
            font="FontAwesome6Free",
            fontsize=14,
            background=colors['color15'],
            foreground=colors['color0'],
            text="",
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
            mouse_callbacks={
                'Button1' : lazy.spawn('alacritty -e /home/wingej0/dotfiles/scripts/power-management.sh'),
            },
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
            mouse_callbacks={
                'Button1' : lazy.spawn("google-chrome-stable --app=https://bard.google.com"),
            }
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("variety --selector")
            }
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("/home/wingej0/dotfiles/qtile/scripts/clipboard.sh"),
            }
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('thunar'),
            },
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('/home/wingej0/dotfiles/scripts/grim.sh'),
            }
        ),
        widget.TextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('blueman-manager'),
            }
        ),
        WifiTextBox(
            background=colors['color15'],
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=14,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('alacritty -e nmtui'),
            }
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
