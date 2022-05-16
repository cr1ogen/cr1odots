import os
import subprocess
from libqtile import qtile
from libqtile import widget
from qtile_extras import widget as extrawidgets #Extras

widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
                widget.GroupBox(
                fontsize=28,
                padding=7,
                highlight_method='text',
                ),
                widget.Prompt(
                ),
                widget.TaskList(
                    font="JetBrainsMono Nerd Font",
                    highlight_method='text',
                    max_title_width=200,
                ),
                widget.Clock(
                    format="%b  %d %H:%M %p",
                    font='JetBrainsMono Nerd Font Bold',
                    fontsize=14,
                ),
                widget.Spacer(
                ),
                extrawidgets.StatusNotifier(
                icon_size=22,
                ),
                extrawidgets.ALSAWidget(
                    mode='icon',
                    theme_path='/home/cr1ogen/.local/share/icons/BeautyLine',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                ),
                 widget.CurrentLayoutIcon(
                    scale=0.7,
                    custom_icon_paths=["/home/cr1ogen/.config/qtile/layout-icons/gruvbox-neutral_orange"],
                ),

]
