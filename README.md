
# Glamper - Cuerpos de agua

Soluci贸n a la prueba propuesta por Glamper

## 馃搵 Descripci贸n del problema

Un cart贸grafo lo ha llamado a usted para que lo ayude a programar un sistema que le permita encontrar los cuerpos de agua m谩s grandes dentro de cualquier terreno de tama帽o arbitrario. Los terrenos vienen codificados en tablas de la siguiente manera: 

![Alt text](/assets/gampler-ejemplo.png?raw=true)

El cart贸grafo le indica a usted que, debido a las caracter铆sticas de los terrenos a analizar, todo lo que est茅 por debajo de 0 se considera agua, y el resto es terreno, como se puede apreciar el ejemplo anterior. 
Para el ejemplo anterior, los cuerpos de agua que existen, organizados por 谩rea (asumiendo que cada celda del mapa mide 1 m2), son:

1. 4 m2
2. 2 m2

Con base en la informaci贸n dada, desarrolle un sistema en Python que pueda ejecutar las siguientes tareas:
1. Generar mapas arbitrarios de 1000 x 1000, para poder evaluar la correcta ejecuci贸n del programa.
2. Identificar los cuerpos de agua presentes en un mapa dado de n x n, y organizarlos por 谩rea estimada. Se puede asumir que cada celda mide 1 m2 para la estimaci贸n de 谩rea de cada cuerpo de agua.

## 馃殌 Start
Inicie la aplicaci贸n usando el comando 

```
python main.py
```

Aparecer谩 un men煤 en la consola con la cual podr谩: 
1. Generar una matriz de 1000x1000
2. Generar una matriz de n x n
3. Generar la matriz de ejemplo (Imagen)
4. Salir de la aplicaci贸n

## 鉂? 驴C贸mo funciona?

La aplicaci贸n genera una matriz n x n (n se escoge de manera aleatoria), luego se rellena con valores entre 5 y -5, posteriormente cuando el usuario lo indique el algoritmo comienza a iterar el arreglo para buscar celdas donde el valor sea menor a 0, si as铆 lo es entonces buscar谩 alrededor de esa celda para estimar el 谩rea total donde los valores son menores que 0.

