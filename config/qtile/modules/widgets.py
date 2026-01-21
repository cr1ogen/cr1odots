import os
import subprocess
from libqtile import qtile
from qtile_extras import widget #as extrawidgets #Extras
from qtile_extras.widget.decorations import BorderDecoration, RectDecoration, PowerLineDecoration
from modules.colors import colors

widget_defaults = dict(
    font="Poppins",
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
                    fontsize=18,
                    #foreground=colors[9],
                    font='Poppins Bold',
                    padding=14,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show drun")},
                    **decoration_border,
                    line_colour='#ffffff',
                    line_width=4,
                    background=colors[3],
                    ),
                 widget.TextBox(
                    text='',
                    fontsize=22,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("kitty")},
                    ),
                 widget.TextBox(
                    text='󰈹',
                    fontsize=25,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("firefox")},
                    ),
                 widget.TextBox(
                    text='󰓓',
                    fontsize=25,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("steam")},
                    ),
                 widget.TextBox(
                     text='',
                    fontsize=21,
                    padding=10,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("thunar")},
                    ),
                 widget.Sep(
                    padding=12,
                    foreground='#00000000',#transparency
                    ),
                 widget.CurrentLayout(
                     font="Poppins",
                     fontsize=16,
                     padding=14,
                     **decoration_group,
                     background=colors[6],
                    ), 
                 widget.TaskList(
                    font="Poppins",
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
                    font="Poppins",
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
                    fontsize=22,
                    padding=6,
                    **decoration_group,
                    background=colors[6],
                ),
                widget.KeyboardLayout(
                    configured_keyboards=['us','es'],
                    font='Poppins',
                    fontsize=16,
                    padding=6,
                    **decoration_group,
                    background=colors[6],
                ),
                widget.Sep(
                    padding=12,
                    foreground='#00000000', #transparency
                ),
                widget.PulseVolumeExtra(
                    mode='icon',
                    theme_path='/home/cr1ogen/.local/share/icons/BeautyLine',
                    icon_theme='BeautyLine',
                    bar_width=50,
                    bar_height=75,
                    channel='Master',
                    icon_size=22,
                    padding=14,
                    volume_down_command='XF86AudioLowerVolume',
                    volume_up_command='XF86AudioRaiseVolume',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pwvucontrol")},
                    **decoration_group,
                    background=colors[6],
                    ),
                widget.Sep(
                    padding=12,
                    background=colors[6], 
                    foreground='#00000000', #transparency
                    **decoration_group
                ),
                widget.Sep(
                    padding=6,
                    foreground='#00000000', #transparency
                ),
                        
                    #widget.TextBox(
                     #   text='',
                     #   fontsize=18,
                     #   padding=8,
                     #   **decoration_group,
                     #   background=colors[6],
                     #),
                widget.Bluetooth(
                    default_text='{connected_devices}',
                    font='Poppins',
                    fontsize=26,
                    padding=6,
                    icon_theme='/usr/share/icons/BeautyLine',
                    ),    
                widget.WiFiIcon(
                    format='{interface}',
                    interface='wlp15s0',
                    font='Poppins',
                    fontsize=16,
                    padding=6,
                    wifi_shape='arc',
                    wifi_arc=75,
                        #**decoration_group,
                        #background=colors[6],
                ),
                widget.StatusNotifier(
                    icon_theme='/usr/share/icons/BeautyLine',
                    icon_size=26,
                    highlight_colour=colors[0], 
                    #padding_y=2,
                    show_menu_icons=True,
                    padding=6,
                    #**decoration_group,
                    ),
               widget.GithubNotifications(
                   icon_size=22,
                   active_colour='#ff6532',
                   inactive_colour='#ffffff',
                   token_file='/home/cr1ogen/.config/qtile/scripts/github.token',
                   update_interval=150,
                   padding=8,
               ),
               widget.TextBox(
                    text='',
                    fontsize=22,
                    #margin=13,
                    padding=9,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("/usr/local/bin/waypaper")},
                    #**decoration_group,
               ),
                widget.TextBox(
                    text='',
                    fontsize=22,
                    foreground='#ffffff',
                    #margin=13,
                    padding=14,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("wlogout")},
                    #**decoration_group,
                ),
                widget.Clock(
                    format= '%H:%M %a',
                    font='Poppins Bold',
                    fontsize=18,
                    padding=14,
                    **decoration_border,
                    background=colors[3],
                ),
    ]

             
