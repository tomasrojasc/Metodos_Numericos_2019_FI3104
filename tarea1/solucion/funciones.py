import numpy as np

#P1:



#Método con  error de órden O(h)
def DerivadaO1(f,x,h):
    return (f(x+h)-f(x))/h

#Método con error de órden O(h^4)
def DerivadaO4(f,x,h):
    return (-f(x+2*h)+8*f(x+h)-8*f(x-h)+f(x-2*h))/(12*h)

#funcion que se encarga de preparar toodo para graficar
def Setup(f,x,iteraciones,datatype,reff=None,g=None):

    h=datatype(0.1)**np.arange(iteraciones)
    f=f
    x=x*np.ones(len(h),dtype=datatype)

    #esto es para poner una función dentro de la función externa
    if g!=None:
        intermedio = g(x)
    else:
        intermedio = x

    if reff!=None:
        ref=reff(intermedio[0])
    else:
        ref=None

    #calculamos los valores para la aprocimación que deja O(h)
    O_1=DerivadaO1(f,intermedio,h)


    #calculamos los valores para la aprox que deja O(h^4)
    O_4=DerivadaO4(f,intermedio,h)

    return h,ref, O_1, O_4

def Aprox2nd(f,a,b,h):
    x=np.linspace(a,b,(b-a)/h)
    h=np.ones(len(x))*h
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)


#=======================================================================================================================


#P2:

def Conv(I_0, I_1):
    return np.divide(np.abs(I_1-I_0),np.abs(I_0))


def Trap_iter(f, a, b, k):
    n = 100
    error = .01
    delta = (b-a)/n
    #se crean particiones pertinentes
    partition_0 = np.linspace(a,b,n)
    partition_1 = np.linspace(a,b,2*n)
    #evaluaciones de integrales
    I_0=delta*.5*f(partition_0[0],k)+f(partition_0[-1],k)+2*np.sum(f(partition_0[1:-1],k))
    I_1=I_0*.5+np.sum(f(partition_1[1::2],k))*delta*.5
    #redefino cositas
    n=2*n
    delta=(b-a)/n
    #criterio de convergencia
    while Conv(I_0, I_1) >= error:
        n=2*n
        p = np.linspace(a,b,n)
        I_n = I_1*.5*delta+np.sum(f(p[1::2],k))*delta*.5
        I_0 = I_1
        I_1 = I_n
        delta=delta/2

    #devuelve una integral mejor basado en las últimas dos calculadas con método de trapecio
    return (4/3)*I_1-(1/3)*I_0
