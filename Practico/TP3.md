# UNIVERSIDAD NACIONAL DE CÓRDOBA
### Facultad de Ciencias Exactas, Físicas y Naturales
## Redes de Computadoras
## Trabajo Práctico de Teórico Nº2: Transmisión de Datos

#### Comisión: ICOMP 24-3
#### Docentes: Oliva, Facundo
#### Alumnos:
- Lamas, Matías Angel
- Torres Sosa, Candelaria
- Baiutti, Bruno Augusto
- Sanchez Oliveto, Juan Cruz
- Vazquez Zuloeta, Fabian
- Pinque, Emanuel Leandro
- Mayne, William Annesley

#### Año: 2026

---

## Item 1

- **B)**
    Una dirección MAC (Media Access Control) es un id único de 48 bits grabado en la tarjeta de red (NIC) de un dispositivo, de esta forma es posible identificar de manera inequívoca a un dispositivo en una red LAN. Por otro lado, la dirección IP (Internet Protocol) es una dirección entre redes, que permite ubicar a un destinatario de un paquete de manera sencilla, no deja de ser público mientras que la dirección MAC solo la conoce la red interna, LAN o WAN.

- **C)**
    La trama ethernet, transmitida en la capa de enlace de datos, es una trama de entre 64 y 1518 bytes. Esta trama contiene los siguientes elementos de cabecera:
    - Preámbulo - SFD 8 bytes: Una ristra de 0s y 1s alternados para sincronizar el reloj del receptor
    - MAC Destino 6 bytes
    - MAC Origen 6 bytes
    - Ether type 2 bytes: identifica el tipo de protocolo que viene en la capa 3, IPv4 o IPv6
    - Payload 46 - 1500 bytes: paquete IP real con un padding de al menos 46 bytes
    - Frecuencia de Verificación de trama (FCR): Es el código de redundancia cíclica de esta capa que le permite al receptor identificar errores

- **D)**
    El encargado es el Ether type, donde tenemos que:
    - 0x0800 -> IPv4
    - 0x86DD -> IPv6
    - 0x0806 -> ARP

---

## Item 2

- **A)**
    El paquete observado bajo la arquitectura del protocolo TCP (al acceder a YouTube) proviene de la IP pública 142.251.155.4, perteneciente a los servidores de Google. En este evento se registra la siguiente trama Ethernet II:

    ```
    24 4b fe 82 39 3d 02 10 18 cf 61 74 08 00
    ```

    En este encabezado podemos identificar:
    - **MAC de Origen:** 02:10:18:cf:61:74 — Corresponde al gateway (router local). Su prefijo es resuelto por Wireshark como MS-NLB (Microsoft Network Load Balancing).
    - **MAC de Destino:** 24:4b:fe:82:39:3d — Dirección física de la tarjeta de red de la computadora receptora.

- **D)**
    Los últimos dos bytes del encabezado de la trama Ethernet (0x0800) representan el campo EtherType. Este valor le comunica a la capa de enlace que el protocolo encapsulado en la capa de red superior corresponde a IPv4.

- **B)**
    En el encabezado del protocolo IP (Capa de Red), se identifican las siguientes direcciones de capa 3:
    - **IP de Origen:** 142.251.155.4 — Dirección pública perteneciente a los servidores de Google (servicios de YouTube).
    - **IP de Destino:** 192.168.0.77 — Dirección privada asignada a la computadora receptora dentro de la red local.

- **C)**
    Las direcciones MAC e IP cumplen funciones completamente distintas dentro del modelo de red:
    - **Dirección MAC (Capa 2):** Tiene alcance exclusivo dentro de la red local (LAN). Cambia en cada salto de red, por lo que la MAC de origen observada (02:10:18:cf:61:74) corresponde al router local (gateway) y no al emisor final.
    - **Dirección IP (Capa 3):** Identifica el origen y destino finales a nivel global. Se mantiene a lo largo de toda la ruta a través de Internet.

---

## Item 3

*(pendiente)*

---

## Item 4

Para el ejercicio propuesto se nos dieron los siguientes parámetros:

**Parámetros de Conexión:**
- IP de Destino: 34.136.251.235
- Puerto de Destino: 5555

**Registro de Interacción (Packet Sender / Servidor TCP):**

| Solicitud | Respuesta |
|---|---|
| hola | hola :) |
| pika | Server no conocer ese comando. Mi confundido. Probar otra cosa. |
| fernetmodulation | seq: 7, payload: yo |
| hola | hola :) |
| ping | pong |
| h | Server no conocer ese comando. Mi confundido. Probar otra cosa. |

**Resultado Clave:**
Al enviar el comando `fernetmodulation`, el servidor retornó la secuencia 7 asociada al payload "yo" (`seq: 7, payload: yo`).

---

## Bibliografía

**Comunicaciones y Redes de Computadores — William Stallings — 7ed:**
- Capítulo 3.1: Conceptos y terminología
- Capítulo 3.2: Transmisión de datos analógicos y digitales
- Capítulo 3.3: Dificultades en la transmisión
- Capítulo 3.4: Capacidad del canal
- Capítulo 4.1: Medios de transmisión guiados
- Capítulo 4.2: Transmisión inalámbrica
- Capítulo 4.3: Propagación inalámbrica
- Capítulo 4.4: Transmisión en la trayectoria visual
- Capítulo 5.1: Datos digitales, señales digitales
- Capítulo 5.2: Datos digitales, señales analógicas
- Capítulo 6.1: Transmisión asincrónica y sincrónica
- Capítulo 6.5: Configuraciones de línea