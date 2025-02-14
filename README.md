# Codigo de la tortuga que dibuja un cubo 3D,

Este proyecto utiliza la biblioteca `turtle` de Python para dibujar dos cuadrados y conectarlos con lineas de puntos, creando un efecto visual de cubo 3D


## Requisitos

**Este proyecto fue desarrollado y probado en:**

    - Sistema operativo: Ubuntu 22.04
    - Python: 3.12.3
    - Entorno virtual: venv
    - Si al ejecutar obtienes el error `No module named '_tkinter'`, debes instalar el paquete de la interfaz Tk en tu sistema, con:
    
    - En Ubuntu:
      ```bash
      sudo apt-get install python3-tk
      ```

## Descripción del Código
El código realiza los siguientes pasos:
1. **Configuración inicial:** Se importa `turtle` y se establece la posición inicial.
2. **Dibujar el primer cuadrado:** Se crean puntos en los vértices y bordes del primer cuadrado y se almacenan en la lista `A`.
3. **Dibujar el segundo cuadrado:** Se repite el proceso con un desplazamiento, almacenando las coordenadas en la lista `B`.
4. **Conectar los cuadrados:** Se dibujan puntos intermedios entre los puntos correspondientes de `A` y `B`, creando la ilusión de profundidad.
5. 

## Cómo Ejecutar el Código

Se recomienda ejecutar dentro de venv 

1. **Crear y activar un entorno virtual:**
   - En Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Instalar dependencias (si es necesario):**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el script:**
   ```bash
   python cubo.py
   ```

Aparecerá una ventana mostrando el cubo formado por puntos.


