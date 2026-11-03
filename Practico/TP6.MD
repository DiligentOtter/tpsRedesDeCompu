# Universidad Nacional de Córdoba
### Facultad de Ciencias Exactas, Físicas y Naturales

![alt text](images/image3.png)

# Redes de Computadoras
## Trabajo Práctico Nº 6 - Laboratorio: Construcción de cable UTP y conexión en red LAN

| | |
|---|---|
| **Comisión** | ICOMP 24-3 |
| **Docente** | SANTIAGO MARTIN HENN |
| **Año** | 2026 |

**Alumnos:**
- Lamas, Matías Angel
- Torres Sosa, Candelaria
- Baiutti, Bruno Augusto
- Sanchez Oliveto, Juan Cruz
- Vazquez Zuloeta, Fabian
- Pinque, Emanuel Leandro
- Mayne, William Annesley

---

## Parte 1: Armado y verificación de cable UTP bajo estándar T568B

El armado de un cable de red de transmisión directa, también conocido como cable derecho, es un procedimiento técnico fundamental en las telecomunicaciones que garantiza la correcta transmisión de datos entre dispositivos como computadoras, switches y routers. Este proceso se rige bajo la norma internacional ANSI/TIA/EIA-568, la cual define el esquema exacto de distribución y orden de los cables dentro de los conectores. La norma contempla dos variantes principales para el código de colores: T568A y T568B. Ambas ofrecen exactamente el mismo rendimiento técnico y ancho de banda, diferenciándose únicamente en el intercambio de posiciones entre el par verde y el par naranja. Para armar un cable directo, la regla básica es replicar el mismo estándar en ambos extremos del cable, siendo el esquema T568B el más utilizado en la industria.

### Procedimiento de crimpado de cable de red RJ-45

#### Materiales necesarios
- Cable de par trenzado UTP categoría 5e o 6
- Dos conectores RJ-45 transparentes
- Pinza crimpadora o ponchadora para conectores de 8 pines
- Pelacables o la cuchilla de la crimpadora
- (Opcional) Comprobador o tester de cables LAN

#### Desarrollo
1. **Preparación del cable**

    Con el pelacables o la cuchilla de la crimpadora, retiramos unos 3 cm del revestimiento exterior de plástico de un extremo del cable. Tuvimos cuidado de no mellar ni cortar el aislamiento de los ocho hilos de cobre internos.

    Luego separamos y destrenzamos con cuidado los cuatro pares de hilos.

2. **Organización de los hilos (norma T568B)**

    Ordenamos los hilos en una tira plana, de izquierda a derecha, según esta secuencia:

    | Posición | Color |
    |-----|-----|
    | 1 | Blanco / naranja |
    | 2 | Naranja |
    | 3 | Blanco / verde |
    | 4 | Azul |
    | 5 | Blanco / azul |
    | 6 | Verde |
    | 7 | Blanco / marrón |
    | 8 | Marrón |

    Sostuvimos la tira firmemente, cerca del borde de la cubierta externa. Cortamos la punta del manojo a 90 grados con la navaja recta de la crimpadora, dejando los hilos con una longitud uniforme de 1,2 a 1,4 cm.

    Esta medida es crítica: los hilos deben llegar hasta el fondo del conector, y la funda exterior tiene que entrar lo suficiente para quedar sujeta por el mecanismo de retención del RJ-45.

3. **Inserción en el conector**

    Tomamos el conector RJ-45 con la pestaña de fijación hacia abajo y los contactos dorados hacia arriba. Introducimos los ocho hilos alineados.

    ![alt text](images/photo_2.jpg)

    Empujamos suavemente hasta verificar, a través del plástico transparente, que cada hilo llegó al fondo del conector y que el orden de colores no se alteró.

4. **Crimpado**

    Insertamos el conector en la ranura correspondiente de la pinza crimpadora y presionamos firmemente los mangos hasta completar todo el recorrido del mecanismo.

    ![alt text](images/photo_1.jpg)

    Durante este paso, las cuchillas empujan los contactos metálicos para perforar la funda de cada hilo y establecer contacto eléctrico. Al mismo tiempo, una pestaña plástica sujeta la cubierta exterior del cable para resistir tirones.

    Repetimos exactamente el mismo procedimiento en el extremo opuesto, manteniendo el esquema T568B.

