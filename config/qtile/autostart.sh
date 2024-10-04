#!/bin/sh

#volumeicon &

#scale in X11
xrandr --output DisplayPort-3 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-4 --scale 1.60 &

# Share screen with pipewire hack
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user stop  xdg-desktop-portal xdg-desktop-portal-wlr &

exec /usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &


dunst &
/usr/bin/easyeffects --gapplication-service

# Setup Wallpaper and update colors

swww-daemon &
~/.config/qtile/scripts/wallpaper.sh init
