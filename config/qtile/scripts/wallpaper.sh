#!/usr/bin/env bash

# Variables de entorno y rutas limpias de ML4W
IMAGE_PATH=""
NOTIFICATIONS=false
CACHE_FOLDER="$HOME/.cache/qtile_dotfiles"
CACHE_FILE="$CACHE_FOLDER/current_wallpaper"
BLURRED_WALLPAPER="$CACHE_FOLDER/blurred_wallpaper.png"
SQUARE_WALLPAPER="$CACHE_FOLDER/square_wallpaper.png"
RASI_FILE="$CACHE_FOLDER/current_wallpaper.rasi"

# Configuraciones de Blur
SETTINGS_BLUR="$HOME/.local/bin/blur.sh"
BLUR="50x30"
if [ -f "$SETTINGS_BLUR" ]; then
    BLUR=$(cat "$SETTINGS_BLUR")
fi

# Colores para la salida de la consola
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

info() { echo -e "${GREEN}[INFO]${NC} $1" >&2; }
error() { echo -e "${RED}[ERROR]${NC} $1" >&2; }

# Validamos que Waypaper le haya pasado la ruta de la imagen como argumento al script
if [[ $# -eq 0 ]]; then
    echo "Uso: $0 /ruta/a/la/imagen.jpg"
    exit 1
fi
IMAGE_PATH="$1"

if [[ ! -f "$IMAGE_PATH" ]]; then
    error "La imagen enviada por Waypaper no existe en -> $IMAGE_PATH"
    exit 1
fi

if [ ! -d "$CACHE_FOLDER" ]; then
    mkdir -p "$CACHE_FOLDER"
fi

# Guardamos la ruta en el historial de caché de ML4W
echo "$IMAGE_PATH" > "$CACHE_FILE"

# --- DETECTAR TEMA (MODO OSCURO / CLARO) ---
SETTINGS_FILE="$HOME/.config/gtk-3.0/settings.ini"
THEME_PREF=1
if [ -f "$SETTINGS_FILE" ]; then
    THEME_PREF=$(grep -E '^gtk-application-prefer-dark-theme=' "$SETTINGS_FILE" | awk -F'=' '{print $2}')
fi

# Determinar la ruta real del binario de Matugen
if [ -f "$HOME/.cargo/bin/matugen" ]; then
    MATUGEN_BIN="$HOME/.cargo/bin/matugen"
elif [ -f "$HOME/.local/bin/matugen" ]; then
    MATUGEN_BIN="$HOME/.local/bin/matugen"
else
    MATUGEN_BIN="matugen"
fi

# --- EJECUTAR MATUGEN CORREGIDO ---
# Reemplazamos '--scheme' por '-t' para evitar el fallo 'unexpected argument'
if [ "$THEME_PREF" -eq 1 ] || [ -z "$THEME_PREF" ]; then
    $MATUGEN_BIN image "$IMAGE_PATH" -t scheme-content -m "dark" --source-color-index 0
else
    $MATUGEN_BIN image "$IMAGE_PATH" -t scheme-content -m "light" --source-color-index 0
fi
info "Matugen actualizó tu plantilla de colores con éxito"

# --- RECARGA COMPATIBLE CON WAYLAND ---
# Cambiado de 'restart' (que se rompe en Wayland) a 'reload_config'
qtile cmd-obj -o cmd -f reload_config
info "Configuración de Qtile recargada en caliente"

# --- RECARGA DE APLICACIONES ---
killall -q nautilus nemo pavucontrol

 --- FORZAR EL MOTOR HÍBRIDO COMPATIBLE ---
# Esto obliga a Nemo (GTK3) y Nautilus (GTK4) a usar el mismo motor de renderizado
gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'
gsettings set org.gnome.desktop.interface gtk-theme 'adw-gtk3-dark'

# --- RECARGA DE APLICACIONES ---
killall -q nautilus nemo pavucontrol


killall -q nautilus nemo
info "Entorno de Nautilus refrescado"

# --- RECARGAR COMPLEMENTOS DE NAVEGADOR ---
if type pywalfox >/dev/null 2>&1; then
    pywalfox update
    info "Pywalfox actualizado"
fi

# --- CACHÉ DE RENDERIZADO (Para Rofi o menús de ML4W) ---
if type magick >/dev/null 2>&1; then
    magick "$IMAGE_PATH" -resize 75% "$BLURRED_WALLPAPER"
    if [ ! "$BLUR" == "0x0" ]; then
        magick "$BLURRED_WALLPAPER" -blur "$BLUR" "$BLURRED_WALLPAPER"
    fi
    magick "$IMAGE_PATH" -gravity Center -extent 1:1 "$SQUARE_WALLPAPER"
    
    echo "* { current-image: url(\"$BLURRED_WALLPAPER\", height); }" > "$RASI_FILE"
    info "Caché de Rofi (.rasi) escrita correctamente"
fi




info "¡Proceso de sincronización de colores finalizado!"
exit 0
