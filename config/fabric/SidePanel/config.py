"""side panel example, contains info about the system (Official Layout Version - Text Percentages)"""

import os
import sys
import time
import socket
import psutil
from loguru import logger
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay
from fabric.widgets.datetime import DateTime
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import invoke_repeater, get_relative_path
from gi.repository import GLib

# Puerto local exclusivo
PUERTO_SIDEPANEL = 14246

def get_profile_picture_path() -> str | None:
    path = os.path.expanduser("~/Imágenes/face.png")
    if not os.path.exists(path):
        path = os.path.expanduser("~/.face")
    if not os.path.exists(path):
        logger.warning(
            "can't fetch a user profile picture, add a profile picture image at ~/.face or at ~/Pictures/Other/profile.jpg"
        )
        path = None
    return path


class SidePanel(Window):
    @staticmethod
    def bake_progress_bar(name: str = "progress-bar", size: int = 64, **kwargs):
        return CircularProgressBar(
            name=name, min_value=0, max_value=100, size=size, **kwargs
        )

    @staticmethod
    def bake_progress_icon(**kwargs):
        return Label(**kwargs).build().add_style_class("progress-icon").unwrap()

    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",
            title="fabric-sidepanel",
            anchor="top right",
            margin="60px 18px 10px 0px",
            exclusivity="none",
            visible=False,
            all_visible=False,
            **kwargs,
        )

        self.set_visual(self.get_screen().get_rgba_visual())
        self.set_app_paintable(True)

        self.profile_pic = Box(
            name="profile-pic",
            style=f'background-image: url("file://{get_profile_picture_path() or ""}")',
        )
        self.uptime_label = Label(label=f"{self.get_current_uptime()}")

        self.header = Box(
            spacing=14,
            name="header",
            orientation="h",
            children=[
                self.profile_pic,
                Box(
                    orientation="v",
                    children=[
                        DateTime(
                            name="date-time",
                            style="margin-top: 4px; min-width: 180px;",
                        ),
                        self.uptime_label,
                    ],
                ),
            ],
        )

        # Saludo limpio sin el cero de antes
        self.greeter_label = Label(
            label=f"Good {'Morning' if time.localtime().tm_hour < 12 else 'Afternoon'}, {os.getlogin()}!",
            style="font-size: 20px;",
        )

        # Inicialización oficial de las barras originales
        self.cpu_progress = self.bake_progress_bar()
        self.ram_progress = self.bake_progress_bar()
        self.disk_progress = self.bake_progress_bar().build().set_value(42).unwrap()

        # !!! NUEVO !!! Etiquetas de texto fijas para ver los números abajo de los círculos
        self.cpu_text_label = Label(label="0%", style="font-size: 13px; font-weight: bold; margin-top: 4px;")
        self.ram_text_label = Label(label="0%", style="font-size: 13px; font-weight: bold; margin-top: 4px;")
        self.disk_text_label = Label(label="0%", style="font-size: 13px; font-weight: bold; margin-top: 4px;")

        self.progress_container = Box(
            name="progress-bar-container",
            spacing=12,
            children=[
                # Columna de CPU
                Box(
                    orientation="v",
                    children=[
                        Overlay(
                            child=self.cpu_progress,
                            overlays=[self.bake_progress_icon(label="", style="margin-right: 8px; text-shadow: 0 0 10px #fff, 0 0 10px #fff, 0 0 10px #fff;")],
                        ),
                        self.cpu_text_label
                    ]
                ),
                Box(name="progress-bar-sep"),
                # Columna de RAM
                Box(
                    orientation="v",
                    children=[
                        Overlay(
                            child=self.ram_progress,
                            overlays=[self.bake_progress_icon(label="", style="margin-right: 4px; text-shadow: 0 0 10px #fff;")],
                        ),
                        self.ram_text_label
                    ]
                ),
                Box(name="progress-bar-sep"),
                # Columna de Disco Principal
                Box(
                    orientation="v",
                    children=[
                        Overlay(
                            child=self.disk_progress,
                            overlays=[self.bake_progress_icon(label="󰋊", style="margin-right: 0px; text-shadow: 0 0 10px #fff, 0 0 18px #fff;")],
                        ),
                        self.disk_text_label
                    ]
                ),
            ],
        )

        self.add(
            Box(
                name="window-inner",
                orientation="v",
                spacing=24,
                children=[self.header, self.greeter_label, self.progress_container],
            ),
        )
        
        self.update_status()
        
        invoke_repeater(
            15 * 60 * 1000,
            lambda: (self.uptime_label.set_label(self.get_current_uptime()), True),
        )
        invoke_repeater(1000, self.update_status)

        self.show_all()
        GLib.idle_add(self.hide)

    def toggle_visibilidad(self):
        if self.get_mapped():
            self.set_visible(False)
        else:
            self.set_visible(True)
            self.present()

    def update_status(self):
        # 1. Calculamos las estadísticas reales
        cpu_val = psutil.cpu_percent()
        ram_val = psutil.virtual_memory().percent
        disk_val = psutil.disk_usage('/').percent

        # 2. Llenamos los anillos elásticos
        self.cpu_progress.value = cpu_val
        self.ram_progress.value = ram_val
        self.disk_progress.value = disk_val
        
        # 3. !!! NUEVO !!! Actualizamos los numeritos de texto en vivo cada 1 segundo
        self.cpu_text_label.set_label(f"{int(cpu_val)}%")
        self.ram_text_label.set_label(f"{int(ram_val)}%")
        self.disk_text_label.set_label(f"{int(disk_val)}%")
        
        return True

    def get_current_uptime(self):
        uptime = time.time() - psutil.boot_time()
        uptime_days, remainder = divmod(uptime, 86400)
        uptime_hours, remainder = divmod(remainder, 3600)
        return f"{int(uptime_days)} {'days' if uptime_days > 1 else 'day'}, {int(uptime_hours)} {'hours' if uptime_hours > 1 else 'hour'}"


def arrancar_servidor_escucha(window):
    def servidor():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", PUERTO_SIDEPANEL))
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
            s.connect(("127.0.0.1", PUERTO_SIDEPANEL))
            s.sendall(b"toggle")
            s.close()
        except ConnectionRefusedError:
            pass
        sys.exit(0)

    app = Application("side-panel")
    side_panel = SidePanel()
    app.add_window(side_panel)
    arrancar_servidor_escucha(side_panel)
    app.set_stylesheet_from_file(get_relative_path("./style.css"))
    app.run()
