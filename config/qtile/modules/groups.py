from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from .keys import mod, keys

groups = [
    Group(name='1', label="", matches=[
          Match(wm_class='firefox')], layout="monadtall"),
    Group(name='2', label="", layout="monadtall"),
    Group(name='3', label="", layout="monadtall"),
    Group(name='4', label="", matches=[
          Match(wm_class='discord')], layout='monadtall'),
    Group(name='5', label="ﰝ", matches=[
        Match(wm_class='pw-jack ardour')], layout='max'),
    Group(name='6', label="", matches=[
        Match(wm_class='Steam'), Match(wm_class='r2modman'), Match(wm_class='heroic')], layout='monadtall'),

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
        ]
    )
