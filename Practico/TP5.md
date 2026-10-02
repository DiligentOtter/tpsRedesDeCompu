# Universidad Nacional de Córdoba
### Facultad de Ciencias Exactas, Físicas y Naturales

![alt text](images/image3.png)

# Redes de Computadoras
## Trabajo Práctico de Nº 5 - Transmision de Datos: de ICMP y ARP a Sockets TCP entre Dos computadoras

| | |
|---|---|
| **Comisión** | ICOMP 24-3 |
| **Docente** | Oliva, Facundo |
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

## Item 1: ICMP y primer contacto con Wireshark.

### A) ¿Que es ICMP y para que se usa? ¿Transporta datos de aplicaciones como lo hacen TCP o UDP?

**ICMP** proporciona un medio para transferir mensajes desde los dispositivos de encaminamiento y otros computadoras a un computador. En esencia, ICMP proporciona informacion de realimentacion sobre **problemas del entorno de la comunicacion**. Se usa cuando por ejemplo un datagrama no puede llegar a destino ó cuando el dispositivo de encaminamiento no tiene la capacidad de almacenar temporalmente para reenviar el datagrama ó cuando el dispositivo de encaminamiento indica a una estacion que envie el trafico por una ruta mas corta.

A diferencia de **TCP** o **UDP**, **ICMP** no transporta datos de aplicaciones de usuario, sino que comunica directamente a los modulos de software IP de distintos equipos para tareas de control y gestion.

### B) ¿Que relacion tiene con IP? ¿Viaja dentro de IP, al lado de IP o debajo de IP? ¿Como sabe el receptor que el contenido de un paquete IP es ICMP?

**ICMP** está, a todos los efectos, en el mismo nivel que **IP** en el conjunto de protocolos **TCP/IP**, es un usuario de IP. Cuando se construye un mensaje de ICMP, este se pasa a IP, que encapsula el mensaje con una cabecera IP y despues transmite el datagrama resultante de la forma habitual. Los mensajes ICMP se transmiten en datagramas IP.

Por lo tanto, **ICMP** viaja dentro de la **carga util** de IP.

El receptor indica que la carga util es un mensaje de **ICMP** al examinar el campo **Protocol** del encabezado IPv4, el cual lleva asignado el valor de **1**.

### C) ¿Que hace Ping? ¿Que es un Echo Request y un Echo Reply? ¿Que campos de ICMP permiten distinguirlos?

**PING** es una herramienta de diagnostico de red que sirve para comprobar si una computadora o router remoto esta encendido y accesible a traves de la red, midiendo ademas el tiempo que tarda la señal en ir y volver **RTT** (*Round Trip Time*).

Echo Request y Echo Reply son dos tipos de mensajes de informacion de **ICMP**:
- **Echo Request** (*Peticion de Eco*): es el mensaje que envia tu maquina hacia el equipo de destino solicitandole que confirme si esta activo.
- **Echo Reply** (*Respuesta de Eco*): es el mensaje de respuesta que genera obligatoriamente el equipo de destino cuando recibe una peticion, devolviendo exactamente los mismos datos que le enviaron.

Se diferencian fundamentalmente por el campo **Type** del encabezado **ICMP**, en **IPv4**, el **Echo Request** tiene `type = 8` y el **Echo Reply** tiene `type = 0`.

### D) ¿Que informacion minima contiene un mensaje ICMP de tipo Echo?

Un mensaje ICMP de tipo Echo (Echo Request o Echo Reply) contiene una cabecera fija de 8 bytes mas una carga util de datos opcional (Data).
La informacion que compone la estructura minima de un mensaje Echo consta de los siguientes campos:
- `type` (Tipo - 1 byte): especifica si el mensaje es una peticion (`8`) o una respuesta (`0`).
- `code` (Codigo - 1 byte): en los mensajes Echo siempre vale `0`.
- `checksum` (Suma de Comprobacion - 2 bytes): codigo de comprobacion de errores calculado sobre todo el mensaje ICMP.
- `identifier` (Identificador - 2 bytes): un valor numerico que sirve para identificar la sesion o el proceso del sistema operativo que envio el ping.
- `sequence number` (Numero de Secuencia - 2 bytes): un numero que se incrementa secuencialmente con cada peticion enviada por la aplicacion.
- `data` (Datos opcionales - Longitud variable): un bloque de datos opcional enviado por la aplicacion.