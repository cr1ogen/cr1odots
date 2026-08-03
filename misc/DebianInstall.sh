#!/usr/bin/env bash

set -euo pipefail

# Colores para la salida en consola
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Iniciando instalación de componentes del sistema ===${NC}\n"

# 1. Verificar si el script se corre con sudo / root
if [ "$EUID" -ne 0 ]; then
  echo -e "${RED}[ERROR] Este script debe ejecutarse como root o con sudo.${NC}"
  exit 1
fi

# Detectar el usuario real y su carpeta home
ACTUAL_USER="${SUDO_USER:-$USER}"
USER_HOME=$(eval echo "~${ACTUAL_USER}")

# 2. Actualizar lista de paquetes
echo -e "${GREEN}[1/5] Actualizando repositorios APT...${NC}"
apt update -y

# 3. Instalación de paquetes de sistema principales
echo -e "${GREEN}[2/5] Instalando paquetes de APT...${NC}"
APT_PACKAGES=(
  git
  gpm
  xdg-utils
  xdg-user-dirs
  xwayland
  wayland-protocols
  wayland-utils
  libwayland-bin
  pkg-config
  python3-pip
  amd64-microcode
  python3-cffi
  python3-cairocffi
  libpangocairo-1.0-0
  python3-xcffib
  python3-setuptools
  libwlroots-0.19
  libwlroots-0.19-dev
  imagemagick
  wlr-randr
  wlogout
  rofi
  nwg-look
  cmake
  meson
  libmpv-dev
  libgirepository-2.0-dev
  socat
  libiw-dev
  pipewire
  pulseaudio-utils
  zsh
  starship
  eza
  grim
  slurp
  libqt6webenginecore6
  python3-pyqt6
  python3-jinja2
  python3-yaml
  python3-pyqt6.qtqml
  python3-pyqt6.qtwebengine
)

apt install -y "${APT_PACKAGES[@]}"

# Instalación de SDDM sin recomendados
echo -e "${GREEN}[+] Instalando SDDM (sin recomendados)...${NC}"
apt install -y --no-install-recommends sddm

# 4. Instalación de dependencias de Qtile via PIP
echo -e "${GREEN}[3/5] Instalando dependencias de Python con PIP...${NC}"
PIP_PACKAGES=(
  dbus-fast
  iwlib
  pulsectl-asyncio
)

python3 -m pip install --break-system-packages "${PIP_PACKAGES[@]}"

# 5. Clonar e instalar Qtile con soporte Wayland
echo -e "${GREEN}[4/5] Clonando e instalando Qtile (backend Wayland)...${NC}"

GIT_DIR="${USER_HOME}/Git"

# Crear directorio Git si no existe
sudo -u "$ACTUAL_USER" mkdir -p "$GIT_DIR"

# Clonar o actualizar el repositorio de Qtile
if [ -d "${GIT_DIR}/qtile/.git" ]; then
  echo -e "${YELLOW}[!] El repositorio Qtile ya existe, actualizando con git pull...${NC}"
  sudo -u "$ACTUAL_USER" git -C "${GIT_DIR}/qtile" pull
else
  sudo -u "$ACTUAL_USER" git clone https://github.com/qtile/qtile.git "${GIT_DIR}/qtile"
fi

# Instalar Qtile usando pip con backend Wayland
cd "${GIT_DIR}/qtile"
pip install --config-setting backend=wayland . --break-system-packages

# 6. Activación de servicios y configuración del entorno de usuario
echo -e "${GREEN}[5/5] Configurando servicios y usuario...${NC}"

# Creación de carpetas de usuario XDG (Downloads, Documents, Pictures, etc.)
if [ "$ACTUAL_USER" != "root" ] && command -v xdg-user-dirs-update &> /dev/null; then
  echo -e "${GREEN}[+] Generando directorios del usuario (${ACTUAL_USER})...${NC}"
  sudo -u "$ACTUAL_USER" xdg-user-dirs-update
fi

# Habilitar SDDM para que arranque de forma predeterminada al reiniciar
if command -v sddm &> /dev/null; then
  echo -e "${GREEN}[+] Habilitando servicio SDDM...${NC}"
  systemctl enable sddm.service
  systemctl set-default graphical.target
fi

# Cambiar la shell predeterminada a Zsh para el usuario
if [ "$ACTUAL_USER" != "root" ] && [ -x "$(command -v zsh)" ]; then
  echo -e "${GREEN}[+] Cambiando shell por defecto a Zsh para ${ACTUAL_USER}...${NC}"
  chsh -s "$(which zsh)" "$ACTUAL_USER" || true
fi

echo -e "\n${BLUE}=== ¡Instalación de Qtile, carpetas de usuario y paquetes completada con éxito! ===${NC}"
echo -e "${YELLOW}Podés reiniciar con 'sudo reboot' para ingresar a través de SDDM.${NC}"
