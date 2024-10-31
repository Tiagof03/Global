Análisis de Mutaciones en Secuencias de ADN

Descripción del Proyecto:

Este programa analiza secuencias de ADN en busca de mutaciones específicas. Representamos el ADN como una matriz de 6x6 en la que cada celda contiene una base nitrogenada: Adenina (A), Timina (T), Citosina (C) o Guanina (G). El objetivo es detectar mutaciones basadas en la repetición de cuatro bases nitrogenadas iguales en una orientación horizontal, vertical o diagonal.

Estructura del Proyecto

Este repositorio contiene los siguientes archivos en una única carpeta:

README.md: Este archivo, con las instrucciones de uso, lista de participantes, y un ejemplo de ejecución.
clases.py: Contiene las clases Detector, Mutador, Radiacion, Virus y Sanador, cada una con métodos específicos para la manipulación y análisis de la secuencia de ADN.
ejecutable.py: Script principal que permite interactuar con el programa, ingresar una secuencia de ADN y elegir entre detectar mutaciones, generar mutaciones o sanar el ADN.
Cómo Ejecutar el Programa
Para ejecutar el programa, sigue estos pasos:

Requisitos previos: Asegúrate de tener Python instalado (versión 3.6 o superior).

Ejecutar el programa:

Abre una terminal o línea de comandos en la carpeta del proyecto.
Ejecuta el archivo ejecutable.py con el siguiente comando:

python ejecutable.py #

Interacción:

El programa solicitará ingresar una secuencia de ADN en el formato de una lista de strings (por ejemplo: ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]).
Luego, el programa preguntará qué operación deseas realizar:
1: Detectar mutaciones.
2: Aplicar una mutación (horizontal, vertical o diagonal).
3: Sanar el ADN (crear una secuencia sin mutaciones).
Ejemplo de Ejecución:

Entrada:

Ingrese la secuencia de ADN en formato de lista de strings: ["AGATCA", "GATTCA", "CAACAT", "GAGCTA", "ATTGCG", "CTGTTC"]
¿Desea (1) detectar mutaciones, (2) mutarlo, o (3) sanarlo? 1 #

Salida esperada:

¿Es mutante? No #

Participantes del Grupo:

Tiago Funes
Emiliano Orobello
Sergio Haquin 

