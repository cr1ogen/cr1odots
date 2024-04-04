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
                    fontsize=16,
                    padding=9,
                    center_aligned=True,
                    highlight_method='block',
                    this_current_screen_border=colors['orange'],
                    inactive=colors['white'],    
                ),
                widget.Prompt(
                ),
                widget.TaskList(
                    font="Mononoki Nerd Font",
                    fontsize=14,
                    icon_size=20,
                    margin=3,
                    highlight_method='text',
                    foreground=colors['white'],
                    border=colors['orange'],
                    max_title_width=200,
                    theme_mode='preferred',
                    theme_path='/usr/share/icons/Yaru-dark', 
                ),
                widget.TextBox(
                    text='󰥔',
                    foreground=colors['white'],
                    fontsize=18,
                    padding=5,
                ),    
                widget.Clock(
                    format= '%d %b, %H:%M %p',
                    font='Mononoki Nerd Font Bold',
                    fontsize=16,
                    foreground=colors['orange'],
                ),
                widget.Spacer(
                ),
                extrawidgets.StatusNotifier(
                    icon_size=20,
                ),
                widget.TextBox(
                    text='󰌌',
                    fontsize=20,
                    padding=5,
                    foreground=colors['white'],
                ),
                widget.KeyboardLayout(
                configured_keyboards=['us','es'],
                foreground=colors['orange']
                ),
                extrawidgets.ALSAWidget(
                    mode='both',
                    theme_path='/usr/share/icons/Yaru-dark',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    margin=13,
                ),
                 extrawidgets.CurrentLayoutIcon(
                    scale=0.7,
                    use_mask=True,
                    foreground=colors['white'], 
                ),
                widget.TextBox(
                    text='',
                    fontsize=18,
                    padding=9,
                    #margin=13,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("wlogout")},
                )

]
