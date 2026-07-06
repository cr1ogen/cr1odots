# 🌌 cr1odots - Qtile Desktop Environment

Bienvenido a **cr1odots**, mi repositorio personal de archivos de configuración (dotfiles). Este espacio contiene mi entorno de escritorio personalizado basado en el gestor de ventanas **Qtile**, diseñado para ser estético, funcional y altamente dinámico.


---

## 📸 Screenshots

Aquí puedes ver cómo luce el entorno actualmente:

![241013_21-10-26](https://github.com/user-attachments/assets/c4722547-6c28-4832-8978-f73b2be2b4bc)



<p align="center">
  <img src="screenshot.png" alt="Qtile Showcase" width="85%"/>
</p>

*(Próximamente añadiré más capturas mostrando el funcionamiento de los temas y componentes interactivos).*

---

## 🎨 Características Principales

*   **Window Manager:** [Qtile](https://qtile.org) (personalizado con Python).
*   **Esquema de Colores Dinámico:** Generación automática de paletas mediante [Matugen](https://github.com) a partir del fondo de pantalla actual.
*   **Integración GTK Extendida:** Compatibilidad total de colores automáticos para aplicaciones **GTK-3** y **GTK-4**.
*   **Pruebas Activas:** Implementación experimental de widgets y componentes visuales usando [Quickshell](https://hyprland.org).

---

## 🛠️ En Desarrollo (Área de Pruebas)

Actualmente me encuentro desarrollando y testeando nuevos scripts interactivos basados en **Quickshell** con la ayuda de Inteligencia Artificial (AI). El objetivo es reemplazar componentes tradicionales de la barra y notificaciones con interfaces de usuario nativas y fluidas basadas en QML.

---

## 📦 Dependencias Requeridas (Debian Based)

Para que todas las funciones de este entorno corran correctamente en **Debian**, asegúrate de instalar las siguientes herramientas:

### Sistema Base
*   `qtile` - El gestor de ventanas principal (instalado vía `apt` o mediante `pip` en un entorno virtual).

### Estética y Colores Dinámicos
*   `matugen` - Generador de paletas de colores de nueva generación (instalado generalmente vía `cargo` o descargando el binario oficial).
*   `waypaper` - Interfaz gráfica para la gestión y selección de fondos de pantalla.
*   `mpvpaper` - Motor backend utilizado por Waypaper para reproducir e inyectar videos como fondos de pantalla animados.

### Componentes de Interfaz e Innovación
*   `quickshell` - Entorno de ejecución para los nuevos scripts y widgets QML interactivos (compilado desde fuente o mediante binarios oficiales).
*   `rofi` - Lanzador de aplicaciones.
*   `kitty` - Emulador de terminal por defecto.

---

## ⌨️ Atajos de Teclado Principales (Keybindings)

A continuación se listan las combinaciones de teclas por defecto configuradas en este entorno (`Mod` corresponde generalmente a la tecla `Super` / `Windows`):

| Combinación | Acción |
| :--- | :--- |
| `Mod + Enter` | Abrir la terminal por defecto |
| `Mod + R` | Lanzar el menú de aplicaciones (Rofi) |
| `Mod + Q` | Cerrar la ventana enfocada actualmente |
| `Mod + Control + R` | Reiniciar Qtile por completo (Recargar configs) |
| `Mod + Control + Q` | Salir de la sesión de Qtile |
| `Mod + Espacio` | Cambiar entre los diferentes layouts de ventanas |
| `Mod + [Flechas / HJKL]` | Cambiar el foco entre ventanas abiertas |
| `Mod + Shift + [Flechas]` | Desplazar o mover ventanas de posición |

---

## 📥 Instalación

Puedes clonar este repositorio directamente en tu carpeta de configuraciones:

```bash
git clone https://github.com ~/.config/qtile
```

*Nota: Se recomienda respaldar tu configuración previa antes de sustituir los archivos.*

---

## 🤝 Créditos y Agradecimientos

Este proyecto no sería posible sin el increíble trabajo de la comunidad de Linux y código abierto. Quiero dar una mención especial y agradecer a:

*   **Stephan Raabe ([ML4W](https://mylinuxforwork.com)):** Por servir de base e inspiración con su excelente script `wallpaper.sh` para la gestión y cambio dinámico de fondos de pantalla.
*   **end-4 ([dots-hyprland](https://github.com/end-4)):** Por la excelente plantilla de generación de colores de Matugen, la cual utilizo para tematizar automáticamente las interfaces **GTK-3** y **GTK-4**.
*   **Mi Asistente de IA:** Por la colaboración continua en la estructura, lógica y depuración de los nuevos scripts de Quickshell.

---
Mantenido con 💻 por [cr1ogen](https://github.com).
