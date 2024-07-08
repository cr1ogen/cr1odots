import os
import subprocess
from libqtile import qtile
#from libqtile import widget
from qtile_extras import widget #as extrawidgets #Extras
from qtile_extras.widget.decorations import RectDecoration

from modules.colors import colors

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration(colour=colors['orange'], radius=6, filled=True, padding_y=4, group=True)
    ],
    "padding": 10,
}

primary_widgets = [
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    fontsize=16,
                    #margin=-2,
                    center_aligned=True,
                    highlight_method='text',
                    highlight_color=colors['orange'],
                    this_current_screen_border=colors['white'],
                    inactive=colors['white'],
                    **decoration_group,
                ),
                    widget.CurrentLayoutIcon(
                    scale=0.7,
                    use_mask=True,
                    foreground=colors['white'], 
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
                    #foreground=colors['white'],
                    fontsize=18,
                    **decoration_group,
                ),    
                widget.Clock(
                    format= '%d %b, %H:%M %p',
                    font='Mononoki Nerd Font Bold',
                    fontsize=16,
                    foreground=colors['white'],
                    **decoration_group,
                ),
                widget.Spacer(
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
                    widget.StatusNotifier(
                    icon_theme='/usr/share/icons/Yaru/scalable',
                    icon_size=20,
                    **decoration_group,
                    ),
                widget.Volume(
                    #mode='icon',
                    #theme_path='/usr/share/icons/Yaru-dark',
                    channel='Master',
                    fontsize=18,
                    emoji=True,
                    emoji_list=['🔇', '🔈', '🔉', '🔊'],
                    volume_down_command='XF86AudioLowerVolume',
                    volume_up_command='XF86AudioRaiseVolume',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    #**decoration_group,
                    #margin=13,
                ),
                widget.TextBox(
                    text='',
                    fontsize=18,
                    padding=9,
                    #margin=13,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("wlogout")},
                )

]
