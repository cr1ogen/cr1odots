import os
import sys
import socket
import subprocess
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import get_relative_path, invoke_repeater
from gi.repository import GLib

# Puerto local exclusivo para el widget de redes
PUERTO_REDES = 14244

class NetworkWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="network-card",
            spacing=14,
            orientation="v",
            **kwargs
        )

        # --- SECCIÓN 1: ESTADO ACTUAL ---
        status_box = Box(orientation="h", spacing=12, v_align="center")
        
        self.icon_label = Label(label="NET", name="network-icon", v_align="center")
        
        text_box = Box(orientation="v", spacing=2, v_align="center")
        self.ssid_label = Label(label="Desconectado", name="network-ssid", h_align="start")
        self.ip_label = Label(label="Sin IP", name="network-ip", h_align="start")
        text_box.add(self.ssid_label)
        text_box.add(self.ip_label)

        # Interruptor de texto claro [ON] / [OFF]
        self.toggle_wifi_btn = Button(
            label="ON", 
            name="network-toggle-btn", 
            v_align="center", 
            h_align="end",
            on_clicked=lambda *_: self.alternar_estado_hardware_wifi()
        )

        status_box.add(self.icon_label)
        status_box.add(text_box)
        status_box.add(self.toggle_wifi_btn)
        self.add(status_box)

        # --- SECCIÓN 2: LISTA DE REDES ---
        self.list_title = Label(label="Redes Disponibles:", name="network-list-title", h_align="start")
        self.add(self.list_title)

        self.wifi_list_box = Box(orientation="v", spacing=6, name="network-list")
        self.add(self.wifi_list_box)

        invoke_repeater(5000, self.actualizar_todo)
        self.actualizar_todo()

    def ejecutar_comando(self, comando):
        try:
            return subprocess.check_output(comando, shell=True, timeout=1.5).decode("utf-8").strip()
        except Exception:
            return ""

    def alternar_estado_hardware_wifi(self):
        estado_actual = self.ejecutar_comando("nmcli radio wifi")
        if estado_actual == "enabled":
            subprocess.Popen(["nmcli", "radio", "wifi", "off"])
            self.toggle_wifi_btn.set_label("OFF")
        else:
            subprocess.Popen(["nmcli", "radio", "wifi", "on"])
            self.toggle_wifi_btn.set_label("ON")
        GLib.timeout_add(800, self.actualizar_todo)

    def conectar_a_red(self, ssid_destino):
        subprocess.Popen(["nmcli", "device", "wifi", "connect", ssid_destino])
        self.ssid_label.set_label("Conectando...")
        GLib.timeout_add(1500, self.actualizar_todo)

    def actualizar_todo(self):
        # 1. Forzamos a NetworkManager a escanear el aire en segundo plano de fondo
        subprocess.Popen(["nmcli", "device", "wifi", "rescan"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        # 2. Buscar la IP de la interfaz inalámbrica real filtrando puentes virtuales
        ip = self.ejecutar_comando("ip -4 addr show | grep -E 'inet .* (wlan|wlp|wlo)' | awk '{print $2}' | cut -d/ -f1 | head -n 1")
        if not ip:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.connect(("8.8.8.8", 80))
                ip = s.getsockname()[0]
                s.close()
            except Exception:
                ip = ""

        radio_wifi = self.ejecutar_comando("nmcli radio wifi")
        if radio_wifi == "disabled":
            self.ssid_label.set_label("Wi-Fi Desactivado")
            self.ip_label.set_label("Usa el botón para encender")
            self.icon_label.set_label("OFF")
            self.toggle_wifi_btn.set_label("OFF")
            for child in self.wifi_list_box.get_children():
                self.wifi_list_box.remove(child)
            return True

        self.toggle_wifi_btn.set_label("ON")

        # 3. Buscamos el SSID activo directamente desde el dispositivo inalámbrico real (independiente del idioma)
        ssid_activo = self.ejecutar_comando("nmcli -t -f DEVICE,CONNECTION device | grep -E '^(wlan|wlp|wlo)' | cut -d':' -f2")
        if ssid_activo == "--" or not ssid_activo: 
            ssid_activo = ""

        if ssid_activo:
            self.ssid_label.set_label(ssid_activo)
            self.ip_label.set_label(ip if ip else "Conectado")
            self.icon_label.set_label("WIFI")
        else:
            ethernet_real = self.ejecutar_comando("nmcli dev | grep -E '^e(nt|lp|p)' | grep 'conectado'")
            if ethernet_real:
                self.ssid_label.set_label("Cableada")
                self.icon_label.set_label("ETH")
            else:
                self.ssid_label.set_label("Desconectado")
                self.icon_label.set_label("DIS")
            self.ip_label.set_label(ip if ip else "Sin internet")

        # 4. Escaneamos redes a la redonda
        salida_redes = self.ejecutar_comando("nmcli -t -f ssid dev wifi | sort -u | grep -v '^$' | head -n 5")
        
        for child in self.wifi_list_box.get_children():
            self.wifi_list_box.remove(child)

        if salida_redes:
            for red in salida_redes.split("\n"):
                if not red or red == ssid_activo:
                    continue
                
                btn = Button(
                    label=f"  {red}", 
                    name="network-item-btn",
                    h_align="start",
                    on_clicked=lambda *_, r=red: self.conectar_a_red(r)
                )
                self.wifi_list_box.add(btn)
        
        self.wifi_list_box.show_all()
        return True


class NetworkWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",
            title="fabric-network",
            anchor="top right",
            margin="45px 12px 0px 0px",
            exclusivity="none",
            pass_through=False,
            visible=False,
            all_visible=False,
            **kwargs
        )
        
        self.set_visual(self.get_screen().get_rgba_visual())
        self.set_app_paintable(True)
        
        self.widget_interior = NetworkWidget()
        self.add(self.widget_interior)
        self.show_all()
        self.hide()

    def toggle_visibilidad(self):
        if self.get_visible():
            self.set_visible(False)
        else:
            self.set_visible(True)
            self.present()


def arrancar_servidor_escucha(window):
    def servidor():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", PUERTO_REDES))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                data = conn.recv(1024).decode().strip()
                if data == "toggle":
                    GLib.idle_add(window.toggle_visibilidad)
                conn.close()
        except Exception:
            pass

    import threading
    threading.Thread(target=servidor, daemon=True).start()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "toggle":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", PUERTO_REDES))
            s.sendall(b"toggle")
            s.close()
        except ConnectionRefusedError:
            pass
        sys.exit(0)

    app = Application("network-widget")
    
    window = NetworkWindow()
    app.add_window(window)
    arrancar_servidor_escucha(window)

    ruta_estilos = get_relative_path("./style.css")
    if os.path.exists(ruta_estilos):
        app.set_stylesheet_from_file(ruta_estilos)
        
    app.run()
