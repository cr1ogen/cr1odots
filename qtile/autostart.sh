#!/bin/sh
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
csd-xsettings &
xscreensaver --no-splash &
nitrogen --restore &
/usr/bin/dunst &
picom --experimental-backends &
