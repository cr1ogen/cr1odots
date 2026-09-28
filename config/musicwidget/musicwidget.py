#!/usr/bin/env python3
"""Panel flotante de música para Wayland (gtk-layer-shell, Gtk3).

Lee el reproductor vía playerctl: carátula, título, artista, álbum,
progreso y botones anterior / play-pausa / siguiente.
Primera ejecución lo muestra, las siguientes (o --toggle) muestran/ocultan.
Click derecho oculta, --hide inicia oculto, --quit lo cierra.
"""

import argparse
import os
import signal
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
gi.require_version("GtkLayerShell", "0.1")
gi.require_version("GLibUnix", "2.0")

from gi.repository import Gtk, Gdk, GtkLayerShell, GLib, GLibUnix, GdkPixbuf

RUNTIME_DIR = os.environ.get("XDG_RUNTIME_DIR", "/tmp")
PIDFILE = os.path.join(RUNTIME_DIR, "musicwidget.pid")
COVER_SIZE = 110
BASE_DIR = Path(__file__).parent


def playerctl(*args):
    try:
        out = subprocess.run(
            ["playerctl"] + list(args),
            capture_output=True, text=True, timeout=3,
        )
        if out.returncode != 0:
            return None
        return out.stdout.strip()
    except Exception:
        return None


def art_to_path(art_url):
    if not art_url:
        return None
    if art_url.startswith("file://"):
        return unquote(urlparse(art_url).path)
    return None


