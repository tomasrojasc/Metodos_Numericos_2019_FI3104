import numpy as np
import funciones as f
import matplotlib.pyplot as plt
import scipy.interpolate as inter





n = np.linspace(2,50,49)

# se definen listas que van a contener a todos nuestros 'puntos muestrales'
lista_de_iteraciones_x = []
lista_de_iteraciones_y = []


# se evalúan esos ptos muestrales y se van concatenando
for i in n:
    x_aux=np.linspace(-1,1,i)
    lista_de_iteraciones_x.append(x_aux)
    lista_de_iteraciones_y.append(np.exp(-(x_aux**2)/.05))



lista_de_interpolacion_x = []
lista_de_interpolacion_y = []


# se hacen las interpolaciones, cada una con un linspace de 250 puntos
XX = np.linspace(-1,1,250)

# se van concatenando las interpolaciones
for i in range(len(lista_de_iteraciones_x)):
    lista_de_interpolacion_x.append(XX)
    lista_de_interpolacion_y.append(f.Lagrange(lista_de_iteraciones_x[i], lista_de_iteraciones_y[i]).eval_lagrange(XX))

maximos = []

for i in range(len(lista_de_interpolacion_y)):
    maximos.append(np.max(np.abs(lista_de_interpolacion_y[i]-np.exp(-(XX**2)/.05))))


plt.plot(n,maximos,'-^')
plt.grid()
plt.legend(['Desviacions máximas'])
plt.title('Iteración versus desvaciones de la función original\n interpolación con polinomios')
plt.xlabel('Numero de puntos')
plt.ylabel('Resta interpolación con función original')
plt.savefig('./../informe/P1_3.png',ppi=300)
plt.show()




#====================== LO MISMO PERO PARA SPLINE ============================================


lista_de_interpolacion_x_spline = lista_de_interpolacion_x
lista_de_interpolacion_y_spline = []

for i in range(len(lista_de_iteraciones_x)):
    x_actual = lista_de_iteraciones_x[i]
    lista_de_interpolacion_y_spline.append(inter.CubicSpline(x_actual,lista_de_iteraciones_y[i]))

maximos_spline = []

for i in range(len(lista_de_interpolacion_y_spline)):
    maximos_spline.append(np.max(np.abs(lista_de_interpolacion_y_spline[i](XX)-np.exp(-(XX**2)/.05))))


plt.figure()
plt.plot(n,maximos_spline,'-^')
plt.grid()
plt.legend(['Desviaciones máximas'])
plt.title('Iteración versus desvaciones de la función original\n interpolación Spline')
plt.xlabel('Numero de puntos')
plt.ylabel('Resta interpolación con función original')
plt.savefig('./../informe/P1_S_3.png',ppi=300)
plt.show()



