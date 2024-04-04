#!/bin/sh

#scale in X11
xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.75 &

# Share screen with pipewire hack
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user stop  xdg-desktop-portal xdg-desktop-portal-wlr &

exec /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &

mpvpaper -vfs -o "loop" DP-3 /home/cr1ogen/.local/share/backgrounds/live/Ninja.mp4 &
dunst &
