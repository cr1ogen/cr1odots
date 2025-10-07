from libqtile import bar;
from libqtile.config import Screen
from modules.widgets import primary_widgets
from modules.colors import colors
#from modules.qtilecolors import qtilecolors

screens = [
    Screen(
       # wallpaper = '~/.local/share/backgrounds/revenant.jpg',
       # wallpaper_mode = 'fill',
        top=bar.Bar(primary_widgets,
        size=33,
        opacity=1,
        background='#00000000', #['transparency'],
        margin=[8, 13, 0, 13], 
        ),
    ),
]
