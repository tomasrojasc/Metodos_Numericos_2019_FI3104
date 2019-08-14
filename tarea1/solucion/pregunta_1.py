#se importa numpy y matplotlib
import math
import matplotlib.pyplot as plt

#se importan las funciones creadas para esta tarea
from funciones import *
#-----------------------------

#se hacen cálculos usando float32
h_float32, ref_float32, O_1_float32, O_4_float32= Setup(np.sin, 1.339, 17, np.float32, math.cos, lambda x:x/2)

#tomamos las diferencias entre cada aproximación y el
#valor de la función implementada en python

error_O1_float32=O_1_float32-ref_float32
error_O4_float32=O_4_float32-ref_float32
#----------------------------------
#----------------------------------
#se hacen cálclos usando float64
h_float64, ref_float64, O_1_float64, O_4_float64= Setup(np.sin, 1.339, 17, np.float64, math.cos, lambda x:x/2)

#tomamos las diferencias entre cada aproximación y el
#valor de la función implementada en python

error_O1_float64=O_1_float64-ref_float64
error_O4_float64=O_4_float64-ref_float64

#----------------------------------
#----------------------------------

h_float128, ref_float128, O_1_float128, O_4_float128= Setup(np.sin, 1.339, 17, np.float128, math.cos, lambda x:x/2)

#tomamos las diferencias entre cada aproximación y el
#valor de la función implementada en python

error_O1_float128=O_1_float128-ref_float128
error_O4_float128=O_4_float128-ref_float128


#----------------------------------
#----------------------------------


#graficamos las fiderencias vs el número de la potencia de 0.1
#al que corresponde el valor de h utilizado
fig,AX=plt.subplots(nrows=3,ncols=1,sharex=True)
(ax1,ax2,ax3)=AX

ax1.set_yscale('log')



ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')



#datos gráfico float32
ax1.plot(h_float32,O_1_float32,'-*')
ax1.plot(h_float32,O_4_float32,'-o')
ax1.plot(h_float32,ref_float64*np.ones(len(h_float32)),'--')

ax1.grid(True)

#datos gráfico float64
ax2.plot(h_float64,O_1_float64,'-*')
ax2.plot(h_float64,O_4_float64,'-o')
ax2.plot(h_float64,ref_float64*np.ones(len(h_float64)),'--')

ax2.grid(True)

#datos gráfico float128
ax3.plot(h_float128,O_1_float128,'-*')
ax3.plot(h_float128,O_4_float128,'-o')
ax3.plot(h_float128,ref_float128*np.ones(len(h_float128)),'--')

ax3.grid(True)


#títulos de cada subplot
AX[0].set_title('Float32')
AX[1].set_title('Float64')
AX[2].set_title('Float128')

#titulos eje y
for i in range(3):
    AX[i].set_ylabel('derivada')


AX[2].set_xlabel('Tamaño h')
fig.legend(['O(h)','O($h^4$)'])
fig.tight_layout()
plt.show()



