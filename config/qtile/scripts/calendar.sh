#!/usr/bin/env bash

# Ruta absoluta a tu archivo QML (ajustala si es necesario)
QML_PATH="/home/cr1ogen/.config/quickshell/calendar.qml"

# Si QuickShell ya está ejecutando este calendario, lo cierra
if pgrep -f "qs --path $QML_PATH" > /dev/null; then
    pkill -f "qs --path $QML_PATH"
    exit 0
fi

# Si no está abierto, lo lanza en segundo plano
qs --path "$QML_PATH" &
