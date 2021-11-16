# EJERCICIO de matplotlib 02
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    # Crear acá su gráfico
    figura =plt.figure()
    figura.suptitle('multi ploteo de lineas')
    plt.plot(y1, marker='+',markeredgecolor='k',color='blue',linestyle='-',label='y1=x**2')
    plt.plot(y2, marker='+', markeredgecolor='y', color='red', linestyle='--', label='y1=x**3')
    plt.grid()
    plt.ylabel('y1')
    plt.xlabel('y2')
    plt.legend()
    plt.show()
    print("terminamos")