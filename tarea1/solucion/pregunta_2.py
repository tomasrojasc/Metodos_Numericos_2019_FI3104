import scipy.integrate as inte
from funciones import *
import matplotlib.pyplot as plt



#primero, hacviendo el cambio de variable pertinente, vamos a calcular la integral con
# la variable theta y no phi. phi=2*theta

#primero hacemos la funcion

def f(theta,k):
    '''
    Define la funcion que vamos a usar
    :param theta: corresponde a la variable luego del cambio de variable
    :param k: corresponde a la constante que liga el
    :return: devuelve la función
    '''
    return 2/(np.pi*np.sqrt(1-k**2*np.sin(theta)**2))

#la integral va de 0 a pi/2 con el cambio de variable
phi_0=np.linspace(0,np.pi/2.,100)
k=np.sin(phi_0/2.)

def Evalua(f,a,b,k):
    solution_0 = []
    for i in k:
        res = Trap_iter(f, a, b, i)
        solution_0.append(res[0])
    return solution_0, res[1]




solution,n=Evalua(f,0,np.pi/2.-.0000005,k)


plt.plot(phi_0,solution)
plt.title('Integral para distintos $\phi_0$ (n= {} )'.format(n))
plt.ylabel('Valor de la integral')
plt.xlabel('Valor de $\phi_0$')
plt.grid(True)
plt.savefig('../informe/P2.png',ppi=300)
plt.show()

def Trap_scipy(f,x,k):
    sol=[]
    for element in k:
        sol.append(inte.trapz(f(x,element),x))
    return sol