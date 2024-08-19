import xcffib
import xcffib.xproto
import struct

def set_xwayland_scale():
    # Conectar al servidor X
    try:
        conn = xcffib.connect()
    except xcffib.ConnectionException as e:
        print(f"Error al conectar al servidor X: {e}")
        return
    
    setup = conn.get_setup()
    screen = setup.roots[0]

    # Definir la escala
    scale = 1

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
        window_id = screen.root

        print(f"Setting xwayland scale atom `{atom_id}` to `{scale}` on root window `{window_id}`")

        # Preparar los datos para la propiedad
        data = struct.pack('=I', scale)

        try:
            # Cambiar la propiedad del átomo
            conn.core.ChangeProperty(
                xcffib.xproto.PropMode.Replace,
                window_id,
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

if __name__ == "__main__":
    set_xwayland_scale()
