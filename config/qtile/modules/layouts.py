from libqtile import layout
from libqtile.config import Match
from modules.colors import colors

# Setup layout Theme

layout_theme = {
     "border_width":6,
     "margin":14,
     "border_focus":colors['orange'],
     "border_normal":colors['dark'],
     "single_border_width": 3,
 }

layouts = [
    layout.MonadTall(**layout_theme),                   
    layout.Max(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
 float_rules = [
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
      #  Match(wm_class="kitty"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        ],
)
