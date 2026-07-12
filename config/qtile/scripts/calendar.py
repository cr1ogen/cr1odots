import sys
import os
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QCalendarWidget
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QGuiApplication

class CalendarioFlotante(QWidget):
    def __init__(self):
        super().__init__()
        # Forzar backend de Wayland
        os.environ["QT_QPA_PLATFORM"] = "wayland"
        
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.init_ui()
        self.posicionar_esquina_derecha()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)

        self.cal = QCalendarWidget()
        self.cal.setGridVisible(False)
        self.cal.setNavigationBarVisible(True)
        layout.addWidget(self.cal)

        # Paleta de colores oscura integrada con el estilo de tu barra
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e2e;
                border: 1px solid #313244;
                border-radius: 12px;
                color: #cdd6f4;
                font-family: 'Segoe UI', sans-serif;
            }
            QCalendarWidget QWidget {
                background-color: #1e1e2e;
                border: none;
            }
            QCalendarWidget QTableView {
                background-color: #11111b;
                border-radius: 8px;
                color: #cdd6f4;
                selection-background-color: #cba6f7;
                selection-color: #11111b;
            }
            QCalendarWidget QMenu {
                background-color: #1e1e2e;
                color: #cdd6f4;
            }
            QAbstractItemView {
                font-size: 12px;
            }
        """)
        self.resize(300, 280)

    def posicionar_esquina_derecha(self):
        # Obtiene la geometría de la pantalla activa para alinearse a la derecha
        pantalla = QGuiApplication.primaryScreen().geometry()
        # Coloca el calendario en la esquina superior derecha dejando margen para tu barra
        x = pantalla.width() - self.width() - 15
        y = 45 # Ajusta este número si tu barra es más gruesa o fina
        self.move(QPoint(x, y))

    # Se auto-destruye si haces clic en cualquier otro lado (comportamiento popup)
    def changeEvent(self, event):
        if event.type() == event.Type.ActivationChange and not self.isActiveWindow():
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cal = CalendarioFlotante()
    cal.show()
    cal.activateWindow()
    sys.exit(app.exec())
