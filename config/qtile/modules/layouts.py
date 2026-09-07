from libqtile import layout
from qtile_extras.layout.decorations import RoundedCorners
from libqtile.config import Match
from modules.colors import colors

# Setup layout Theme

# 1. Decoración para la ventana enfocada
borde_enfocado = RoundedCorners(
    #corner_radius=180,
    #border_width=6,
    colour=colors["primary"]
)

# 2. Decoración para las ventanas inactivas
borde_normal = RoundedCorners(
    #corner_radius=180,
    #border_width=6,
    colour=colors["surface_highest"] # Mismo radio y grosor, cambia el color
)

layout_theme = {
     "border_width":6,
     "margin":16,
     #"border_focus":colors["primary"], #['orange'],
     "border_focus": borde_enfocado,
     "border_normal": borde_normal,  
     #"border_normal":colors["surface_highest"], #['dark'],
     "single_border_width": 8,
 }

layouts = [
    layout.MonadTall(**layout_theme),                   
    layout.Max(**layout_theme),
    layout.MonadWide(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    **layout_theme,
    float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="kitty"),
        Match(wm_class="org.gnome.Nautilus"),
        Match(wm_class="com.saivert.pwvucontrol"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="waypaper"),
        Match(wm_class="xfce-polkit"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        ],
)
