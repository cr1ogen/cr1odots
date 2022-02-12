# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

from typing import List  # noqa: F401

from libqtile import bar
from libqtile import layout, hook
from libqtile import widget, qtile
from qtile_extras import widget as extrawidgets
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import pywal
from settings.bar import bar

# Autostart
import os
import subprocess

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

 # Get the number of connected screens

# @hook.subscribe.screens_reconfigured
def get_monitors():
    xr = qtile.screens
    result = len(xr) - 1 if len(xr) > 2 else len(xr)
    if result <= 0:
        result = 1
    logger.warning(f"Number of monitors: {result}")
    return result

monitors = 1
    
# Pywal

colors = []
cache='/home/cr1ogen/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#000000')
    lazy.reload()
load_colors(cache)



mod = "mod4"
terminal = "kitty"
home = os.path.expanduser('~')
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Aplicaciones principales

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "backslash", lazy.spawn("firefox"), desc="Launch Browser"),
    Key([mod,"shift"], "backslash", lazy.spawn("thunar"), desc="Launch File"),


    #Audio
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),

    # Run Apps
    Key([mod], "b", lazy.spawn("rofi -show drun -modi drun"),
        desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="run apps"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "control"], "p", lazy.spawn("wlogout"), desc="Power Options"),
    
    # Take a screenshot of the selected region
    Key([mod], "Print",
        lazy.spawn(home + "/.local/bin/screenshot.sh selected-region"),
        desc='Save the selected region of the screen to the screenshots folder'
        ),
    # Capture region of screen to clipboard
    Key([mod, "shift"], "Print",
        lazy.spawn(home + "/.local/bin/screenshot.sh save-to-clipboard"),
        desc='Capture a region of the screen to the clipboard'
        ),
]



# groups = [Group(i) for i in "12345678"]



# Groups with matches

workspaces = [
    {"name": " ₁", "key": "1", "matches": [Match(wm_class='firefox')], "layout": "monadtall"},
    {"name": " ₂", "key": "2", "matches": [Match(wm_class='kitty'), Match(wm_class='thunar')], "layout": "monadtall"},
    {"name": " ₃", "key": "3", "matches": [Match(wm_class='emacs')], "layout": "monadtall"},
    {"name": " ₄", "key": "4", "matches": [Match(wm_class='telegram-desktop'), Match(wm_class='discord')], "layout": "monadtall"},
    {"name": " ₅", "key": "5", "matches": [Match(wm_class='gimp-2.99')], "layout": "monadtall"},
    {"name": "阮 ₆", "key": "6", "matches": [Match(wm_class='Spotify')], "layout": "monadtall"},
    {"name": " ₇", "key": "7", "matches": [Match(wm_class='soffice')], "layout": "monadtall"},
    {"name": " ₈", "key": "8", "matches": [Match(wm_class='newsboat')], "layout": "monadtall"},
    {"name": " ₉", "key": "9", "matches": [Match(wm_class='Steam')], "layout": "monadtall"},
]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    layouts = workspace["layout"] if "layout" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=layouts))
    keys.append(Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen()))
    keys.append(Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"])))

# Move window to screen with Mod, Alt and number


for i in range(monitors):
    keys.extend([Key([mod, "mod1"], str(i), lazy.window.toscreen(i))])

# DEFAULT THEME SETTINGS FOR LAYOUTS #
layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": colors,
                "border_normal": colors
                }

    
layouts = [
    layout.MonadTall(**layout_theme, single_border_width=0),
    layout.Stack(num_stacks=2, **layout_theme),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font='JetBrainsMonoExtraBold',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = '~/Imágenes/Wallpapers/el_gau10.jpg',
        wallpaper_mode = 'fill',
        top=bar.Bar(
          [
                widget.Image(
                    filename='~/.config/qtile/debian.png',
                    mouse_callbacks={'Button1' : lambda: qtile.cmd_spawn("rofi -show drun -modi drun")},
                    margin_x=10,
                    margin_y=4,
                    background=colors[0],
                ),
                widget.GroupBox(
                    borderwidth=2,
                    highlight_method='line',
                    active='ffffff',
                    inactive='ffffff',
                    this_current_screen_border='ffffff',
                    font='FiraCode Nerd Font',
                    fontsize=14,
                    padding_x=5,
                ),
                widget.TaskList(
                    highlight_method='text',
                    border='585e6c',
                    this_current_screen_border='ffffff',
                    max_title_width=350,
                    icon_size=30,
                    padding=2,
                ),
                widget.Clock(
                    format='%d %^b  |  %H:%M %p'
                ),
                widget.Spacer(
                ),
                widget.Moc(
                    play_color='f6737d',
                ),
                extrawidgets.StatusNotifier(
                    ),
                extrawidgets.ALSAWidget(
                    mode='both',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    theme_path='/usr/share/icons/Numix/',
                ),        
                widget.CurrentLayoutIcon(
                    scale=0.5,
                ),
            ],
            28,
            margin=[4, 8, 0, 8],
            background=colors[0],
            opacity=0.85,
            #border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='xfce4-notifyd'),
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

