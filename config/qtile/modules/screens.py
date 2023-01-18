from libqtile import bar;
from libqtile.config import Screen
from modules.widgets import primary_widgets
from modules.colors import colors

screens = [
    Screen(
        wallpaper = '~/.local/share/backgrounds/flare.jpg',
        wallpaper_mode = 'fill',
        top=bar.Bar(primary_widgets,
        size=26,
        opacity=1,
        background=colors['dark'],
        border_width=[6, 0, 0, 0],  # Draw top and bottom borders
        ),
    ),
]
