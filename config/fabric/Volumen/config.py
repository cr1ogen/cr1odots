import os
from typing import cast
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.audio.service import Audio
from fabric.utils import invoke_repeater, get_relative_path
from gi.repository import GLib

# Importamos tu animador local
from animator import Animator

# --- CLASE DE LA BARRA CIRCULAR ANIMADA DE LA WIKI ---
class AnimatedCircularProgressBar(CircularProgressBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.animator = Animator(
            bezier_curve=(0.34, 1.56, 0.64, 1.0),
            duration=0.3,
            min_value=self.min_value,
            max_value=self.value,
            tick_widget=self,
            notify_value=lambda p, *_: self.set_value(p.value),
        )

    def animate_value(self, value: float):
        self.animator.pause()
        self.animator.min_value = self.value
        self.animator.max_value = value
        self.animator.play()


# --- WIDGET CONTENEDOR DEL VOLUMEN ---
class AnimatedVolumeWidget(Box):
    def __init__(self, **kwargs):
        super().__init__(
            name="volume-card",
            orientation="v",
            v_align="center",
            h_align="center",
            **kwargs
        )

        self.audio = Audio()
        self.timeout_id = None

        # La barra de progreso circular contendrá al icono directamente en su interior
        self.progress_bar = AnimatedCircularProgressBar(
            name="volume-progress",
            min_value=0,
            max_value=100,
            value=0,
            size=80, # Tamaño ideal
            v_align="center",
            h_align="center"
        )

        # Icono NerdFont limpio
        self.icon_label = Label(
            label="  ", 
            name="volume-icon",
            v_align="center",
            h_align="center"
        )

        # Metemos el icono DIRECTAMENTE dentro de la barra circular
        self.progress_bar.add(self.icon_label)
        self.add(self.progress_bar)

        # Escuchamos los cambios del sistema
        self.audio.connect("speaker-changed", self.al_cambiar_volumen)

        # Carga inicial
        if self.audio.speaker:
            self.progress_bar.set_value(self.audio.speaker.volume)

    def al_cambiar_volumen(self, *args):
        if not self.audio.speaker: 
            return
            
        volumen_actual = self.audio.speaker.volume
        self.progress_bar.animate_value(volumen_actual)

        if volumen_actual == 0 or self.audio.speaker.muted:
            self.icon_label.set_label("  ")
        elif volumen_actual < 50:
            self.icon_label.set_label("  ")
        else:
            self.icon_label.set_label("  ")

        window = self.get_toplevel()
        if window and hasattr(window, "show"):
            window.show_all()

        if self.timeout_id:
            GLib.source_remove(self.timeout_id)
        
        self.timeout_id = GLib.timeout_add(2000, self.ocultar_ventana)

    def ocultar_ventana(self):
        window = self.get_toplevel()
        if window and hasattr(window, "hide"):
            window.hide()
        self.timeout_id = None
        return False


# --- VENTANA CON TRANSPARENCIA NATIVA ---
class VolumeWindow(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="overlay",
            title="fabric-volume",
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
        
        self.widget_volumen = AnimatedVolumeWidget()
        self.add(self.widget_volumen)


if __name__ == "__main__":
    app = Application("volume-widget")
    
    ruta_estilos = get_relative_path("./style.css")
    if os.path.exists(ruta_estilos):
        app.set_stylesheet_from_file(ruta_estilos)
        
    window = VolumeWindow()
    app.add_window(window)
    app.run()
