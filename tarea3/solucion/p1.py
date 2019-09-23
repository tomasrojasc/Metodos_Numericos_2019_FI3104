import numpy as np
from funciones import *
import matplotlib.pyplot as plt
import scipy.interpolate as inter




###################################   LO QUE VIENE ES LAGRANGE   ###################################


#primero hacemos una división equiespaciada como pide el enunciado
#definimos x
x = np.linspace(-1,1,5)
#definimos y
y = np.exp(-(x**2)/.05)


#Para la interpolación, creamos un objeto Lagrange
inter_lagrange = Lagrange(x,y)

# ahora interpolamos, para eso usamos un x que pase por los puntos pedidos, pero que además pase por otros puntos

X = np.linspace(-1,1,5*10)
Y = inter_lagrange.eval_lagrange(X)

#graficamos toodo junto
plt.figure()
plt.plot(x,y,'o')
plt.plot(X,Y)
plt.grid()
plt.plot(np.linspace(-1,1,200),np.exp(-(np.linspace(-1,1,200)**2)/.05),'--')
plt.title('Interpolación de Lagrange')
plt.legend(['Puntos de la función','Interpolación','Función Original'])
plt.savefig('./../informe/P1_1.png',ppi=300)

plt.show()



# se definen listas que van a contener a todos nuestros 'puntos muestrales'
lista_de_iteraciones_x = []
lista_de_iteraciones_y = []


n = [5,10,15,20,30]


# se evalúan esos ptos muestrales y se van concatenando
for i in n:
    x_aux=np.linspace(-1,1,i)
    lista_de_iteraciones_x.append(x_aux)
    lista_de_iteraciones_y.append(np.exp(-(x_aux**2)/.05))

# se definen listas que van a contener a todas nuestras interpolaciones
lista_de_interpolacion_x = []
lista_de_interpolacion_y = []


# se hacen las interpolaciones, cada una con un linspace de 100 puntos
XX = np.linspace(-1,1,100)

# se van concatenando las interpolaciones
for i in range(len(lista_de_iteraciones_x)):
    lista_de_interpolacion_x.append(XX)
    lista_de_interpolacion_y.append(Lagrange(lista_de_iteraciones_x[i], lista_de_iteraciones_y[i]).eval_lagrange(XX))

#se crea una nueva figura donde irán todos los gráficos de nuestras interpolaciones juntas
plt.figure()


#acá se van a concatenar los nombres de cada curva
legend = []
plt.plot(XX,np.exp(-(XX**2)/.05), linewidth=4)
legend.append('Función original')
plt.grid()


#se empieza a graficar todas las interpolaciones juntas
for i in range(len(lista_de_interpolacion_x)):
    plt.plot(lista_de_interpolacion_x[i],lista_de_interpolacion_y[i],'--')
    #se concatena el nombre que le corresponde a la curva
    legend.append('Interpolación con {} puntos'.format(n[i]))




# se pone la leyenda en el gráfico
plt.legend(legend)
# se guarda el gráfico
plt.savefig('./../informe/P1_2.png',ppi=300)
#se muestra el gráfico
plt.show()


###################################   FIN LAGRANGE   ###################################



###################################   LO QUE VIENE ES SPLINE   ###################################


# Lo primero es tomar las listas de puntos que utilizamos en la parte anterior y
# usamos spline para hacer exactamente lo mismo


# se definen listas que van a contener a todas nuestras interpolaciones
lista_de_interpolacion_x_spline = lista_de_interpolacion_x
lista_de_interpolacion_y_spline = []


# se van concatenando las interpolaciones
for i in range(len(lista_de_iteraciones_x)):
    lista_de_interpolacion_y_spline.append(inter.CubicSpline(lista_de_iteraciones_x[i],
                                                      lista_de_iteraciones_y[i],
                                                      bc_type='natural')
                                           )


plt.figure()
plt.plot(x,y,'o')
plt.plot(lista_de_interpolacion_x_spline[0],lista_de_interpolacion_y_spline[0](lista_de_interpolacion_x_spline[0]))
plt.plot(np.linspace(-1,1,200),np.exp(-(np.linspace(-1,1,200)**2)/.05),'--')
plt.grid()
plt.title('Interpolación Spline')
plt.legend(['Puntos de la función','Interpolación','Función Original'])
plt.savefig('./../informe/P1_S_1.png',ppi=300)
plt.show()





plt.figure()
#acá se van a concatenar los nombres de cada curva
legend_spline = []
plt.plot(XX,np.exp(-(XX**2)/.05), linewidth=4)
legend_spline.append('Función original')
plt.grid()

#se empieza a graficar todas las interpolaciones juntas
for i in range(len(lista_de_interpolacion_x_spline)):
    x_actual = lista_de_interpolacion_x_spline[i]
    plt.plot(x_actual,lista_de_interpolacion_y_spline[i](x_actual),'--')
    #se concatena el nombre que le corresponde a la curva
    legend_spline.append('Interpolación con {} puntos'.format(n[i]))


# se pone la leyenda en el gráfico
plt.legend(legend_spline)
# se guarda el gráfico
plt.savefig('./../informe/P1_S_2.png',ppi=300)
#se muestra el gráfico
plt.show()







