# *UNIVERSIDAD NACIONAL DE CORDOBA*

## *FACULTAD DE CIENCIAS EXACTAS, FÌSICAS Y NATURALES*

![image8.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image8.png)



## REDES DE COMPUTADORAS

## Trabajo Práctico de Laboratorio N°1:

## FUNDAMENTOS ESENCIALES E

## INTRODUCCIÓN A PACKET TRACER

#### Comision:Icom 24-3

#### Docentes:HENN, Santiago

#### Alumnos:

###### Torres Sosa Candelaria

###### Baiutti Bruno Augusto

###### Vazquez Zuloeta Fabian

###### Pinque Emanuel Leandro

###### (COMPLETAR)

#### Año 2026

---

## Objetivos

- Repasar conceptos fundamentales de Comunicaciones. Establecer un vínculo entre la capa física y modelos de transmisión/recepción de datos.

- Presentar Packet Tracer, un simulador de redes utilizado para el diseño y análisis de redes de dispositivos.

## Desarrollo

---

## Item 1

----

B.

#### Recordemos la formula de onda:

$\huge \lambda f = C$

##### Donde:

$\lambda:$Longitud de onda

$f$ : Frecuencia de la onda

$C$: Velocidad de la luz en el vacio 

##### Podemos hallar  la longitud de onda

$\lambda = \Delta_x = x_1 - x_0 = 120mm- 60mm = 60mm = 0.06m$

###### Ahora hallamos la frecuencia f

$f=\frac{C}{\lambda} = \frac{299792458 \frac{m}{s} }{0.06m}$

$\boxed{f \approx 5Ghz} $

---

C.

- La onda al tener una frecuencia de 5 GHz. Según la clasificación presentada por Stallings en la figura 4.1, esta frecuencia se encuentra dentro de la región de **MICROONDAS** del espectro electromagnético, más precisamente, pertenece a la banda **FRECUENCIAS SUPER ALTAS** (SHF Super High Frequency) que comprende desde 3 GHz ~ 30 GHz.

---

D.

- La tabla en la figura 4.1 describe como dispositivos de comunicaciones de datos a Antenas de Microondas y Radares en la banda SHF. Un ejemplo de uso cada vez más frecuente es en enlaces punto a punto a cortas distancias entre dispositivos, con aplicaciones típicas como circuitos cerrados de tv o interconexiones entre redes locales.

---

E.

- La tabla en la figura 4.1 describe como dispositivos de comunicaciones de datos a Antenas de Microondas y Radares en la banda SHF. Un ejemplo de uso cada vez más frecuente es en enlaces punto a punto a cortas distancias entre dispositivos, con aplicaciones típicas como circuitos cerrados de tv o interconexiones entre redes locales.

---

F.

- Si, la atenuación afecta a los sistemas de radar y antenas de microondas, ya que provoca una disminución de la potencia de la señal durante su propagación. Si, se puede notar en la señal Wi-Fi que a medida que nos alejamos del router la señal se debilita debido a la pérdida de potencia.

---

G.

- Si, el fenómeno de la atenuación afecta a las transmisiones de telefonía celular, porque la señal se atenúa a medida que aumenta la distancia y al atravesar obstáculos, como edificios y paredes. Las transmisiones por cable coaxial también son afectadas porque el cable presenta pérdidas de energía de la señal a medida que se propaga por el conductor. Y las transmisiones por fibra óptica sufren también la atenuación durante su propagación por la fibra.

---

## Item 2:

---

A.

- La transmisión representada en la imagen es una transmisión de tipo simplex ya que es unidireccional además de ser una transmisión digital síncrona donde ambos dispositivos de comunicación comparten un reloj.

B.

- El esquema actual de comunicación entre los dispositivos, no permite una comunicación bidireccional, por el hecho de tener una sola línea de datos. Tampoco permite alcanzar altas velocidades de transmisión porque el medio  puede sufrir de desfasajes por frecuencias con retardos donde el receptor podría no llegar a tiempo y no leer el dato. Además de que el medio propio actúa como un filtro pasa-bajos redondeando la señal provocando que sea más difícil diferenciar los niveles lógicos, una atenuación.

C.

Carácter en minúscula transmitido.



![image17.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image17.png)



D.

- Dada la pendiente en la señal proporcionada, un comportamiento esperado de un medio fisico, se deberia medir/muestrear la misma en un momento del tiempo donde el valor de tension se haya estabilizado, en este caso los momentos ideales son T0,T2,T4, evitando asi cualquier problema de incertidumbre o de rebote en la señal.

---

## Item 3:

---

