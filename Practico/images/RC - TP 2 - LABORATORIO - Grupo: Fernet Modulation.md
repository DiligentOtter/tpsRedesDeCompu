  
# UNIVERSIDAD NACIONAL DE CÓRDOBA |  FACULTAD DE CIENCIAS EXACTAS, FÍSICAS Y NATURALES  
<img width="532" height="520" alt="image1" src="https://github.com/user-attachments/assets/85d62a69-318f-4106-b3d6-e28ec01adab9" />


## **REDES DE COMPUTADORAS**  
### **Trabajo Practico de laboratorio N°2:**  
### **TRANSMISIÓN DE DATOS**

**Comisión: ICOMP 24-3**  
**Docentes: Oliva, Facundo**  

**Alumnos:**
- **Lamas, Matías Angel**  
- **Torres Sosa, Candelaria**  
- **Baiutti, Bruno Augusto**  
- **Sanchez Oliveto, Juan Cruz**  
- **Vazquez Zuloeta, Fabian**  
- **Pinque, Emanuel Leandro**	  
- **Mayne, William Annesley**  

**Año: 2026** 

## **ITEM 1**

A)  
El fenómeno presentado se denomina efecto doppler se trata del aumento de frecuencia con respecto a un observador con velocidad relativa respecto a la onda distinta de 0 

su fórmula es:  
$f' = f (v+-v0/v+-vs)$

Si el observador se acerca a la fuente  
$f' = f (v+v0 / v-vs)$  

Si se aleja  
$f' = f (v-v0v+vs)$

### Ejemplo con la velocidad del sonido 343.4 m/s
<img width="445" height="467" alt="image3" src="https://github.com/user-attachments/assets/e6f9efc8-4d4f-4275-abdf-eaa4c7493d3c" />
<img width="445" height="467" alt="image5" src="https://github.com/user-attachments/assets/3c66d6b4-58da-4c50-beb0-d1c85cd9261e" />




**Se aprecian varias características:**

* *Al hacer variar la velocidad objeto con la fuente en reposo se observa un **crecimiento lineal** en la frecuencia de la onda, esto sucede por que al aplicar la ecuación de onda v=f vemos que la aumentar la velocidad del objeto también aumenta la velocidad de onda aparente v por la velocidad relativa, y crece de forma lineal por su proporcionalidad a la frecuencia*
    
* *Ahora sucede algo interesante al mover la fuente, cuando está en movimiento produce ondas pero las mismas al tener una velocidad constante en el medio no conservan la velocidad relativa de la fuente, por lo que siempre se mueven a la misma velocidad, cuando el objeto cada vez se acerca más a la velocidad del medio estas ondas cada vez se acumulan más hasta que si la fuente se mueve a una velocidad extremadamente cercana a la del medio las ondas quedan muy juntas por que no les da tiempo a separarse de la fuente lo que hace tender a infinito la frecuencia (aunque esto en la práctica no ocurre por la conservación de la energía)*

B)  

Debido a que este efecto es proporcional a la frecuencia de la onda emisora, es más afectado por bandas de mayor frecuencia, es decir. Las más afectadas son las SHF Y EHF , las transmisiones de microondas como radares y comunicaciones de telefonía moderna

<img width="780" height="488" alt="image4" src="https://github.com/user-attachments/assets/7ac90416-f164-4d30-ac20-dddd60636b6c" />


Por otra parte, las bandas de frecuencia menos afectadas son las MF HF O VHF las ondas de radio AM , FM y la TV.

C)

Hay dos razones por las cuales no se deben encender los celulares arriba de un avión, el efecto doppler por la velocidad y la saturación de la red en tierra por la altura.

Por velocidad un avión comercial vuela a unos 900 Km/h, a esa velocidad, la variación de frecuencia es tan grande que el receptor en tierra no podría compensar la variación rápidamente.  
Por altura, a 10000 m de altura, al no haber obstáculos físicos como edificios o montañas, se produce una propagación en la trayectoria visual directa con muchísimas antenas en la tierra a la vez. Los teléfonos de la cantidad de pasajeros estuvieran encendidos intentaron conectarse con decenas de antenas base de forma simultánea, esto generaría mucho intercambio de señalización que saturaría la capacidad de las celdas en tierra.

# **ITEM 2**

A)  
El fenómeno que se está representando en la figura del obrero con el taladro es el ruido impulsivo. Este ruido no es continuo, es irregular, tiene una duración muy corta y con picos de amplitud muy elevados.

B)  
Esto afecta principalmente a las transmisiones digitales, las transmisiones analógicas son más resilientes. Por ejemplo si se está hablando por un teléfono analógico se acopla un chasquido por un taladro, se va a oír un clic molesto pero se va a seguir entendiendo la conversación. A diferencia de transmitir datos digitales, ese clic puede cambiar ceros por unos y corromper el archivo completo.  
Las transmisiones de altísima velocidad sufren un impacto mucho más severo, a grandes velocidades puede corromper cientos de bits en esa fracción de tiempo.

