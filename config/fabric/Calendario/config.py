import os
import sys
import socket
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.image import Image
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import get_relative_path
from gi.repository import Gtk, GLib

PUERTO_CALENDARIO = 14242

class CalendarWidget(Box):
    def __init__(self, window_parent, **kwargs):
        super().__init__(
            name="calendar-card",
            orientation="v",
            spacing=10,
            v_align="center",
            h_align="center",
            **kwargs
        )

        # --- COMPONENTE DE CALENDARIO NATIVO ---
        self.calendar = Gtk.Calendar()
        self.calendar.set_name("gtk-calendar")
        self.calendar.set_property("show-heading", True)
        self.calendar.set_property("show-day-names", True)

        self.add(self.calendar)


class CalendarWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",            # Capa estándar segura
            title="fabric-calendar",
            anchor="top right",
            margin="45px 12px 0px 0px", # Justo debajo de tu barra de Qtile
            exclusivity="none",
            pass_through=False,
            visible=False,              # Arranca totalmente oculto
            all_visible=False,
            **kwargs
        )
        
        self.set_visual(self.get_screen().get_rgba_visual())
        self.set_app_paintable(True)
        
        # Le pasamos "self" al widget para que el botón pueda controlar la ventana
        self.widget_interior = CalendarWidget(window_parent=self)
        self.add(self.widget_interior)
        self.show_all()
        self.hide()

    def toggle_visibilidad(self):
        if self.get_visible():
            self.set_visible(False)
        else:
            self.set_visible(True)
            self.present()


# --- SERVIDOR DE COMANDOS EN SEGUNDO PLANO ---
def arrancar_servidor_escucha(window):
    def servidor():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", PUERTO_CALENDARIO))
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
    # !!! EL ORDEN CORRECTO !!!
    # Primero validamos si el usuario mandó la palabra 'toggle'.
    # Si es así, actúa como cliente rápido, envía el paquete y se cierra de inmediato
    if len(sys.argv) > 1 and sys.argv[1] == "toggle":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", PUERTO_CALENDARIO))
            s.sendall(b"toggle")
            s.close()
        except ConnectionRefusedError:
            print("[Calendario] El servidor principal no está encendido en segundo plano.")
        sys.exit(0)

    # Si se ejecuta normal (sin argumentos), inicializa la aplicación base
    app = Application("fabric-calendar")
    
    window = CalendarWindow()
    app.add_window(window)
    arrancar_servidor_escucha(window)

    ruta_estilos = get_relative_path("./style.css")
    if os.path.exists(ruta_estilos):
        app.set_stylesheet_from_file(ruta_estilos)

    app.run()
