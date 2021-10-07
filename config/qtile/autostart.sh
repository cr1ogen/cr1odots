#!/bin/sh
#lxpolkit &
/usr/lib/x86_64-linux-gnu/polkit-mate/polkit-mate-authentication-agent-1 &
xrandr -s 3840x2160 --output DP-2 --scale 0.5x0.5 &
picom --experimental-backends &
nm-applet & 
pasystray &
dunst &
wal -R &		
