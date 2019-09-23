import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interpol
import pandas as pd
from funciones import *
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()




# Primero importamos los datos, pero nos saltamos la primera línea ya ue es información irrelevante
data = pd.read_csv('./../GLB.Ts+dSST-short.csv',skiprows=1)

# ahora que tenemos el dataset, tomamos los años y la columna J-D

Y = data['Year'].to_numpy()
J_D = data['J-D'].to_numpy()



#lagrange
polinomial=Lagrange(Y,J_D)

#spline anual

CS_A=interpol.CubicSpline(Y,J_D,bc_type='natural')

#Ahora spline pero mensual

#creo fechas por mes para los datos que tengo
fechas=pd.date_range(start='Jan 2010',end='Jan 2019',freq='m')
fechas=fechas[np.where(fechas.year!=2016)]
#reordeno los datos para ponerlos con sus fechas correspondientes
datitos=data.iloc[:,1:13].to_numpy().reshape(-1)

#se crea el nuevo DataFrame
meses=pd.DataFrame(datitos,columns=['data'])
meses.index=fechas

#Ahora tomo todas las fechas
fechas_2=pd.date_range(start='Jan 2010',end='Jan 2019',freq='m')

#interpololos datos
CS=interpol.CubicSpline(fechas.values.astype(float),datitos,bc_type='natural')

#un df con los datos interpolados por cubic spline
datos_interpolados_por_mes=pd.DataFrame(data=np.array(CS(fechas_2.values.astype(float))).reshape(-1))
#le pongo los índices adecuados
datos_interpolados_por_mes.index=fechas_2

promedio_2016_interpolado_por_meses=np.average(datos_interpolados_por_mes.iloc[
                                                   np.where(datos_interpolados_por_mes.index.year==2016)]
                                               )




Y=np.append(Y,2016)
order = np.argsort(Y)




J_D=np.append(J_D,1.02)
plt.plot(Y[order],J_D[order],'o--')
plt.plot(2016,polinomial.eval_lagrange(2016),'*')
plt.plot(2016,CS_A(2016),'*')
plt.plot(2016,promedio_2016_interpolado_por_meses,'*')
plt.grid()
plt.legend(['Datos reales',
            'Interpolación polinomial anual',
            'Interpolación Spline anual',
            'Interpolación Spline mensual promediada']
           )

plt.savefig('./../informe/P2_1.png',ppi=300)
plt.show()


DATOS=pd.DataFrame(datitos)
DATOS.index= fechas
DATOS=DATOS.resample('m').mean()

plt.figure()
plt.grid()
plt.plot(DATOS,'*--')
plt.savefig('./../informe/P2_2.png',pp1=300)
plt.show()