class MusicWidget(Gtk.Window):
    def __init__(self):
        super().__init__(title="musicwidget")
        GtkLayerShell.init_for_window(self)
        GtkLayerShell.set_layer(self, GtkLayerShell.Layer.TOP)
        GtkLayerShell.set_anchor(self, GtkLayerShell.Edge.TOP, True)
        GtkLayerShell.set_margin(self, GtkLayerShell.Edge.TOP, 50)
        GtkLayerShell.set_exclusive_zone(self, 0)
        GtkLayerShell.set_keyboard_mode(
            self, GtkLayerShell.KeyboardMode.NONE
        )
        GtkLayerShell.set_namespace(self, "musicwidget")
        self.set_decorated(False)
        self.set_skip_taskbar_hint(True)
        self.set_keep_below(True)
        self.stick()
        self.add_events(Gdk.EventMask.BUTTON_PRESS_MASK)
        self.connect("button-press-event", self.on_click)
        self.connect("destroy", self.on_destroy)

        css = Gtk.CssProvider()
        try:
            css.load_from_path(str(BASE_DIR / "style.css"))
            Gtk.StyleContext.add_provider_for_screen(
                Gdk.Screen.get_default(),
                css,
                Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION,
            )
        except Exception:
            pass

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=12)
        box.set_border_width(12)
        self.add(box)

        self.cover = Gtk.Image()
        self.cover.set_size_request(COVER_SIZE, COVER_SIZE)
        box.pack_start(self.cover, False, False, 0)

        right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        box.pack_start(right, True, True, 0)

        self.title = Gtk.Label()
        self.title.set_use_markup(True)
        self.title.set_halign(Gtk.Align.START)
        self.title.set_ellipsize(3)  # PANGO_ELLIPSIZE_END
        self.title.set_max_width_chars(38)
        right.pack_start(self.title, False, False, 0)

        self.artist = Gtk.Label()
        self.artist.set_use_markup(True)
        self.artist.set_halign(Gtk.Align.START)
        self.artist.set_ellipsize(3)
        self.artist.set_max_width_chars(38)
        right.pack_start(self.artist, False, False, 0)

        self.album = Gtk.Label()
        self.album.set_use_markup(True)
        self.album.set_halign(Gtk.Align.START)
        self.album.set_ellipsize(3)
        self.album.set_max_width_chars(38)
        right.pack_start(self.album, False, False, 0)

        self.progress = Gtk.ProgressBar()
        self.progress.set_show_text(True)
        right.pack_start(self.progress, False, False, 4)

        btns = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        btns.set_halign(Gtk.Align.CENTER)
        right.pack_start(btns, False, False, 0)

        for icon, cmd in [
            ("media-skip-backward", ["previous"]),
            ("media-playback-start", ["play-pause"]),
            ("media-skip-forward", ["next"]),
        ]:
            btn = Gtk.Button()
            btn.set_image(
                Gtk.Image.new_from_icon_name(icon, Gtk.IconSize.BUTTON)
            )
            btn.set_relief(Gtk.ReliefStyle.NONE)
            btn.connect("clicked", self.on_media_button, cmd)
            btns.pack_start(btn, False, False, 0)

        self._cover_path = object()  # fuerza primera carga
        self.update()
        GLib.timeout_add(1000, self.update)

    def on_media_button(self, _btn, cmd):
        playerctl(*cmd)
        self.update()

    def on_click(self, _widget, event):
        if event.button == 3:
            self.hide()
        return True

    def on_destroy(self, _widget):
        try:
            os.unlink(PIDFILE)
        except OSError:
            pass
        Gtk.main_quit()

    def quit_gracefully(self):
        self.destroy()
        return False

    def toggle_visible(self):
        if self.is_visible():
            self.hide()
        else:
            self.update()
            self.show_all()
        return True

    @staticmethod
    def fmt_time(seconds):
        seconds = max(0, int(seconds))
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"

    def update(self):
        try:
            status = playerctl("status")
            if not status:
                self.title.set_markup(
                    '<span font="JetBrainsMono Nerd Font 11"><b>♪ sin reproductor</b></span>'
                )
                self.artist.set_text("")
                self.album.set_text("")
                self.progress.set_fraction(0.0)
                self.progress.set_text("")
                return True

            meta = playerctl(
                "metadata",
                "--format",
                "{{artist}}|{{title}}|{{album}}|{{mpris:length}}|{{mpris:artUrl}}",
            ) or "||||"
            artist, title, album, length, art = meta.split("|", 4)
            icon = "⏸" if status == "Playing" else "▶"
            self.title.set_markup(
                f'<span font="JetBrainsMono Nerd Font 11"><b>{icon} {GLib.markup_escape_text(title or "?")}</b></span>'
            )
            self.artist.set_markup(
                f'<span font="JetBrainsMono Nerd Font 10">{GLib.markup_escape_text(artist or "?")}</span>'
            )
            self.album.set_markup(
                f'<span font="JetBrainsMono Nerd Font 10" foreground="#aaaaaa">{GLib.markup_escape_text(album or "")}</span>'
            )

            try:
                total = int(length) / 1e6
            except (TypeError, ValueError):
                total = 0
            try:
                pos = float(playerctl("position") or 0)
            except (TypeError, ValueError):
                pos = 0
            if total > 0:
                self.progress.set_fraction(min(pos / total, 1.0))
                self.progress.set_text(
                    f"{self.fmt_time(pos)} / {self.fmt_time(total)}"
                )
            else:
                self.progress.set_fraction(0.0)
                self.progress.set_text(self.fmt_time(pos))

            path = art_to_path(art)
            if path != self._cover_path:
                self._cover_path = path
                if path:
                    try:
                        pix = GdkPixbuf.Pixbuf.new_from_file_at_size(
                            path, COVER_SIZE, COVER_SIZE
                        )
                        self.cover.set_from_pixbuf(pix)
                    except Exception:
                        self.cover.clear()
                else:
                    self.cover.clear()
        except Exception as exc:
            self.title.set_text(f"MUS -- ({exc})")
        return True


def running_pid():
    try:
        with open(PIDFILE) as f:
            pid = int(f.read().strip())
        os.kill(pid, 0)
        return pid
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Panel de música (toggle)")
    parser.add_argument("--toggle", action="store_true",
                        help="muestra/oculta la instancia en ejecución")
    parser.add_argument("--hide", action="store_true",
                        help="inicia oculto (para autostart)")
    parser.add_argument("--quit", action="store_true",
                        help="cierra la instancia en ejecución")
    args = parser.parse_args()

    pid = running_pid()
    if args.quit:
        if pid:
            os.kill(pid, signal.SIGTERM)
        return
    if pid:
        os.kill(pid, signal.SIGUSR1)
        return
    # Sin instancia en ejecución: arrancar (visible, u oculto con --hide).
    # Así el primer click siempre muestra algo.

    win = MusicWidget()
    with open(PIDFILE, "w") as f:
        f.write(str(os.getpid()))
    GLibUnix.signal_add(
        GLib.PRIORITY_DEFAULT, signal.SIGUSR1, win.toggle_visible
    )
    GLibUnix.signal_add(
        GLib.PRIORITY_DEFAULT, signal.SIGTERM, win.quit_gracefully
    )
    if not args.hide:
        win.show_all()
    Gtk.main()


if __name__ == "__main__":
    sys.exit(main())
