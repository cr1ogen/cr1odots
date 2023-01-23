from libqtile import bar;
from libqtile.config import Screen
from modules.widgets import primary_widgets
from modules.colors import colors

screens = [
    Screen(
        wallpaper = '~/.local/share/backgrounds/resto.png',
        wallpaper_mode = 'fill',
        top=bar.Bar(primary_widgets,
        size=26,
        opacity=1,
        background=colors['dark'],
        margin=[8, 13, 0, 13], 
        ),
    ),
]
