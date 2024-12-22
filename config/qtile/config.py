####     QTILE-WAYLAND     ######
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao 


import os
import subprocess
from libqtile import bar
from libqtile.config import Screen
from libqtile.lazy import lazy
from qtile_extras import widget #as extrawidgets #Extras


# Modules

from modules import hooks
from modules import widgets
from modules.groups import groups
from modules.keys import mod, keys, terminal
from modules.layouts import layouts, floating_layout
from modules.mouse import mouse
from modules.screens import screens
from modules.colors import colors





dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = "Bibata-Modern-Ice"
wl_xcursor_size = 30

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None
wmname = "LG3D"
