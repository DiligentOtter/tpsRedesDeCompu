# Universidad Nacional de Córdoba
### Facultad de Ciencias Exactas, Físicas y Naturales

![alt text](images/image3.png)

# Redes de Computadoras
## Trabajo Práctico de Nº 6 - Laboratorio: Construccion de cable UTP y conexion en red LAN

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

Parte 1)
    El armado de un cable de red de transmisión directa, también conocido como cable derecho, es un procedimiento técnico fundamental en las telecomunicaciones que garantiza la correcta transmisión de datos entre dispositivos como computadoras, switches y routers. Este proceso se rige bajo la norma internacional ANSI/TIA/EIA-568, la cual define el esquema exacto de distribución y orden de los cables dentro de los conectores. La norma contempla dos variantes principales para el código de colores: T568A y T568B. Ambas ofrecen exactamente el mismo rendimiento técnico y ancho de banda, diferenciándose únicamente en el intercambio de posiciones entre el par verde y el par naranja. Para armar un cable directo, la regla básica es replicar el mismo estándar en ambos extremos del cable, siendo el esquema T568B el más utilizado en la industria.

    Procedimiento de crimpado de cable de red RJ-45
Materiales necesarios
- Cable de par trenzado UTP categoría 5e o 6
- Dos conectores RJ-45 transparentes
- Pinza crimpadora o ponchadora para conectores de 8 pines
- Pelacables o la cuchilla de la crimpadora
- (Opcional) Comprobador o tester de cables LAN

#### Desarrollo
1. Preparación del cable

    Con el pelacables o la cuchilla de la crimpadora, retiramos unos 3 cm del revestimiento exterior de plástico de un extremo del cable. Tuvimos cuidado de no mellar ni cortar el aislamiento de los ocho hilos de cobre internos.

    Luego separamos y destrenzamos con cuidado los cuatro pares de hilos. 

2. Organización de los hilos (norma T568B)

    Ordenamos los hilos en una tira plana, de izquierda a derecha, según esta secuencia:

    |Posición|	Color|
    |-----|-----|
    |1	|Blanco / naranja|
    |2	|Naranja|
    |3	|Blanco / verde|
    |4	|Azul|
    |5	|Blanco / azul|
    |6	|Verde|
    |7	|Blanco / marrón|
    |8	|Marrón|

    Sostuvimos la tira firmemente, cerca del borde de la cubierta externa. Cortamos la punta del manojo a 90 grados con la navaja recta de la crimpadora, dejando los hilos con una longitud uniforme de 1,2 a 1,4 cm.

    Esta medida es crítica: los hilos deben llegar hasta el fondo del conector, y la funda exterior tiene que entrar lo suficiente para quedar sujeta por el mecanismo de retención del RJ-45.

3. Inserción en el conector

    Tomamos el conector RJ-45 con la pestaña de fijación hacia abajo y los contactos dorados hacia arriba. Introducimos los ocho hilos alineados.

    ![alt text](images/photo_2.jpg)

    Empujamos suavemente hasta verificar, a través del plástico transparente, que cada hilo llegó al fondo del conector y que el orden de colores no se alteró.

4. Crimpado

    Insertamos el conector en la ranura correspondiente de la pinza crimpadora y presionamos firmemente los mangos hasta completar todo el recorrido del mecanismo.

    ![alt text](images/photo_1.jpg)

    Durante este paso, las cuchillas empujan los contactos metálicos para perforar la funda de cada hilo y establecer contacto eléctrico. Al mismo tiempo, una pestaña plástica sujeta la cubierta exterior del cable para resistir tirones.

    Repetí exactamente el mismo procedimiento en el extremo opuesto, manteniendo el esquema T568B.

5. Verificación

    Probamos ambos extremos en el tester de red. Si el crimpado es correcto, los ocho LED se encenderán en secuencia, en el mismo orden, en ambos lados. Como se muestra a continuacion.
    ![alt text](images/video_1.gif)