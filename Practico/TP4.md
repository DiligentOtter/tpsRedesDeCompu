# Universidad Nacional de Córdoba
### Facultad de Ciencias Exactas, Físicas y Naturales

![alt text](images/image3.png)

# Redes de Computadoras
## Trabajo Práctico de Teórico N.º 4: Capas de Acceso en Redes Locales, Protocolos y Fundamentos

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

## Ítem 1 — Alcance de Redes y Virtualización

### A) Clasificación de las redes según su alcance

Las redes de computadoras se clasifican según su cobertura geográfica en distintos tipos. En la escala más reducida se encuentran las PAN (Personal Area Network), diseñadas para interconectar dispositivos de uso personal en un radio de pocos metros, por ejemplo Bluetooth.  
Subiendo en cobertura están las LAN (Local Area Network), las cuales son muy utilizadas en corporaciones o en el hogar para conectar equipos dentro de una misma oficina o edificio ya que ofrecen altas velocidades de transferencia y una baja latencia.  
Para abarcar áreas mayores existen las CAN (Campus Area Network), que tienen múltiples redes locales dentro de un predio delimitado como una universidad o complejo industrial, y las MAN (Metropolitan Area Network), que fueron creadas para cubrir la infraestructura de una ciudad o municipio entero uniendo sedes distantes.  
Por último, las WAN (Wide Area Network) abarcan países o continentes a través de infraestructuras públicas y privadas, donde Internet es el mayor ejemplo de esta categoría.

### B) ¿Qué es una vLAN? ¿Cómo se clasifican?

Una VLAN (Virtual Local Area Network) es una técnica de segmentación lógica que permite dividir una red física en varias redes lógicas independientes dentro del mismo switch o infraestructura física. Esto significa que los dispositivos conectados al mismo equipo físico pueden comportarse como si estuvieran en redes completamente aisladas, lo que mejora la seguridad, optimiza el tráfico broadcast y facilita la administración de la red sin necesidad de modificar el cableado. Las VLANs se clasifican  según la forma en que se asignan los puertos o dispositivos:las VLANs basadas en puerto vinculan un puerto físico del switch a una VLAN determinada; las VLANs dinámicas asignan la pertenencia de forma flexible utilizando parámetros como la dirección MAC del dispositivo, el tipo de protocolo de capa superior utilizado o credenciales de usuario (por medio de servidores como RADIUS).

### C) Protocolo IEEE 802.1Q y su relación con las VLANs

El estándar IEEE 802.1Q es el protocolo universal de red que define la arquitectura y el mecanismo formal para la implementación de VLANs en redes Ethernet. Su función clave es permitir que múltiples redes virtuales puedan viajar compartiendo un mismo enlace físico entre dos dispositivos de red (por ejemplo, el cable que conecta dos switches o un switch con un router). La relación con las VLANs es directa y estructural: sin este estándar de la industria, cada VLAN requeriría su propio cable físico independiente para comunicarse entre equipos, mientras que 802.1Q permite que el tráfico de decenas de VLANs distintas transite de forma multiplexada por un único enlace de interconexión (trunk) manteniendo la separación de cada red.

### D) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?

En el marco de las VLANs y el estándar IEEE 802.1Q, el Tagging es el proceso mediante el cual un switch inserta un encabezado especial de 4 bytes dentro de la trama Ethernet antes de enviarla a través de un enlace trunk. Esta etiqueta incluye un campo fundamental llamado VLAN ID (Identificador de VLAN), el cual le informa al dispositivo receptor a qué red virtual específica pertenece esa trama para que no se mezcle con el tráfico de otras VLANs. Cuando la trama llega a su destino o a un puerto de acceso final, el switch receptor lee el tag, encamina el paquete a la VLAN correspondiente y elimina la etiqueta antes de entregar la trama al dispositivo final, asegurando que las computadoras reciban paquetes Ethernet estándar sin enterarse de la infraestructura virtual subyacente.  

---

## Bibliografía

*Comunicaciones y Redes de Computadores — William Stallings, 7.ª edición*

1. Capítulo 3.1 — Conceptos y terminología
2. Capítulo 3.2 — Transmisión de datos analógicos y digitales
3. Capítulo 3.3 — Dificultades en la transmisión
4. Capítulo 3.4 — Capacidad del canal
5. Capítulo 4.1 — Medios de transmisión guiados
6. Capítulo 4.2 — Transmisión inalámbrica
7. Capítulo 4.3 — Propagación inalámbrica
8. Capítulo 4.4 — Transmisión en la trayectoria visual
9. Capítulo 5.1 — Datos digitales, señales digitales
10. Capítulo 5.2 — Datos digitales, señales analógicas
11. Capítulo 6.1 — Transmisión asincrónica y sincrónica
12. Capítulo 6.5 — Configuraciones de línea