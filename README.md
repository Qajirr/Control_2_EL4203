# Control_2_EL4203
 Control 2 Programacion Avanzada
 
# Justificador de Texto

## Descripción

Este programa toma un archivo de texto y lo formatea para que cada línea tenga un ancho máximo de caracteres especificado por el usuario, distribuyendo los espacios de manera que el texto quede justificado. Se inspira en tres problemas clásicos de programación dinámica: Longest Common Substring, Word Break, y Word Wrap.

## Instalación

Asegúrese de tener Python 3 instalado en su sistema. También necesitará instalar `numpy` para el cálculo de programación dinámica.

```bash
pip install numpy
```
## Uso
Para ejecutar el programa:
```bash
python format_text.py
```

## Interfaz de Usuario
El programa presenta cuatro opciones:

    Crear un nuevo archivo.
    Leer un archivo existente.
    Actualizar el archivo existente con el texto formateado.
    Eliminar un archivo existente.

El usuario debe ingresar la ruta del archivo de texto y, para la opción de actualizar, el ancho máximo de caracteres por línea.

## Formato de Ejemplo
Entrada:
```bash
esto    es    un ejemplo  de como funcionarian :D 
```
maxWidth de 15:
```bash
esto
es  un  ejemplo de
como funcionarian :D

```
## Inspiraciones de Programación Dinámica
El proyecto utiliza conceptos de los siguientes problemas de programación dinámica:

    Word Wrap:
        La función word_wrap utiliza programación dinámica para dividir el texto en líneas según el ancho máximo especificado.

    Longest Common Substring:
        La función justify_text se inspira en Longest Common Substring para encontrar las palabras más largas y ajustar los espacios entre las palabras para que cada línea tenga exactamente maxWidth caracteres.

    Word Break:
        Aunque no se usa textualmente, el problema de Word Break inspira la separación del texto en palabras y la justificación de las líneas de texto.
## Inspiraciones de Programación Dinámica
Se incluyen los siguientes documentos de prueba:

    example.doc
    example.txt

Además de un archivo de salida de ejemplo:

    formateado.txt