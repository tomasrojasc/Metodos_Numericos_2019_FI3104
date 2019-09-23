import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpol
import pandas as pd
import funciones as f



# Primero importamos los datos, pero nos saltamos la primera línea ya ue es información irrelevante
data = pd.read_csv('./../GLB.Ts+dSST-short.csv',skiprows=1)

# ahora que tenemos el dataset, tomamos los años y la columna J-D

Y = data['Year']
J_D = data['J-D']

plt.plot(Y,J_D,'*')
plt.grid()
plt.show()

L=f.Lagrange(data['Year'],data['J-D'])
interpolacion_sp=interpol.CubicSpline(Y,J_D,bc_type='natural')
x_plot=np.linspace(2010,2018,200)

plt.plot(data['Year'],data['J-D'],'^')
plt.plot(2016, L.eval_lagrange(2016),'o')
plt.plot(2016,1.02,'*')
plt.plot(2016,interpolacion_sp(2016),'+')
plt.plot(x_plot,L.eval_lagrange(x_plot),'--')
plt.plot(x_plot,interpolacion_sp(x_plot),'--')
labe= ['data','lagrange','real','spline','interpollagrange','interpolspline']
plt.legend(labe)
plt.show()