#!/bin/sh

#volumeicon &

#scale in X11
xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.75 &

# Share screen with pipewire hack
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user stop  xdg-desktop-portal xdg-desktop-portal-wlr &

exec /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &

#feh --bg-scale ~/Imágenes/Wallpapers/city.jpeg &
#mpvpaper -f -o "loop" DP-2 /home/cr1ogen/Imágenes/Videowall/video.mp4 &
#/usr/bin/emacs --daemon &
dunst &
#conky-startup &