5. **Verificación**

    Probamos ambos extremos en el tester de red. Si el crimpado es correcto, los ocho LED se encienden en secuencia, en el mismo orden, en ambos lados, como se muestra a continuación.

    ![alt text](images/video_1.gif)

---

## Parte 2: Equipamiento físico, verificación y utilización de equipos de red y generación de tráfico

Para esta parte utilizamos el switch **Cisco Catalyst 2950** disponible en el laboratorio. El switch funciona en capa 2 (enlace): reenvía tramas Ethernet entre sus puertos según las direcciones MAC que va aprendiendo, sin mirar las direcciones IP. Con su configuración de fábrica todos los puertos pertenecen a la VLAN 1 y están habilitados, por lo que para armar una LAN simple alcanza con conectar las computadoras, sin configurar nada en el switch. Por eso no realizamos la parte opcional (acceso por consola y administración).

Las computadoras se conectan al switch con cables **derechos** como el armado en la Parte 1: la PC transmite por los pines 1-2 y recibe por los 3-6, y el switch hace lo inverso internamente. Por eso no hace falta un cable cruzado entre equipos de distinto tipo (PC ↔ switch).

### Levantar y testear una LAN

#### 1. Configuración manual de la interfaz de red

> **TODO:** completar sistema operativo de cada PC, el grupo con el que compartimos el switch y agregar captura de pantalla de la configuración.

| Equipo | Sistema operativo | Dirección IPv4 | Máscara de subred | Default gateway |
|---|---|---|---|---|
| PC-1 | _completar_ | 192.168.1.10 | 255.255.255.0 (/24) | 192.168.1.1 |
| PC-2| _completar_ | 192.168.1.20 | 255.255.255.0 (/24) | 192.168.1.1 |

La configuración se puede hacer por interfaz gráfica o por consola:

- **Windows** (PowerShell como administrador):
  ```powershell
  netsh interface ipv4 set address name="Ethernet" static 192.168.1.10 255.255.255.0 192.168.1.1
  ```
- **Linux**:
  ```bash
  sudo ip addr add 192.168.1.10/24 dev eth0
  sudo ip route add default via 192.168.1.1
  ```

![alt text](images/TODO_config_ip.png)

**Justificación de las direcciones elegidas:**

- **Dirección IPv4:** elegimos direcciones del rango privado 192.168.0.0/16 (RFC 1918), que no son ruteables en Internet y no generan conflictos con redes públicas. Cada PC tiene una dirección distinta dentro de la misma red para que no haya duplicados.
- **Máscara de subred:** con 255.255.255.0 (/24), los tres primeros octetos identifican la red (192.168.1.0) y el último el host. Así todas las PCs quedan en la misma subred y pueden comunicarse directamente a través del switch, resolviendo las MAC con ARP. La red admite hasta 254 hosts, más que suficiente para el laboratorio.
- **Default gateway:** configuramos 192.168.1.1 por convención, pero en esta actividad **no tiene efecto**. No hay ningún router conectado al switch, y todo el tráfico va dirigido a hosts de la misma subred, que se entrega directamente sin pasar por el gateway. El gateway solo se usaría para alcanzar destinos fuera de 192.168.1.0/24, como Internet, que en esta LAN aislada no son alcanzables. Se podría haber dejado vacío y todo habría funcionado igual.
#### 2. Conexión al switch y prueba con ping

Conectamos una computadora de cada grupo al switch utilizando cables verificados con el tester. Al conectar, el LED del puerto correspondiente en el switch se encendió, indicando enlace en capa física.

Desde nuestra PC ejecutamos:

```bash
ping 192.168.1.20
```

> **TODO:** pegar la salida del ping (o captura) e indicar si hubo pérdida de paquetes y el tiempo promedio de respuesta. Si hubo problemas (por ejemplo, el firewall de Windows bloquea por defecto las solicitudes de eco ICMP entrantes), describir cómo se resolvieron.

![alt text](images/TODO_ping.png)

#### 3. Comunicación UDP con ncat

En la PC receptora levantamos un receptor UDP escuchando en el puerto 5000:

```bash
ncat -u -l 5000
```

Desde la segunda PC enviamos mensajes al receptor:

```bash
ncat -u 192.168.1.10 5000
```

Cada línea escrita en la consola del emisor se envía como un datagrama UDP y aparece en la consola del receptor.

> **TODO:** agregar capturas de ambas terminales (emisor y receptor) y los mensajes enviados.

