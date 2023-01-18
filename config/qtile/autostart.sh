#!/bin/sh

#volumeicon &

#scale in X11
xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.75 &

exec /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &

#feh --bg-scale ~/Imágenes/Wallpapers/city.jpeg &
#mpvpaper -f -o "loop" DP-2 /home/cr1ogen/Imágenes/Videowall/video.mp4 &
#/usr/bin/emacs --daemon &
dunst &
#conky-startup &
