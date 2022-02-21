# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

## Qtile import ##
import os
import subprocess
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

## Qtile "El Paraguayo" extras import ##

from qtile_extras import widget as extrawidgets

## Llamada de aplicaciones al inicio ##

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


mod = "mod4"
terminal = guess_terminal("kitty")

keys = [
    # Se puede encontrar una lista de los comandos disponibles que se pueden vincular a las teclas
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Cambiar entre ventanas.
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Mover ventanas entre las columnas izquierda/derecha o subir/bajar en la pila actual.
    # Salir del rango en el diseño de Columnas creará una nueva columna.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Crecer ventanas. Si la ventana actual está en el borde de la pantalla y la dirección
    # estará en el borde de la pantalla - la ventana se encogería.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Alternar entre los lados divididos y no divididos de la pila.
    # Dividir = todas las ventanas mostradas
    # Nodividir = 1 ventana mostrada, como el Max layout, pero aun com
    # multiple paneles de pila.
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Alternar entre diferentes layouts como se define a continuación.
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    ## Captura de pantalla ##
    
    Key([], "Print", lazy.spawn("/home/cr1ogen/.config/rofi/bin/menu_screenshot")),

    ## Aplicaciones mas usadas ##
  
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "backslash", lazy.spawn("firefox"), desc="Launch Browser"),
    Key([mod,"shift"], "backslash", lazy.spawn("thunar"), desc="Launch File"),
]

##groups = [Group(i) for i in "123456789"]

groups= [
    Group("1",
          label="WEB",
          ),
    Group("2",
          label="EDIT",
          ),
    Group("3",
          label="PROMPT",
          ),
    Group("4",
          label="DATA",
          ),
    Group("5",
          label="MEDIA",
          ),
    Group("6",
          label="GAME",
          ),
    
    ]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Bsp(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=1, margin=6,),
    layout.Max(),
    layout.Tile(),
    layout.Floating(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrainsMonoExtraBold",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
         wallpaper = '~/Imágenes/Wallpapers/el_gau10.jpg',
        wallpaper_mode = 'fill',

        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='block',
                    active = '#ffffff',
                    inactive = '#ffffff',
                    this_current_screen_border='#ff5722'
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.5,
                ),
                widget.Prompt(),
                widget.TaskList(
                    max_title_width=350,
                    highlight_method='block',
                    border='ff5722',
                    margin_y=1,
                ),
                widget.Clock(format="%m-%d | %H:%H %p"),
                widget.Spacer(),
                extrawidgets.StatusNotifier(
                icon_theme='/usr/share/icons/Numix/',
                ),
                extrawidgets.ALSAWidget(
                    mode='both',
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("pavucontrol")},
                    theme_path='/usr/share/icons/Numix/',
                    margin_y=8,
                ),
                widget.Image(
                    filename='~/.config/qtile/Power.png',
                    mouse_callbacks={'Button1' : lambda: qtile.cmd_spawn("/home/cr1ogen/.config/rofi/bin/menu_powermenu")},
                    margin_y=4,
                ),
            ],
            28,
            margin=[4, 6, 0, 6],
            background='#212121',
            opacity=0.95,
            border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="wlogout"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
