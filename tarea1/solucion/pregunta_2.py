import scipy.integrate as inte
from funciones import *




#primero, hacviendo el cambio de variable pertinente, vamos a calcular la integral con
# la variable theta y no phi. phi=2*theta

#primero hacemos la funcion

def f(theta,k):
    return 2/(np.pi*np.sqrt(1-k**2*np.sin(theta)**2))

#la integral va de 0 a pi/2 con el cambio de variable
phi_0=np.linspace(0.0001,np.pi/2.,100)
k=np.sin(phi_0/2.)
solution_0=[]

for i in k:
    res=Trap_iter(f,0,np.pi/2.-.0000005,i)
    solution_0.append(res)


solution_1=[]

for i in k:
    res=Trap_iter(f,0,np.pi/2.-.0000005,i)
    solution_1.append(res)

solution_2=[]

for i in k:
    res=Trap_iter(f,0,np.pi/2.-.0000005,i)
    solution_2.append(res)
