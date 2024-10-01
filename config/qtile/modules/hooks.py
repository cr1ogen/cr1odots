import os
import subprocess
import time
from libqtile import qtile
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