C)  
La SNR es un concepto físico de la capa física. Mide la relación entre la potencia de la señal útil que queremos transmitir y la potencia del ruido que se introduce en el medio. Esta relación se mide en decibelios y se evalúa en el receptor porque es ahí donde se procesa la señal y se intenta eliminar el ruido.  
Si tienen que ver, tienen una relación inversa. Al tener una señal muy fuerte frente al ruido (alta SNR), el receptor puede distinguir con más facilidad los niveles de tensión, lo que reduce drásticamente el BER.

## **ITEM 3**
### **Tipos de error y por qué importan**

* **Error aislado:** Afecta a un único bit. Causado típicamente por el ruido térmico (blanco).  
* **Ráfaga de errores (longitud B):** El primer y último bit están errados; los interiores también pueden estarlo. Producido típicamente por el ruido impulsivo.

### **Detección de errores**

El transmisor calcula sobre $k$ bits de datos un código $E = f(\text{datos})$ y lo agrega a la trama ($n = k + (n - k)$ bits). El receptor calcula el mismo código y lo compara.

* **Bit de paridad (simple):** Agrega un bit al final para que la cantidad de unos sea par o impar.  
* **CRC (Comprobación de Redundancia Cíclica):** Transmisor y receptor acuerdan un divisor $P$. Se calcula una secuencia $R$ tal que la trama sea divisible por $P$ en aritmética módulo 2\. Si el resto al dividir en recepción no es cero, hay error.

### **Corrección de errores: códigos de bloque y FEC**

Cuando retransmitir no es viable, el receptor corrige usando solo los bits recibidos: **FEC (Forward Error Correction)**. Se usa con códigos de bloque $(n, k)$: mapean $k$ bits a palabras-código de $n$ bits ($n \> k$).

* **Distancia de Hamming:** Cantidad de posiciones en que difieren dos palabras. Con $d\_{\\min}$, se corrigen hasta $t$ bits si $d\_{\\min} \ge 2t + 1$, y se detectan $d\_{\\min} - 1$ errores. A mayor $d\_{\\min}$ (más corrección), se requieren más bits redundantes (menos ancho de banda útil).  
* **Ganancia del código:** Reducción en dB del $E\_b/N\_0$ necesario para lograr una BER dada.  
* Diferencia clave: **FEC** corrige sin pedir reenvío; **ARQ** detecta y pide retransmisión.

### **Compensación de cambios en la frecuencia (sincronización)**

Los relojes del transmisor y receptor tienen pequeñas diferencias de frecuencia. El receptor necesita saber cuándo muestrear cada bit.

#### **Transmisión asíncrona vs. síncrona**

* **Asíncrona:** Transmite carácter por carácter delimitado por bit de comienzo (0) y parada (1). Evita acumular error de temporización resincronizando en cada carácter. Alto overhead (\~20%).  
* **Síncrona:** Transmite bloques grandes de corrido. Para no perder sincronía, incluye el reloj dentro de la propia señal de datos mediante la codificación.

#### **Códigos autosincronizados (Manchester y Manchester diferencial)**

Garantizan al menos una transición por bit para resincronizar el reloj (a diferencia de NRZ, donde rachas de bits iguales pierden sincronía).

* **Manchester:** Transición en la mitad de cada bit.  
* **Manchester diferencial:** Transición a mitad de intervalo para sincronizar; el bit se codifica según si hay o no transición al principio.  
* **Contra:** Requieren el doble de ancho de banda que NRZ.

#### **Aleatorización / Scrambling**

Sustituye secuencias de tensión constante por patrones con suficientes transiciones sin aumentar la velocidad ni el ancho de banda.

* **B8ZS:** Reemplaza cadenas de 8 ceros introduciendo violaciones de código AMI.  
* **HDB3:** Sustituye cadenas de 4 ceros manteniendo la alternancia de polaridad para evitar componente continua.


## **ITEM 4**

**A)**  

**Sincronización:** Es el proceso mediante el cual el emisor y el receptor acuerdan y alinean sus relojes o tiempos para interpretar la información transmitida.

**Sincronización de bits:** Alinea los relojes a nivel de tiempo individual para determinar exactamente cuándo empieza y termina un solo bit  y tomar la muestra en el momento justo.

**Sincronización de trama:** Identifica el inicio y el fin de un bloque completo de datos mediante banderas o delimitadores especiales, permitiendo reconocer dónde empieza la cabecera y el conjunto de bits de la carga útil.

**Trama (Frame):** Es la unidad fundamental de datos en el nivel de enlace que empaqueta información digital agrupando datos de control y carga útil para enviarla de forma estructurada a través de un medio físico.

