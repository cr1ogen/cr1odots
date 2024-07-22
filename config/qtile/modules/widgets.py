import os
import subprocess
from libqtile import qtile
from qtile_extras import widget #as extrawidgets #Extras
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration

from modules.colors import colors

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
                widget.Image(
                    filename='/home/cr1ogen/.config/qtile/icons/qtile.png',
                    scale='True',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},

                    ),
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    fontsize=12,
                    padding=9,
                    center_aligned=True,
                    highlight_method='text',
                    #block_highlight_text_color=colors['dark'],
                    highlight_color=colors['orange'],
                    inactive=colors['white'],
                    active=colors['orange'],
                    this_current_screen_border=colors['orange'],
                    this_screen_border=colors['orange'],
                    other_current_screen_border=colors['orange'],
                    other_screen_border=colors['orange'],
                    urgent_border=colors['orange'],
                    rounded=True,
                    disable_drag=True,
                ),
                    widget.CurrentLayoutIcon(
                    scale=0.7,
                    use_mask=True,
                    foreground=colors['white'], 
                ),
                widget.TaskList(
                    font="Mononoki Nerd Font",
                    fontsize=16,
                    icon_size=20,
                    margin=3,
                    highlight_method='text',
                    foreground=colors['white'],
                    border=colors['orange'],
                    max_title_width=200,
                    theme_mode='preferred',
                    #theme_path='/usr/share/icons/candy-icons', 
                ),
                widget.TextBox(
                    text='󰥔',
                    #foreground=colors['white'],
                    fontsize=18,
                ),
                widget.Clock(
                    format= '%d %b, %H:%M %p',
                    font='Mononoki Nerd Font Bold',
                    fontsize=16,
                    foreground=colors['white'],
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
                    foreground=colors['white'],
                ),
                    widget.StatusNotifier(
                        icon_theme='/usr/share/Papirus',
                    icon_size=20,
                    highlight_colour=colors['orange'],
                        show_menu_icons=True,
                    ),
                widget.PulseVolumeExtra(
                    mode='both',
                    theme_path='/home/cr1ogen/.local/share/icons/Gently-Color-Dark-Icons/',
                    bar_width=50,
                    bar_height=75,
                    channel='Master',
                    icon_size=22,
                    volume_down_command='XF86AudioLowerVolume',
                    volume_up_command='XF86AudioRaiseVolume',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},

                ),
                widget.TextBox(
                    text='',
                    fontsize=24,
                    padding=9,
                    #margin=13,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("wlogout")},
                )

]