![alt text](images/TODO_ncat.png)

#### 4. Captura con Wireshark

En la PC receptora capturamos en la interfaz Ethernet aplicando el filtro:

```
udp.port == 5000
```

> **TODO:** agregar captura de Wireshark y completar lo observado (IPs y puertos de origen y destino, longitud, contenido del payload).

![alt text](images/TODO_wireshark_udp.png)

En cada paquete se observan las cuatro capas: la trama **Ethernet II** con las MAC de origen y destino, el encabezado **IPv4** con las direcciones de ambas PCs y el campo protocolo = 17 (UDP), el encabezado **UDP** y, por último, los datos, donde se puede leer en texto plano el mensaje enviado. El encabezado UDP ocupa solo 8 bytes: puerto de origen (asignado de forma efímera por el sistema), puerto de destino (5000), longitud y checksum.

#### 5. Preguntas

**a) ¿Se observa algún procedimiento de establecimiento de conexión antes de enviar los datos?**

No. En la captura, el primer paquete entre las dos PCs ya es un datagrama UDP con el mensaje; no aparece ningún intercambio previo equivalente al *three-way handshake* de TCP (SYN, SYN-ACK, ACK). UDP es un protocolo **no orientado a conexión**: cada datagrama se envía de forma independiente, sin negociar ni mantener un estado de sesión entre emisor y receptor. Lo único que puede aparecer antes es un intercambio ARP, que es de capa 2 y sirve para obtener la MAC del destino, no para establecer una conexión.

**b) ¿Existe algún mecanismo de confirmación de recepción equivalente a los ACK de TCP?**

No. En la captura solo se ven datagramas del emisor hacia el receptor, sin ningún paquete de respuesta que confirme la llegada. El encabezado UDP no tiene números de secuencia ni de acuse de recibo, solo puertos, longitud y checksum. El checksum permite al receptor descartar un datagrama corrupto, pero el emisor nunca se entera. Si una aplicación necesita confiabilidad sobre UDP, debe implementar sus propias confirmaciones en la capa de aplicación.

**c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

El datagrama igual se envía y llega a la PC destino, porque UDP no verifica previamente que haya alguien escuchando. Como no hay ningún proceso asociado al puerto 5000, el sistema operativo del receptor descarta el datagrama y, normalmente, responde con un mensaje **ICMP Destination Unreachable (Port Unreachable)**. Según el sistema operativo, ncat puede informar ese error en el siguiente envío (por ejemplo, "Connection refused" en Linux). Si el firewall del receptor descarta el paquete sin responder, cosa habitual en Windows, el emisor no recibe ningún aviso y los mensajes se pierden en silencio. En ningún caso los mensajes se guardan para entregarse después: cuando el receptor vuelve a ejecutarse, solo recibe los datagramas nuevos.

> **TODO:** si se hizo la prueba, indicar qué se observó en Wireshark (si apareció o no el ICMP Port Unreachable) y agregar captura.

**d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

No. UDP no numera los datagramas, así que el receptor no tiene forma de detectar ni corregir desórdenes, pérdidas o duplicados: los entrega a la aplicación en el orden en que llegan. En nuestra LAN, con un único switch y sin caminos alternativos, los mensajes llegaron en orden, pero eso se debe a la simplicidad de la red y no al protocolo. En redes más grandes, donde los paquetes pueden tomar rutas distintas o atravesar colas con congestión, el desorden es posible.

**e) ¿Qué aplicaciones reales utilizan UDP y por qué?**

UDP se usa cuando importa más la baja latencia y la simplicidad que la entrega garantizada, o cuando el intercambio es tan corto que el costo de abrir una conexión TCP no se justifica:

| Aplicación / protocolo | Motivo |
|---|---|
| **DNS** (puerto 53) | Consultas de un solo pedido y una respuesta; si se pierde, el cliente reintenta. Un handshake TCP triplicaría el tiempo. |
| **VoIP y videollamadas** (RTP) | Un paquete de audio que llega tarde ya no sirve; es preferible perderlo que esperar una retransmisión. |
| **Streaming en vivo y videojuegos online** | Requieren baja latencia; el estado se actualiza constantemente, así que un dato perdido queda superado por el siguiente. |
| **DHCP** (puertos 67/68) | El cliente todavía no tiene IP y necesita usar broadcast, que TCP no soporta. |
| **NTP, SNMP, Syslog** | Mensajes cortos y periódicos de sincronización, monitoreo o logs. |
| **QUIC / HTTP/3** | Implementa confiabilidad y cifrado sobre UDP para evitar el bloqueo en cabeza de línea de TCP y reducir el tiempo de establecimiento. |

