#!/usr/bin/env bash

set -euo pipefail

# Colores para la salida
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Obtener la ruta absoluta del repositorio independientemente de desde dónde se ejecute el script
DOTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TIMESTAMP="$(date +%Y%m%d_%H%M%S)"

clear
echo -e "${CYAN}====================================================================${NC}"
echo -e "${BLUE}                 DESPLEGADOR DE DOTFILES - cr1odots                  ${NC}"
echo -e "${CYAN}====================================================================${NC}"
echo -e " Repositorio local: ${GREEN}${DOTS_DIR}${NC}"
echo -e " Este script creará symlinks en tu directorio de usuario (~/)."
echo -e " Las configuraciones existentes serán respaldadas automáticamente."
echo -e "${CYAN}====================================================================${NC}\n"

read -p "¿Deseas vincular estos dotfiles a tu sistema? [s/N]: " CHOICE

case "$CHOICE" in
  [sS]|[sS][iI])
    echo -e "\n${GREEN}[+] Iniciando el despliegue de dotfiles...${NC}\n"
    ;;
  *)
    echo -e "\n${YELLOW}[!] Operación cancelada por el usuario.${NC}"
    exit 0
    ;;
esac

# Función para enlazar elementos de forma segura creando backup
link_item() {
  local src="$1"
  local target="$2"

  # Crear el directorio padre del destino si no existe
  mkdir -p "$(dirname "$target")"

  if [ -e "$target" ] || [ -L "$target" ]; then
    echo -e " ${YELLOW}[!] Se detectó un archivo/directorio existente en: ${target}${NC}"
    echo -e "     Creando backup en: ${target}.bak.${TIMESTAMP}"
    mv "$target" "${target}.bak.${TIMESTAMP}"
  fi

  ln -sfn "$src" "$target"
  echo -e " ${GREEN}[✔] Enlazado:${NC} ${target} -> ${src}"
}

# 1. Enlazar contenido de config/ hacia ~/.config/
if [ -d "${DOTS_DIR}/config" ]; then
  echo -e "${BLUE}=== Aplicando configuraciones de ~/.config ===${NC}"
  for item in "${DOTS_DIR}/config"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    link_item "$item" "${HOME}/.config/${name}"
  done
  echo ""
fi

# 2. Enlazar contenido de local/ hacia ~/.local/
if [ -d "${DOTS_DIR}/local" ]; then
  echo -e "${BLUE}=== Aplicando archivos de ~/.local ===${NC}"
  for item in "${DOTS_DIR}/local"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    link_item "$item" "${HOME}/.local/${name}"
  done
  echo ""
fi

# 3. Enlazar .emacs.d
if [ -d "${DOTS_DIR}/emacs.d" ]; then
  echo -e "${BLUE}=== Aplicando configuración de Emacs ===${NC}"
  link_item "${DOTS_DIR}/emacs.d" "${HOME}/.emacs.d"
  echo ""
fi

# 4. Enlazar .zshenv
if [ -f "${DOTS_DIR}/.zshenv" ]; then
  echo -e "${BLUE}=== Aplicando .zshenv ===${NC}"
  link_item "${DOTS_DIR}/.zshenv" "${HOME}/.zshenv"
  echo ""
fi

# 5. Enlazar rtorrent.rc
if [ -f "${DOTS_DIR}/rtorrent.rc" ]; then
  echo -e "${BLUE}=== Aplicando configuración de rtorrent ===${NC}"
  link_item "${DOTS_DIR}/rtorrent.rc" "${HOME}/.rtorrent.rc"
  echo ""
fi

# 6. Enlazar misc/ o cache/ opcionales si se desean incluir en ~/.cache
if [ -d "${DOTS_DIR}/cache" ]; then
  echo -e "${BLUE}=== Aplicando directorio cache ===${NC}"
  for item in "${DOTS_DIR}/cache"/*; do
    [ -e "$item" ] || continue
    name="$(basename "$item")"
    link_item "$item" "${HOME}/.cache/${name}"
  done
  echo ""
fi

echo -e "${GREEN}====================================================================${NC}"
echo -e "${GREEN}      ¡Dotfiles vinculados con éxito en tu entorno de usuario!     ${NC}"
echo -e "${GREEN}====================================================================${NC}"