B)

**Encabezado (*Header*):** Se ubica al inicio de la trama y contiene la metadata de control necesaria para el enrutamiento y la identificación.

**Carga Útil (*Payload*):** Es el contenido de datos real que se desea transmitir

**Tráiler:** Se ubica al final de la trama y contiene metadatos de detección/corrección de errores y delimitadores de fin de trama para asegurar que el mensaje llegó íntegro.

C) 	La función que cumple el preámbulo antes de la trama es ayudar a sincronizar al receptor, para que este pueda determinar con exactitud dónde comienza la información que se quiere enviar. Por lo que, el preámbulo no es necesariamente parte de la información que se desea transmitir, sino que contiene información de sincronización entre los sistemas facilitando así la correcta recepción de los datos. 

D) Existen diferentes mecanismos para que el receptor pueda identificar el final de una trama:

**Longitud fija:** Todas las tramas tienen exactamente la misma cantidad de bits o bytes. Por lo tanto, una vez identificado el comienzo de una trama, el receptor sabe que después de una cantidad determinada de bits llegará su final. 

**Caracteres o secuencias delimitadoras:** Se utiliza una secuencia especial de bits o caracteres para indicar el final de una trama. El receptor busca continuamente esa secuencia y, cuando la encuentra, sabe que la trama terminó. Un ejemplo es **HDLC**, que utiliza la secuencia `01111110` como *flag*. Esta secuencia puede indicar tanto el comienzo como el final de una trama. El problema es que esa misma secuencia podría aparecer dentro de los datos. Para evitar que el receptor la confunda con el final de la trama, se utiliza una técnica denominada **inserción de bits (*bit stuffing*)**, mediante la cual el emisor modifica temporalmente los datos para que la secuencia delimitadora no aparezca accidentalmente.

**Campo que indique la longitud:** En este caso, la trama contiene un campo dentro de su cabecera que indica cuántos bits o bytes ocupa la trama. El receptor lee ese campo y, a partir de allí, sabe cuántos datos debe recibir antes de considerar que la trama terminó. La ventaja es que permite utilizar tramas de **longitud variable**. Una desventaja es que si el campo de longitud se corrompe por un error, el receptor puede perder la sincronización y tener dificultades para encontrar nuevamente los límites de las tramas. 

## Item 5

A partir de la estructura de trama definida ($HDR + PAYLOAD$) con la siguiente especificación de campos:

* **GROUP (40 bits / 5 bytes):** "ferne" $\rightarrow$ 66 65 72 6E 65 (ASCII hexadecimal, lower case).  
* **SEQ (8 bits / 1 byte):** Número de secuencia de paquete.  
* **LENGTH (8 bits / 1 byte):** Longitud en bytes de la carga útil ($uint8$).  
* **PAYLOAD:** Carga útil equivalente a $N$ bytes según el valor del campo LENGTH.

#### **Trama Identificada**

Se identificó dentro del binario el bloque correspondiente al grupo **"ferne"**, cuyo despiece y análisis hexadecimal es el siguiente:

| Campo | Valor (Hex) | Decodificación / Descripción |
| :---- | :---- | :---- |
| **GROUP** | 66 65 72 6E 65 | Representación ASCII de la clave de grupo ("ferne"). |
| **SEQ** | 06 | Paquete número 6 en la secuencia global. |
| **LENGTH** | 01 | Longitud del payload: 1 byte. |
| **PAYLOAD** | 2F | Carácter ASCII de la carga útil ('/'). |

**Trama completa en hexadecimal:**

`66 65 72 6E 65 06 01 2F`

**Valor del payload extraído:** `'/'` (ASCII `0x2F`, posición en secuencia: `06`)

Link del binario: [https://www.youtube.com/shorts/be\_ln6Lnww](https://www.youtube.com/shorts/be_ln6Lnww) (roto 🙁)

# **3 BIBLIOGRAFÍA**

Comunicaciones y Redes de Computadores \- William Stallings \- 7ed:

* Capítulo 3.1: Conceptos y terminología.  
* Capítulo 3.2: Transmisión de datos analógicos y digitales.  
* Capítulo 3.3: Dificultades en la transmisión.  
* Capítulo 3.4: Capacidad del canal.  
* Capítulo 4.1: Medios de transmisión guiados.  
* Capítulo 4.2: Transmisión inalámbrica.  
* Capítulo 4.3: Propagación inalámbrica.  
* Capítulo 4.4: Transmisión en la trayectoria visual.  
* Capítulo 5.1: Datos digitales, señales digitales.  
* Capítulo 5.2: Datos digitales, señales analógicas.  
* Capítulo 6.1: Transmisión asincrónica y sincrónica.  
* Capítulo 6.5: Configuraciones de línea.

