#!/bin/sh

#scale in X11
xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.70 &

# Share screen with pipewire hack
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user stop  xdg-desktop-portal xdg-desktop-portal-wlr &

exec  /usr/libexec/xfce-polkit &

dunst &
#/usr/bin/easyeffects --gapplication-service

# Setup Wallpaper and update colors

waypaper --restore &

openrgb --startminimized &
