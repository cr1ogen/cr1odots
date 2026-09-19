#!/bin/sh

#scale in X11
xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.35 &

# Share screen with pipewire hack
dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots &
systemctl --user stop  xdg-desktop-portal xdg-desktop-portal-wlr &

/usr/libexec/xfce-polkit &

#/usr/bin/easyeffects --gapplication-service

# Setup Wallpaper and update colors (waypaper --restore colgado por bug screeninfo/xrandr, se usa mpvpaper directo)
WALL=$(cat "$HOME/.cache/qtile_dotfiles/current_wallpaper" 2>/dev/null || echo "$HOME/Imágenes/wallpapers/wallhaven-rqe7q7.png")
mpvpaper --fork -o "input-ipc-server=/tmp/mpv-socket-DP-3 loop panscan=1.0 --mute=yes" DP-3 "$WALL" &
~/.config/qtile/scripts/wallpaper.sh "$WALL" >> /tmp/wallpaper.log 2>&1 &

openrgb --startminimized &
