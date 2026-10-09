#!/bin/sh

#scale in X11
#xrandr --output DisplayPort-2 --scale 0.60 &

#scale in wayland
wlr-randr --output DP-3 --scale 1.35 &

# Portales: no hacer restart incondicional (provocó timeout 23:02:34 y pérdida de seat/input).
# Solo asegurar que estén activos, sincrónico y sin & para evitar carrera con Qtile.
#dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP=wlroots
#systemctl --user is-active --quiet xdg-desktop-portal xdg-desktop-portal-wlr || systemctl --user start xdg-desktop-portal xdg-desktop-portal-wlr

/usr/libexec/xfce-polkit &

#/usr/bin/easyeffects --gapplication-service

# Setup Wallpaper and update colors (restaura último elegido, sin waypaper)
WALL=$(cat "$HOME/.cache/qtile_dotfiles/current_wallpaper" 2>/dev/null || echo "$HOME/Imágenes/wallpapers/wallhaven-rqe7q7.png")
"$HOME/.local/bin/mpv-wall" set "$WALL" >> /tmp/mpv-wall.log 2>&1 &

openrgb --startminimized &
