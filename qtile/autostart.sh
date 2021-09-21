#!/bin/sh
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
xrandr -s 3840x2160 --output DP-2 --scale 0.5x0.5 &
#csd-xsettings &
sxhkd &
nitrogen --restore &
picom --experimental-backends &
nm-applet &
pasystray &
greenclip daemon &
dunst &
wal -R &		
