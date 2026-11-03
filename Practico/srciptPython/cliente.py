import socket
import sys

SERVER_IP = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
MENSAJE = sys.argv[2] if len(sys.argv) > 2 else "Hola desde mi programa"
SERVER_PORT = 12000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.settimeout(5)

try:
    cliente.connect((SERVER_IP, SERVER_PORT))
except ConnectionRefusedError:
    sys.exit("[cliente TCP] conexión rechazada: el host respondió, pero nadie escucha en ese puerto (RST)")
except (socket.timeout, TimeoutError):
    sys.exit("[cliente TCP] sin respuesta al intento de conexión")

ip_local, puerto_local = cliente.getsockname()
print(f"[cliente TCP] conectado a {SERVER_IP}:{SERVER_PORT} desde {ip_local}:{puerto_local}")

cliente.sendall(MENSAJE.encode("utf-8"))
print(f"[cliente TCP] enviado: {MENSAJE!r}")

datos = cliente.recv(1024)
print(f"[cliente TCP] respuesta ({len(datos)} bytes): {datos.decode('utf-8', errors='replace')!r}")

cliente.close()