- Contexto de transmisión de señales inalámbricas: las señales inalámbricas se transmiten por medio de ondas electromagnéticas, donde la antena juega un papel fundamental en la transmisión de estas ondas "irradiadas", ya que el tamaño de la antena depende de la longitud de onda (λ = c / f). El tamaño recomendado es de λ/4 o λ/2.
  Por qué esto afecta a las ondas cuadradas: las ondas cuadradas ocupan un ancho de banda muy grande (desde frecuencias casi de 0 Hz hasta frecuencias del orden de GHz, según los armónicos necesarios para reconstruir sus flancos). Por lo tanto, para las componentes de frecuencia más baja de la señal, la antena debería tener un tamaño del orden de kilómetros, haciendo esto físicamente inviable.
  Además, las bajas frecuencias tienen una mala propagación como ondas libres, ya que no se irradian bien en el aire.
  Por otro lado, está el problema de que en el aire no hay canales específicos para cada señal, por lo tanto tendríamos un solapamiento de señales. Es decir, si dos transmisores emiten señales en la misma frecuencia y son cercanos, el receptor no tendría manera sencilla de separarlas.
  Conclusión: por estas razones, tanto físicas como regulatorias (impuestas por el ENACOM en Argentina y la ITU internacionalmente), en lugar de transmitir tal cual una señal en banda base, se la usa para modular una onda portadora senoidal de alta frecuencia, trasladando su energía a una banda pasante específica (ya sea para WiFi, ondas de radio, etc.).



A.

Modulación por Desplazamiento de Fase Binaria.(BPSK)

En una portadora tenemos 3 casos de modulación:

- ASK: lo que varía es la amplitud de la onda portadora.

- FSK: lo que varía es la frecuencia de la onda.

- PSK: lo que varía es la fase (nuestro caso).

En nuestro caso, específicamente, se trata de una técnica de modulación BPSK (Binary Phase Shift Keying): la forma más simple de PSK, con exactamente dos valores de fase posibles, 0° o 180°.



B.

![image24.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image24.png)



C.

- 3 maneras, la 4-PSK, 8-PSK o QAM Consisten en el mismo principio, dividir la onda senoidal en los bits que vamos a ocupar, ejemplo; si  usamos la 4-PSK, la onda senoidal se va a dividir en 0°,90°, 180°  270°, si tenemos 01 dependiendo de cómo hayamos dividido la onda es como se completa esa parte de onda.

- En el caso de QAM se ocupa un diagram de constelación y prácticamente es lo mismo solo que cambia la amplitud, normalmente se ocupa de 3 o más bits.



D.

El BER (Bit Error Rate) es la proporción de bits que llegan con error respecto al total de bits transmitidos, en un intervalo de tiempo determinado. Básicamente mide que tan confiable es la transmisión: cuanto más bajo el BER, menos errores tiene el enlace.

El BER depende de varios factores: la relación señal-ruido (SNR) del canal, el tipo de modulación que se usa, y las características del canal en sí (atenuación, interferencia, etc).

En cuanto a cuál técnica tiene mejores prestaciones:

- ASK es la que peor se comporta frente al ruido, ya que la información viaja en la amplitud, y el ruido se suma directamente sobre la amplitud de la señal. Esto hace que sea más fácil confundir un símbolo con otro.

- FSK tiene mejor desempeño que ASK, porque la información está en la frecuencia y no en la amplitud, entonces el ruido (que afecta más que nada a la amplitud) le pega menos.

- PSK es la que mejores prestaciones tiene de las tres. Tampoco depende de la amplitud, y además los símbolos quedan más separados entre sí (en BPSK los dos estados posibles están a 180°, la máxima separación posible), por lo que es más difícil que el ruido la haga confundir un símbolo con otro.

---

## Item 4

---

A.

![image16.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image16.png)

B.

- #### Configuracion de IP y mascara:

![image9.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image9.png)

- ### Configuracion de SSID y seguridad

![](/home/emanuelp/.config/marktext/images/2026-08-19-14-23-25-image.png)



C.

- ### Se puede apreciar las siguientes bandas de frecuencia de 2.412Ghz a 2.452Ghz con saltos de 5Mhz. Opera en las frecuencias de microondas màs espacificamente SHF Super High Frecuency que comprende de 3Ghz a 30Ghz

![image22.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image22.png)

D.

- ### Conexion de ethernet establecida

![image21.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image21.png)

- ### Configuracion de placa de red
  
  
  
  ![image14.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image14.png)

E.

- ### Colocando la placa wifi a la laptop
  
  
  
  ![image10.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image10.png)

F.

- ### Interfaz de la laptop para establecer la conexion

![image12.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image12.png)

- ### Se puede apreciar la conectividad
  
  
  
  ![image19.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image19.png)



G.

- ### Se verifica la conectividad haciendo ping al router
  
  ![image11.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image11.png)

H.

- ### Laptop fisicamente cerca



![image23.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image23.png)

![image13.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image13.png)

#### Se concluye que existe una perdida de 25% de los paquetes con un tiempo de 13ms, se podria decir una conexion aceptable

- ### Laptop fisicamente lejos
  
  
  
  ![image18.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image18.png)



![image15.png](/home/emanuelp/Downloads/RC%20-%20Laboratorio%20Nº%201/images/image15.png)



### La conexion es demasido debil o inexistente tanto asi que agota el tiempo de espera del ping y directamente no recibe ningun paquete



- #### Se concluye que esto sucede por el fenomeno de la atenuacion, cuanta mayor distancia fisica las ondas electromagneticas del wifi se atenuan cada vez mas llegando un momento a ser indistinguibles del ruido electrico
