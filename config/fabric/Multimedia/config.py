import os
import sys
import socket
import subprocess
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.image import Image
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import invoke_repeater, get_relative_path
from gi.repository import GLib, GdkPixbuf

# Puerto local exclusivo para la comunicación del widget multimedia
PUERTO_MULTIMEDIA = 14243

class MediaWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="media-card",
            spacing=14,
            orientation="h",
            **kwargs
        )

        text_box = Box(orientation="v", spacing=4, v_align="center", h_expand=True)
        
        self.title_label = Label(label="Nada", name="media-title", ellipsization="end", h_align="start")
        self.artist_label = Label(label="Desconocido", name="media-artist", ellipsization="end", h_align="start")
        
        text_box.add(self.title_label)
        text_box.add(self.artist_label)

        self.cover_image = Image(
            icon_name="audio-x-generic",
            name="media-cover"
        )
        self.cover_image.set_pixel_size(80)

        self.add(self.cover_image)
        self.add(text_box)


class MediaWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",
            title="fabric-media",
            anchor="top right",
            margin="120px 20px 0px 0px",
            exclusivity="none",
            pass_through=True,
            visible=False,
            all_visible=False,
            **kwargs
        )
        
        self.set_visual(self.get_screen().get_rgba_visual())
        self.set_app_paintable(True)
        
        self.widget_interior = MediaWidget()
        self.add(self.widget_interior)
        self.show_all()
        self.hide()

        invoke_repeater(1000, self.comprobar_multimedia)

    def obtener_dato_player(self, comando):
        try:
            return subprocess.check_output(["playerctl", "metadata", "--format", comando]).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            return ""

    def toggle_visibilidad(self):
        # Alterna la ventana de forma manual al recibir el clic de Qtile
        if self.get_visible():
            self.set_visible(False)
        else:
            self.set_visible(True)
            self.present()

    def comprobar_multimedia(self):
        try:
            estado = subprocess.check_output(["playerctl", "status"]).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            estado = "Stopped"

        if estado == "Playing":
            titulo = self.obtener_dato_player("{{title}}") or "Título Desconocido"
            artista = self.obtener_dato_player("{{artist}}") or "Artista Desconocido"
            url_portada = self.obtener_dato_player("{{mpris:artUrl}}")

            self.widget_interior.title_label.set_label(titulo)
            self.widget_interior.artist_label.set_label(artista)

            if url_portada and "file://" in url_portada:
                ruta_limpia = url_portada.replace("file://", "")
                if os.path.exists(ruta_limpia):
                    try:
                        pixbuf = GdkPixbuf.Pixbuf.new_from_file(ruta_limpia)
                        pixbuf_escalado = pixbuf.scale_simple(80, 80, GdkPixbuf.InterpType.BILINEAR)
                        self.widget_interior.cover_image.set_from_pixbuf(pixbuf_escalado)
                    except Exception:
                        self.widget_interior.cover_image.set_from_icon_name("audio-x-generic", 80)
            else:
                self.widget_interior.cover_image.set_from_icon_name("audio-x-generic", 80)

            # Auto-despliegue inicial solo si la música acaba de arrancar
            # (No forzamos si el usuario la ocultó manualmente con el clic)
            pass
        else:
            if self.get_visible():
                self.set_visible(False)
        
        return True


# --- MOTOR DE ESCUCHA DE COMANDOS EN SEGUNDO PLANO ---
def arrancar_servidor_escucha(window):
    def servidor():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind(("127.0.0.1", PUERTO_MULTIMEDIA))
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
    # Si Qtile manda 'toggle', actúa como cliente rápido
    if len(sys.argv) > 1 and sys.argv[1] == "toggle":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(("127.0.0.1", PUERTO_MULTIMEDIA))
            s.sendall(b"toggle")
            s.close()
        except ConnectionRefusedError:
            pass
        sys.exit(0)

    app = Application("media-widget")
    
    window = MediaWindow()
    app.add_window(window)
    arrancar_servidor_escucha(window)

    ruta_estilos = get_relative_path("./style.css")
    if os.path.exists(ruta_estilos):
        app.set_stylesheet_from_file(ruta_estilos)
        
    app.run()
