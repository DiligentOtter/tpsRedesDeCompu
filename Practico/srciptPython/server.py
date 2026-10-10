import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 12000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind((HOST, PORT))
servidor.listen(1)

print(f"[servidor TCP] escuchando en {HOST}:{PORT} ...")

conexion, direccion_cliente = servidor.accept()
print(f"[servidor TCP] conexión aceptada desde {direccion_cliente[0]}:{direccion_cliente[1]}")

datos = conexion.recv(1024)
mensaje = datos.decode("utf-8", errors="replace")
print(f"[servidor TCP] recibido ({len(datos)} bytes): {mensaje!r}")

respuesta = f"Recibido: {mensaje}"
conexion.sendall(respuesta.encode("utf-8"))
print(f"[servidor TCP] respuesta enviada: {respuesta!r}")

while conexion.recv(1024):
    pass

print("[servidor TCP] el cliente cerró la conexión")
conexion.close()
servidor.close()