import xcffib
import xcffib.xproto
import struct

def find_window_by_name(conn, window, name):
    tree = conn.core.QueryTree(window).reply()
    for child in tree.children:
        wm_name = conn.core.GetProperty(False, child, xcffib.xproto.Atom.WM_NAME, xcffib.xproto.Atom.STRING, 0, 100).reply()
        if wm_name.value.buf() == name.encode('utf-8'):
            return child
        found = find_window_by_name(conn, child, name)
        if found:
            return found
    return None

def set_xwayland_scale_for_steam():
    try:
        conn = xcffib.connect()
    except xcffib.ConnectionException as e:
        print(f"Error al conectar al servidor X: {e}")
        return
    
    setup = conn.get_setup()
    screen = setup.roots[0]

    # Definir la escala
    scale = 1  # Cambia esto a la escala que desees aplicar

    # Obtener el ID del átomo
    atom_name = "_XWAYLAND_GLOBAL_OUTPUT_SCALE"
    try:
        atom_reply = conn.core.InternAtom(False, len(atom_name), atom_name).reply()
        atom_id = atom_reply.atom
    except xcffib.xproto.BadAtom as e:
        print(f"Error: {e}")
        return

    if atom_id is None:
        print(f"Warning: no {atom_name} atom, xwayland output scaling not supported")
    else:
        # Buscar la ventana de Steam
        steam_window = find_window_by_name(conn, screen.root, "Steam")

        if steam_window:
            print(f"Setting xwayland scale atom `{atom_id}` to `{scale}` on Steam window `{steam_window}`")

            # Preparar los datos para la propiedad
            data = struct.pack('=I', scale)

            try:
                # Cambiar la propiedad del átomo
                conn.core.ChangeProperty(
                    xcffib.xproto.PropMode.Replace,
                    steam_window,
                    atom_id,
                    xcffib.xproto.Atom.CARDINAL,
                    32,  # El formato es 32 bits por dato
                    1,   # Longitud del dato es 1 (porque sólo empaquetamos un entero)
                    data
                )
                conn.flush()
                print("Propiedad cambiada y comando enviado exitosamente.")
            except xcffib.xproto._errors.XcffibException as e:
                print(f"Error al cambiar la propiedad: {e}")
        else:
            print("No se encontró la ventana de Steam.")

if __name__ == "__main__":
    set_xwayland_scale_for_steam()
