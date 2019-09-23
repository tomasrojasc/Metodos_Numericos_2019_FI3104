import numpy as np
from funciones import *
import scipy.optimize as opti
import matplotlib.pyplot as plt
import timeit

# Se crean las constantes del problema
R = 4
R_2 = 3
V = 20
V_1 = 30


# Matriz ecuaciones de mallas
M = np.array([
    [2*R, 0, 0, R, 0, 0, 0, 0],
    [0, 2*R, 0, R, -R, 0, 0, 0],
    [0, 0, 2*R, 0, -R, 0, 0, 0],
    [R, R, 0, 2*R+R_2, 0, R_2, 0, 0],
    [0, -R, -R, 0, 2*R+R_2, 0, R_2, 0],
    [0, 0, 0, R_2, 0, R+R_2, 0, -R],
    [0, 0, 0, 0, R_2, 0, R+R_2, R],
    [0, 0, 0, 0, 0, -R, R, 2*R]
])



v_s = np.linspace(-200,200,2000)
sol = []
for element in v_s:
    sol.append(compuestaConCramer(element, M))
sol = np.array(sol)

plt.figure()
plt.plot(v_s, sol,'m')
plt.plot(10*np.ones(100), np.linspace(np.min(sol), np.max(sol), 100), '--', color='g')
plt.plot(30*np.ones(100), np.linspace(np.min(sol), np.max(sol), 100), '--', color='g')
plt.grid()
plt.legend(['Función objetivo','$V_2=10[V]$','$V_2=30[V]$'])
plt.title('Voltaje vs función objetivo')
plt.ylabel('Corriente objetivo (20-corriente)[A]')
plt.xlabel('Voltaje de la fuente variable')
plt.savefig('./../informe/img1.png',ppi=300)
plt.show()



# =================== cramer ====================


sol1_cramer = opti.bisect(compuestaConCramer, -100, -50, args=M)
sol2_cramer = opti.bisect(compuestaConCramer, 50, 100, args=M)

code1='''
opti.bisect(f.compuestaConCramer,-100,-50,args = M)
'''
code2='''
opti.bisect(f.usandoScipy,-100,-50,args = M)
'''

setup1='''
import numpy as np
import funciones as f
import scipy.optimize as opti
import matplotlib.pyplot as plt


# Se crean las constantes del problema
R = 4
R_2 = 3
V = 20
V_1 = 30


# Matriz ecuaciones de mallas
M = np.array([
    [2*R, 0, 0, R, 0, 0, 0, 0],
    [0, 2*R, 0, R, -R, 0, 0, 0],
    [0, 0, 2*R, 0, -R, 0, 0, 0],
    [R, R, 0, 2*R+R_2, 0, R_2, 0, 0],
    [0, -R, -R, 0, 2*R+R_2, 0, R_2, 0],
    [0, 0, 0, R_2, 0, R+R_2, 0, -R],
    [0, 0, 0, 0, R_2, 0, R+R_2, R],
    [0, 0, 0, 0, 0, -R, R, 2*R]
])

'''
n=1000
#tiempoCramer=timeit.timeit(stmt=code1,setup=setup1,number=n)/n
#tiempoPLU=timeit.timeit(stmt=code2,setup=setup1,number=n)/n


# =================== descomposición  ====================



sol1_desc = opti.bisect(usandoScipy, -100, -50, args = M)
sol2_desc = opti.bisect(usandoScipy, 50, 100, args = M)



SSS=[]

for i in range(len(v_s)):
    SSS.append(usandoScipy(v_s[i],M))





plt.figure()
plt.plot(v_s,SSS)
plt.plot(10*np.ones(100), np.linspace(np.min(sol), np.max(sol), 100), '--', color='g')
plt.plot(30*np.ones(100), np.linspace(np.min(sol), np.max(sol), 100), '--', color='g')
plt.grid()
plt.legend(['Función objetivo','$V_2=10[V]$','$V_2=30[V]$'])
plt.title('Voltaje vs función objetivo')
plt.ylabel('Corriente objetivo (20-corriente)[A]')
plt.xlabel('Voltaje de la fuente variable')
plt.savefig('./../informe/img2.png',ppi=300)
plt.show()


