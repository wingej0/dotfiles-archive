from libqtile.config import Click, Drag, Key
from libqtile.command import lazy

from .groups import groups

mod = "mod4"
terminal = "alacritty --class=terminal"

keys = [
    # Open terminal
    Key([mod], "Return", lazy.spawn(terminal), 
        desc="Launch terminal"),

    # Qtile System Actions
    Key([mod, "shift"], "r", lazy.reload_config(),
        desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(),
        desc="Shutdown Qtile"),

    # Active Window Actions
    Key([mod], "f", lazy.window.toggle_fullscreen(), 
        desc="Toggle window fullscreen"),
    Key([mod], "q", lazy.window.kill(), 
        desc="Close active window"),
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        desc="Increase active window size."
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size."
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        desc="Decrease active window size."
        ),

    # Window Focus (Arrows and Vim keys)
    Key([mod], "Up", lazy.layout.up(),
        desc="Change focus to window above."),
    Key([mod], "Down", lazy.layout.down(),
        desc="Change focus to window below."),
    Key([mod], "Left", lazy.layout.left(),
        desc="Change focus to window on the left."),
    Key([mod], "Right", lazy.layout.right(),
        desc="Change focus to window on the right."),
    Key([mod], "k", lazy.layout.up(),
        desc="Change focus to window above."),
    Key([mod], "j", lazy.layout.down(),
        desc="Change focus to window below."),
    Key([mod], "h", lazy.layout.left(),
        desc="Change focus to window on the left."),
    Key([mod], "l", lazy.layout.right(),
        desc="Change focus to window on the right."),

    # Qtile Layout Actions
    Key([mod], "r", lazy.layout.reset(),
        desc="Reset the sizes of all window in group."),
    Key([mod], "Tab", lazy.next_layout(),
        desc="Switch to the next layout."),
    Key([mod, "shift"], "f", lazy.layout.flip(),
        desc="Flip layout for Monadtall/Monadwide"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle floating window."),

    # Move windows around MonadTall/MonadWide Layouts
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(),
        desc="Shuffle window up."),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Shuffle window down."),
    Key([mod, "shift"], "Left", lazy.layout.swap_left(),
        desc="Shuffle window left."),
    Key([mod, "shift"], "Right", lazy.layout.swap_right(),
        desc="Shuffle window right."),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(),
        desc="Shuffle window up."),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Shuffle window down."),
    Key([mod, "shift"], "h", lazy.layout.swap_left(),
        desc="Shuffle window left."),
    Key([mod, "shift"], "l", lazy.layout.swap_right(),
        desc="Shuffle window right."),
    
    # Switch focus to specific monitor (out of three)
    Key([mod], "o",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 1'),
    Key([mod], "i",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 2'),
    Key([mod], "p",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 3'),

    # Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'),
    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'),
]

# Add group specific keybindings
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Mod + number to move to that group."),
        Key(["mod1"], "Tab", lazy.screen.next_group(),
            desc="Move to next group."),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group(),
            desc="Move to previous group."),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="Move focused window to new group."),
    ])

# Scratchpad keybindings
keys.extend([
    Key(["mod1"], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["mod1"], "v", lazy.group['scratchpad'].dropdown_toggle('volume')),
    Key(["mod1"], "Space", lazy.group['scratchpad'].dropdown_toggle('newTask')),
    Key([mod], "w", lazy.group['scratchpad'].dropdown_toggle('wallpaper')),
])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Application keybindings
keys.extend([
    Key([mod], "Escape", lazy.spawn("xflock4"),
        desc="Lock screen"),
    Key([mod, "shift"], "Return", lazy.spawn("thunar"),
        desc="Launch file browser"),
    Key([mod], "Space", lazy.spawn("xfce4-appfinder"),
        desc="Application launcher"),
    Key(["control", "mod1"], "delete", lazy.spawn("xfce4-session-logout"),
        desc="Launch powermenu"),
    Key([mod], "b", lazy.spawn("firefox"),
        desc="Launch web browser"),
    Key([mod], "m", lazy.spawn("mailspring"),
        desc="Launch email client"),
    Key([mod], "c", lazy.spawn("google-chrome-stable --app=https://calendar.google.com"),
        desc="Launch Calendar"),
    Key([mod], "t", lazy.spawn("telegram-desktop"),
        desc="Launch Telegram"),
    Key([mod], "e", lazy.spawn("google-chrome-stable --app=https://tasks.google.com/embed/\?origin\=https://mail.google.com\&fullWidth\=1\&amp\;lfhs\=2"),
        desc="Launch Tasks"),
    Key([mod], "v", lazy.spawn("copyq show"),
        desc="Clipboard Manager"),
    
    # System76 Power Management
    Key(["control", "mod1"], "b", lazy.spawn("system76-power charge-thresholds --profile balanced"),
        desc="Set charge threshold to balanced"),
    Key(["control", "mod1"], "d", lazy.spawn("system76-power charge-thresholds --profile max_lifespan"),
        desc="Set charge threshold to max lifespan"),
    Key(["control", "mod1"], "f", lazy.spawn("system76-power charge-thresholds --profile full_charge"),
        desc="Set charge threshold to full charge"),
    Key(["control", "mod1"], "n", lazy.spawn("system76-power profile balanced"),
        desc="Set power profile to balanced"),
    Key(["control", "mod1"], "l", lazy.spawn("system76-power profile battery"),
        desc="Set power profile to battery life"),
    Key(["control", "mod1"], "p", lazy.spawn("system76-power profile performance"),
        desc="Set power profile to performance"),

    # Media Keys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl -- set-sink-volume 0 +5%"),
        desc="Volume Up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl -- set-sink-volume 0 -5%"),
        desc="Volume Down"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle"),
        desc="Toggle Mute"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"),
        desc="Play/Pause"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"),
        desc="Next Song"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"),
        desc="Previous Song"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"),
        desc="Stop music"),
    Key([], "XF86TouchpadToggle", lazy.spawn("/home/wingej0/dotfiles/scripts/touchpad-toggle.sh"),
        desc="Toggle Touchpad"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"),
        desc="Increase brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"),
        desc="Decrease brightness"),
])
