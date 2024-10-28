import os
import subprocess
from libqtile import qtile
from qtile_extras import widget #as extrawidgets #Extras
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration

from modules.colors import colors
#from modules.qtilecolors import colors

widget_defaults = dict(
    font="Mononoki Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

decoration_group = {
    "decorations": [
        RectDecoration (colour='#00000000', use_widget_background=True, radius=15, filled=True, group=True, clip=True , ignore_extrawidth=True)
    ],
}
        
decoration_border = {
    "decorations": [
        RectDecoration (colour='#00000000',line_colour='#ffffff', line_width=3,use_widget_background=True, radius=15, filled=True, group=True, clip=True , ignore_extrawidth=True)        
    ],
}


primary_widgets = [
                widget.TextBox(
                    #text='',
                    text='Debian',
                    fontsize=15,
                    #foreground=colors[9],
                    font='Mononoki Nerd Fonts Bold',
                    padding=14,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
                    **decoration_border,
                    line_colour='#ffffff',
                    line_width=4,
                    background=colors[3],
                    ),
                 widget.TextBox(
                    text='',
                    fontsize=21,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("kitty")},
                    ),
                 widget.TextBox(
                    text='󰈹',
                    fontsize=24,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("firefox")},
                    ),
                 widget.TextBox(
                    text='󰓓',
                    fontsize=24,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("steam")},
                    ),
                 widget.TextBox(
                     text='',
                    fontsize=20,
                    padding=10,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")},
                    ),
                 widget.Sep(
                    padding=12,
                    foreground='#00000000',#transparency
                    ),
                 widget.CurrentLayout(
                     font="Mononoki Nerd Font",
                     fontsize=16,
                     padding=14,
                     **decoration_group,
                     background=colors[6],
                    ), 
                 widget.TaskList(
                    font="Mononoki Nerd Font",
                    fontsize=16,
                    icon_size=20,
                    padding=6,
                    highlight_method='text',
                    border=colors[8],
                    title_width_method='uniform',
                    theme_mode='preferred',
                    spacing=-2,
                    borderwidth=1,
                    max_title_width=100,
                ),
                widget.Spacer(
                ),
                widget.GroupBox(
                    font="Mononoki Nerd Font",
                    fontsize=24,
                    padding=10,
                    center_aligned=True,
                    highlight_method='text',
                    #block_highlight_text_color=colors['dark'],
                    highlight_color=colors[4], #['orange'],
                    inactive=colors[7], #['white'],
                    active=colors[9], #['orange'],
                    this_current_screen_border=colors[2], #['orange'],
                    this_screen_border=colors[4], #['orange'],
                    other_current_screen_border=colors[0], #['orange'],
                    other_screen_border=colors[6], #['orange'],
                    urgent_border=colors[4], #['orange'],
                    rounded=True,
                    disable_drag=True,
                    **decoration_group,
                    background=colors[3],
                ),    
                widget.Spacer(
                ),
                widget.TextBox(
                    text='󰌌',
                    fontsize=20,
                    padding=8,
                    **decoration_group,
                    background=colors[6],
                ),
                widget.KeyboardLayout(
                    configured_keyboards=['us','es'],
                    padding=14,
                    **decoration_group,
                    background=colors[6],
                ),
                widget.Sep(
                    padding=14,
                    foreground='#00000000', #transparency
                ),
                widget.PulseVolumeExtra(
                    mode='icon',
                    theme_path='/usr/share/icons/BeautyLine/',
                    bar_width=50,
                    bar_height=75,
                    channel='Master',
                    icon_size=22,
                    padding=14,
                    volume_down_command='XF86AudioLowerVolume',
                    volume_up_command='XF86AudioRaiseVolume',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    **decoration_group,
                    background=colors[6],
                    ),
                    widget.Sep(
                        padding=14,
                        background=colors[6], 
                        foreground='#00000000', #transparency
                        **decoration_group
                        ),
                    widget.Sep(
                        padding=14,
                        foreground='#00000000', #transparency
                        ),
                        
                    widget.TextBox(
                        text='',
                        fontsize=16,
                        padding=8,
                        **decoration_group,
                        background=colors[6],
                    ),
                    widget.Net(
                        format='{interface}',
                        interface='enp5s0',
                        fontsize=16,
                        padding=14,
                        **decoration_group,
                        background=colors[6],
                    ),    
                    widget.StatusNotifier(
                    icon_theme='/usr/share/icons/BeautyLine',
                    icon_size=24,
                    highlight_colour=colors[0], 
                    #padding=4,
                    show_menu_icons=True,
                    #**decoration_group,
                        
                    ),
               widget.TextBox(
                    text='',
                    fontsize=20,
                    #margin=13,
                    padding=14,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("/home/cr1ogen/.local/bin/waypaper")},
                    #**decoration_group,
                    ),
                widget.TextBox(
                    text='',
                    fontsize=20,
                    foreground='#ffffff',
                    #margin=13,
                    padding=14,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("wlogout")},
                    #**decoration_group,
                    ),
                widget.Clock(
                    format= '%H:%M %a',
                    font='Mononoki Nerd Font Bold',
                    fontsize=16,
                    padding=14,
                    **decoration_border,
                    background=colors[3],
                    ),
    ]

             
