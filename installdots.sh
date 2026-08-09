#!/usr/bin/env bash

set -euo pipefail

# Colores para la salida
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Obtener la ruta absoluta del repositorio
DOTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

clear
echo -e "${CYAN}====================================================================${NC}"
echo -e "${BLUE}                   COPIADOR DE DOTFILES - cr1odots                    ${NC}"
echo -e "${CYAN}====================================================================${NC}"
echo -e " Repositorio local: ${GREEN}${DOTS_DIR}${NC}"
echo -e " Este script COPIARÁ las configuraciones a tu directorio personal (~/)."
echo -e " Preservará permisos y respaldará archivos existentes."
echo -e "${CYAN}====================================================================${NC}\n"

read -p "¿Deseas copiar estos dotfiles a tu sistema? [s/N]: " CHOICE

case "$CHOICE" in
  [sS]|[sS][iI])
    echo -e "\n${GREEN}[+] Iniciando la copia de dotfiles...${NC}\n"
    ;;
  *)
    echo -e "\n${YELLOW}[!] Operación cancelada por el usuario.${NC}"
    exit 0
    ;;
esac

# Función para copiar elementos de forma segura creando backup o fusionando directorios
copy_item() {
  local src="$1"
  local target="$2"

  # Crear el directorio padre del destino si no existe
  mkdir -p "$(dirname "$target")"

  # Si el destino es un directorio y el origen también, se fusionan (evita borrar carpetas como ~/.local/share/fonts)
  if [ -d "$src" ] && [ -d "$target" ]; then
    echo -e " ${BLUE}[i] Fusionando directorio existente:${NC} ${target}"
    cp -rp "$src"/* "$target"/ 2>/dev/null || true
    echo -e " ${GREEN}[✔] Contenido fusionado exitosamente en:${NC} ${target}"
  else
    # Si existe un archivo individual o enlace, se hace backup
    if [ -e "$target" ] || [ -L "$target" ]; then
      echo -e " ${YELLOW}[!] Se detectó un archivo existente en: ${target}${NC}"
      echo -e "     Creando backup en: ${target}.bak.${TIMESTAMP}"
      mv "$target" "${target}.bak.${TIMESTAMP}"
    fi

    # Preserva atributos originales con cp -rp
    cp -rp "$src" "$target"
    echo -e " ${GREEN}[✔] Copiado:${NC} ${src} -> ${target}"
  fi
}

# 1. Copiar contenido de config/ hacia ~/.config/
if [ -d "${DOTS_DIR}/config" ]; then
  echo -e "${BLUE}=== Copiando configuraciones a ~/.config ===${NC}"
  for item in "${DOTS_DIR}/config"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    copy_item "$item" "${HOME}/.config/${name}"
  done
  echo ""
fi

# 2. Copiar contenido de local/ hacia ~/.local/
if [ -d "${DOTS_DIR}/local" ]; then
  echo -e "${BLUE}=== Copiando archivos a ~/.local ===${NC}"
  for item in "${DOTS_DIR}/local"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    copy_item "$item" "${HOME}/.local/${name}"
  done
  echo ""
fi

# 3. Copiar .emacs.d
if [ -d "${DOTS_DIR}/emacs.d" ]; then
  echo -e "${BLUE}=== Copiando configuración de Emacs ===${NC}"
  copy_item "${DOTS_DIR}/emacs.d" "${HOME}/.emacs.d"
  echo ""
fi

# 4. Copiar .zshenv
if [ -f "${DOTS_DIR}/.zshenv" ]; then
  echo -e "${BLUE}=== Copiando .zshenv ===${NC}"
  copy_item "${DOTS_DIR}/.zshenv" "${HOME}/.zshenv"
  echo ""
fi

# 5. Copiar rtorrent.rc
if [ -f "${DOTS_DIR}/rtorrent.rc" ]; then
  echo -e "${BLUE}=== Copiando configuración de rtorrent ===${NC}"
  copy_item "${DOTS_DIR}/rtorrent.rc" "${HOME}/.rtorrent.rc"
  echo ""
fi

# 6. Copiar cache/ opcional
if [ -d "${DOTS_DIR}/cache" ]; then
  echo -e "${BLUE}=== Copiando directorio cache ===${NC}"
  for item in "${DOTS_DIR}/cache"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    copy_item "$item" "${HOME}/.cache/${name}"
  done
  echo ""
fi

# =====================================================================
# Ajuste global de permisos de ejecución
# =====================================================================
echo -e "${BLUE}=== Ajustando permisos de ejecución ===${NC}"

# 1. Todo lo que esté en ~/.local/bin pasa a ser ejecutable
if [ -d "${HOME}/.local/bin" ]; then
  find "${HOME}/.local/bin" -type f -exec chmod +x {} +
  echo -e " ${GREEN}[✔] Permisos +x aplicados a todo en ~/.local/bin${NC}"
fi

# 2. Todos los scripts .sh o .py en ~/.config pasan a ser ejecutables
if [ -d "${HOME}/.config" ]; then
  find "${HOME}/.config" -type f \( -name "*.sh" -o -name "*.py" \) -exec chmod +x {} +
  echo -e " ${GREEN}[✔] Permisos +x aplicados a scripts (.sh, .py) en ~/.config${NC}"
fi

# 3. Cualquier carpeta llamada 'scripts' o 'bin' dentro de ~/.config
find "${HOME}/.config" -type d \( -name "scripts" -o -name "bin" \) -exec find {} -type f -exec chmod +x {} + 2>/dev/null || true

# Regenerar la caché de fuentes por si se agregó algo nuevo
fc-cache -fv &>/dev/null || true

echo -e "\n${GREEN}====================================================================${NC}"
echo -e "${GREEN}    ¡Dotfiles copiados y permisos asignados correctamente! ${NC}"
echo -e "${GREEN}====================================================================${NC}"
