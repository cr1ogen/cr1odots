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
                    font="JetBrainsMono Nerd Font",
                    fontsize=18,
                    padding=7,
                    highlight_method='block',
                    this_current_screen_border=colors['neutral_orange'], #'c65c0e',
                    inactive='ffffff',    
                ),
                widget.Prompt(
                ),
                widget.TaskList(
                    font="JetBrainsMono Nerd Font",
                    fontsize=14,
                    highlight_method='text',
                    foreground='d65d0e',
                    border='ffffff',
                    max_title_width=200,
                    theme_mode='preferred',
                    theme_path='/usr/share/icons/Paper-Mono-Dark', 
                ),
                widget.Clock(
                    format=' %d %b, %H:%M %p',
                    font='JetBrainsMono Nerd Font Bold',
                    fontsize=16,
                    foreground='d65d0e',
                ),
                widget.Spacer(
                ),
                extrawidgets.StatusNotifier(
                    icon_size=22,
                ),
                widget.TextBox(
                    text='',
                    fontsize=24,
                    foreground='d65d0e'
                ),
                widget.KeyboardLayout(
                configured_keyboards=['us','es'],
                foreground='d65d0e'
                ),
                extrawidgets.ALSAWidget(
                    mode='icon',
                    theme_path='/usr/share/icons/Paper-Mono-Dark',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    margin=13,
                ),
                 widget.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths=["/home/cr1ogen/.config/qtile/layout-icons/gruvbox-neutral_orange"],
                ),

]
