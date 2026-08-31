#!/usr/bin/env bash

# 1. Matar SOLO las aplicaciones de Python de Fabric para no suicidarse
# Usamos -o para asegurarnos de no cerrar este script de Bash actual
pkill -o -f "python3.*fabric"
sleep 0.5

# 2. Definir la ruta base de tus widgets
FABRIC_DIR="$HOME/.config/fabric"

# 3. Encender tus widgets en paralelo (con el '&' al final)
python3 "$FABRIC_DIR/Notificaciones/config.py" &
python3 "$FABRIC_DIR/Calendario/config.py" &
python3 "$FABRIC_DIR/Multimedia/config.py" &

# --- Tus futuros widgets ---
# python3 "$FABRIC_DIR/barra_estado/config.py" &

echo "¡Todos los widgets de Fabric han sido inicializados con éxito!"
