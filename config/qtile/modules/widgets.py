import os
import subprocess
from libqtile import qtile
from libqtile import widget
from qtile_extras import widget as extrawidgets #Extras

widget_defaults = dict(
    font="JetBrainsMonoExtraBold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
                widget.GroupBox(
                fontsize=26,
                highlight_method='text',
                ),
                widget.Prompt(
                ),
                widget.TaskList(
                    highlight_method='text',
                    max_title_width=200,
                ),
                widget.Clock(
                    format="%b  %d %H:%M %p",
                    font='JetBrains bold',
                ),
                widget.Spacer(
                ),
                extrawidgets.StatusNotifier(
                ),
                extrawidgets.ALSAWidget(
                    mode='icon',
                    theme_path='/home/cr1ogen/.local/share/icons/McMuse-orange-dark',
                ),
                 widget.CurrentLayoutIcon(
                    scale=0.5,
                    custom_icon_paths=["/home/cr1ogen/.config/qtile/layout-icons/gruvbox-neutral_orange"],
                ),

]
