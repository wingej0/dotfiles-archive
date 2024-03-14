import subprocess

from libqtile import qtile
from libqtile.command import lazy
from libqtile.widget import TextBox
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

from .get_theme import colors
from .widget_defaults import widget_defaults

dark_widgets = {
    "decorations" : [
        RectDecoration(
            colour = colors['color11'],
            filled = True,
            radius = 10,
            padding_y = 4,
            group = True
        )
    ]
}

light_widgets = {
    "decorations" : [
        RectDecoration(
            colour = colors['color15'],
            filled = True,
            radius = 10,
            padding_y = 4,
            group = True
        )
    ]
}

mid_widgets = {
    "decorations" : [
        RectDecoration(
            colour = colors['color1'],
            filled = True,
            radius = 10,
            padding_y = 4,
            group = True
        )
    ]
}

def init_widgets(monitor):
    widgets_list = [
        widget.Sep(
            linewidth = 0,
            padding = 5
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **dark_widgets
        ),
        widget.TextBox(
            font="FontAwesome6Free",
            fontsize=14,
            foreground=colors['color15'],
            text="",  
            **dark_widgets
        ),
        widget.TextBox(
            font="Fira Code Nerd Font Bold",
            fontsize = 12,
            foreground=colors['color15'],
            text="Qtile",
            mouse_callbacks={
                'Button1' : lazy.spawn('xfce4-appfinder'),
            },
            **dark_widgets          
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **dark_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            margin=0,
            padding=5,
            **light_widgets
        ),        
        widget.Memory(
            foreground=colors['color0'],
            format='{MemPercent}%',
            measure_mem="M",
            margin=0,
            padding=0,
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            foreground=colors['color0'],
            padding=10,
            size_percent=60,
            **light_widgets
        ), 
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            margin=0,
            padding=5,
            **light_widgets
        ),        
        widget.CPU(
            foreground=colors['color0'],
            format='{load_percent}%',
            margin=0,
            padding=0,
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            foreground=colors['color0'],
            padding=10,
            size_percent=60,
            **light_widgets
        ), 
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            padding=5,
            **light_widgets
        ),
        widget.ThermalSensor(
            foreground=colors['color0'],
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.TextBox(
            text='',
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            **light_widgets
        ),
        widget.GenPollText(
            foreground=colors['color0'],
            func=lambda: subprocess.check_output("/home/wingej0/dotfiles/scripts/brightness.sh").decode("utf-8").strip(),
            update_interval=30,
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            foreground=colors['color0'],
            padding=10,
            size_percent=60,
            **light_widgets
        ), 
        widget.TextBox(
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            text="",
            **light_widgets
        ),
        widget.Volume(
            foreground=colors['color0'],
            get_volume_command = "/home/wingej0/dotfiles/qtile/scripts/volume.sh",
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **mid_widgets
        ),
        widget.CurrentLayoutIcon(
            foreground=colors['color15'],
            scale=0.50,
            **mid_widgets
        ),
        widget.CurrentLayout(
            foreground=colors['color15'],
            **widget_defaults,
            **mid_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **mid_widgets
        ),
        widget.CapsNumLockIndicator(
            padding = 10,
            update_interval = 1,
            **widget_defaults
        ),
        widget.Spacer(),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **dark_widgets
        ),
        widget.GroupBox(
            active=colors['color15'],
            borderwidth = 2,
            foreground=colors['color15'],
            disable_drag=True,
            font="FontAwesome6Free",
            fontsize=11,
            hide_unused=False,
            highlight_color=['#00000000', '#00000000'],
            highlight_method="line",
            inactive=colors['color6'],
            this_current_screen_border=colors['color15'],
            this_screen_border=colors['color15'],
            other_current_screen_border=colors['color1'],
            other_screen_border=colors['color0'],
            urgent_method = "line",
            use_mouse_wheel=False,
            **dark_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **dark_widgets
        ),
        widget.Spacer(),
        widget.Mpris2(
            display_metadata = ['xesam:title', 'xesam:artist', 'xesam:album'],
            fmt = "{}",
            padding = 10,
            paused_text = " {track}",
            width = 200,
            **widget_defaults,
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **mid_widgets
        ),
        widget.TextBox(
            font="FontAwesome6Free",
            text="",
            foreground=colors['color15'],
            **mid_widgets
        ),
        widget.CheckUpdates(
            foreground=colors['color15'],
            distro='Arch_checkupdates',
            display_format='{updates}',
            initial_text='0',
            no_update_string='0',
            **widget_defaults,
            **mid_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **mid_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.TextBox(
            font="FontAwesome6Free",
            fontsize=12,
            foreground=colors['color0'],
            text="",
            **light_widgets
        ),
        widget.Battery(
            foreground=colors['color0'],
            format="{percent:2.0%}",
            **widget_defaults,
            **light_widgets
        ),
        widget.GenPollText(
            foreground=colors['color0'],
            func=lambda: subprocess.check_output("/home/wingej0/dotfiles/scripts/power-profile.sh").decode("utf-8").strip(),
            update_interval=30,
            mouse_callbacks={
                'Button1' : lazy.spawn('alacritty -e /home/wingej0/dotfiles/scripts/power-management.sh'),
            },
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("google-chrome-stable --app=https://bard.google.com"),
            },
            **light_widgets
        ),
        widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("variety --selector")
            },
            **light_widgets
        ),
        widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('nautilus'),
            },
            **light_widgets
        ),
        # widget.TextBox(
        #     foreground=colors['color0'],
        #     font="FontAwesome6Free",
        #     fontsize=12,
        #     text='',
        #     mouse_callbacks={
        #         'Button1' : lazy.spawn("/home/wingej0/dotfiles/qtile/scripts/clipboard.sh"),
        #     },
        #     **light_widgets
        # ),
        # widget.TextBox(
        #     foreground=colors['color0'],
        #     font="FontAwesome6Free",
        #     fontsize=12,
        #     text='',
        #     mouse_callbacks={
        #         'Button1' : lazy.spawn('/home/wingej0/dotfiles/scripts/grim.sh'),
        #     },
        #     **light_widgets
        # ),
        widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('blueman-manager'),
            },
            **light_widgets
        ),
        widget.WiFiIcon(
            active_colour = colors['color0'],
            foreground = colors['color0'],
            interface = "wlp0s20f3",
            padding_y = 9,
            mouse_callbacks={
                'Button3' : lazy.spawn('alacritty -e nmtui'),
            },
            **widget_defaults,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **light_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10
        ),
        widget.Sep(
            linewidth = 0,
            padding = 10,
            **dark_widgets
        ),
        widget.Clock(
            foreground=colors['color15'],
            font="Fira Code Nerd Font Bold",
            fontsize=12,
            format=' %b %d | %I:%M %p',
            mouse_callbacks={
                'Button1' : lazy.spawn('xfce4-session-logout'),
            },
            **dark_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 15,
            **dark_widgets
        ),
        widget.Sep(
            linewidth = 0,
            padding = 5
        ),
    ]

    if qtile.core.name == "x11":
        clipboard = widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("/home/wingej0/dotfiles/qtile/scripts/greenclip.sh"),
            },
            **light_widgets
        )

        screenshot = widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('flameshot launcher'),
            },
            **light_widgets
        )

    elif qtile.core.name == "wayland":
        clipboard = widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn("/home/wingej0/dotfiles/qtile/scripts/clipboard.sh"),
            },
            **light_widgets
        )

        screenshot = widget.TextBox(
            foreground=colors['color0'],
            font="FontAwesome6Free",
            fontsize=12,
            text='',
            mouse_callbacks={
                'Button1' : lazy.spawn('/home/wingej0/dotfiles/scripts/grim.sh'),
            },
            **light_widgets
        )

    widgets_list.insert(50, clipboard)
    widgets_list.insert(51, screenshot)

    return widgets_list