from libqtile import layout
from libqtile.config import Match
from modules.colors import colors

layouts = [
    layout.MonadTall(
        border_focus=colors['orange'],
        border_width=6,
        margin=14,
                   ),
    layout.Floating(
        border_focus=colors['orange'],
        border_normal=colors['orange'],
        border_width=6,
        max_border_width=6,
                   ),
    layout.Max(),
    layout.Spiral(
        border_focus=colors['orange'],
        main_pane='bottom',
        border_width=6,
                   ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="Kitty"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        ],
)
