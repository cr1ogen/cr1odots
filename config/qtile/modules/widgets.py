import os
import subprocess
from libqtile import qtile
from libqtile import widget
from qtile_extras import widget as extrawidgets #Extras

from modules.colors import colors

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    fontsize=18,
                    padding=7,
                    highlight_method='block',
                    this_current_screen_border=colors['red'], #'c65c0e',
                    inactive=colors['white'],    
                ),
                widget.Prompt(
                ),
                widget.TaskList(
                    font="Mononoki Nerd Font",
                    fontsize=14,
                    highlight_method='text',
                    foreground=colors['white'],
                    border=colors['red'],
                    max_title_width=200,
                    theme_mode='preferred',
                    theme_path='/usr/share/icons/Paper-Mono-Dark', 
                ),
                widget.Clock(
                    format=' %d %b, %H:%M %p',
                    font='Mononoki Nerd Font Bold',
                    fontsize=16,
                    foreground=colors['red'],
                ),
                widget.Spacer(
                ),
                extrawidgets.StatusNotifier(
                    icon_size=22,
                ),
                widget.TextBox(
                    text='',
                    fontsize=24,
                    foreground=colors['red']
                ),
                widget.KeyboardLayout(
                configured_keyboards=['us','es'],
                foreground=colors['red']
                ),
                extrawidgets.ALSAWidget(
                    mode='both',
                    theme_path='/usr/share/icons/Paper-Mono-Dark',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    margin=13,
                ),
                 extrawidgets.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths=["/home/cr1ogen/.config/qtile/layout-icons/gruvbox-light2"],
                ),

]