---

### Desarrollar un pequeño servidor

#### 1. Servidor HTTP con Python

En una de las computadoras creamos un directorio con archivos de distintos tipos y levantamos un servidor HTTP con el módulo incluido en Python:

```bash
mkdir servidor_tp6
cd servidor_tp6
# copiar los archivos: TODO completar nombres (ej. notas.txt, enunciado.pdf, imagen.png)
python3 -m http.server 8000
```

El servidor queda escuchando en el puerto TCP 8000 de todas las interfaces y sirve el contenido del directorio actual, mostrando un listado de archivos.

> **TODO:** completar con los archivos usados y agregar captura del servidor en ejecución.

![alt text](images/TODO_http_server.png)

#### 2. Acceso desde el navegador

Desde la segunda PC abrimos en el navegador la dirección `http://192.168.1.10:8000/`, se mostró el listado de archivos del directorio y descargamos uno de ellos. En la consola del servidor quedó registrada cada petición `GET` con la IP del cliente y el código de respuesta (200).

> **TODO:** agregar captura del navegador y del log del servidor.

![alt text](images/TODO_navegador.png)

#### 3. Descarga con curl

Repetimos la descarga desde la terminal:

```bash
curl -O http://192.168.1.10:8000/archivo.pdf
```

La opción `-O` guarda el archivo con el mismo nombre que tiene en el servidor.

> **TODO:** agregar salida de curl y nombre real del archivo descargado.

![alt text](images/TODO_curl.png)

#### 4. Captura con Wireshark: ¿de qué tipo es el tráfico?

Capturamos con el filtro `tcp.port == 8000`.

> **TODO:** agregar captura de Wireshark.

![alt text](images/TODO_wireshark_http.png)

El tráfico es **HTTP sobre TCP**, a diferencia de la actividad anterior. En la captura se distinguen tres etapas:

1. **Establecimiento de conexión:** el *three-way handshake* de TCP (SYN → SYN-ACK → ACK) entre un puerto efímero del cliente y el puerto 8000 del servidor.
2. **Transferencia:** el cliente envía la petición `GET /archivo.pdf HTTP/1.1` y el servidor responde `HTTP/1.0 200 OK` con encabezados como `Content-Type` y `Content-Length`, seguidos del contenido del archivo dividido en varios segmentos TCP. El receptor confirma los segmentos con ACK, y se pueden ver los números de secuencia avanzando según los bytes transferidos.
3. **Cierre de conexión:** intercambio de segmentos FIN/ACK.

Como el servidor usa HTTP sin cifrar, todo el contenido (encabezados y archivo) viaja en texto plano y puede verse en Wireshark con *Follow → TCP Stream*, o exportarse con *File → Export Objects → HTTP*. Si Wireshark muestra los paquetes solo como TCP y no los interpreta como HTTP por estar en el puerto 8000, se puede forzar con *Decode As… → HTTP*.

Esto contrasta con UDP: aquí sí hay establecimiento de conexión, confirmación de recepción y orden garantizado, servicios que TCP le brinda a HTTP porque un archivo debe llegar completo y sin errores.

---

## Conclusiones

> **TODO:** ajustar con la experiencia real del grupo.

En la primera parte armamos un cable UTP derecho bajo la norma T568B y comprobamos con el tester la continuidad y el orden correcto de los ocho hilos. Vimos que el corte parejo de los hilos y la sujeción de la funda son claves para un cable confiable.

En la segunda parte usamos ese tipo de cable para conectar computadoras a un switch Cisco Catalyst 2950 y armar una LAN configurando las direcciones IP a mano. Comprobamos que, dentro de una misma subred, el gateway no interviene. Al generar y capturar tráfico pudimos comparar en la práctica los dos protocolos de transporte: UDP envía datagramas sin conexión ni confirmaciones, mientras que TCP, usado por HTTP, establece una conexión, confirma cada segmento y la cierra de forma ordenada.

> **Recordatorio:** al terminar, volvimos a configurar las interfaces de red en modo automático (DHCP) para recuperar el acceso a Internet.
