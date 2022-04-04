# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao 

from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy

# Modules

from modules import hooks
from modules.keys import mod, keys, terminal
from modules.groups import groups
from modules.layouts import layouts
from modules.mouse import mouse

colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


widget_defaults = dict(
    font="JetBrainsMonoExtraBold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper = '~/Imagenes/Wallpapers/omen.png',
        wallpaper_mode = 'fill',
        top=bar.Bar(
            [
                widget.GroupBox(
                    fontsize=26,
                    highlight_method='text',
                ),
                widget.CurrentLayout(
                ),    
                widget.Prompt(
                ),
                widget.TaskList(
                    highlight_method='text'
                    
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.StatusNotifier(
                ),
                widget.Clock(
                    format="%Y-%m-%d %a %I:%M %p"
                ),
                widget.QuickExit(
                ),
            ],
            26,
            opacity=0.95,
            background=colors[1],
            border_width=[6, 6, 0, 6],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
