import numpy as np
from collections import Iterable



###################################   LO QUE VIENE ES LAGRANGE   ###################################


def matriz_pitatoria(x):
    #esto lo hago para sacarme el pillo de ir concatenando lostas
    #en vez de eso, defino las dimensiones en un np array y después lo paso a lista
    # trucazo
    l_jm=np.random.rand(len(x),len(x))
    l_jm=l_jm.tolist()

    for j in range(len(x)):
        for m in range(len(x)):
            if j!=m:
                l_jm[j][m] = lambda x_in,x=x,j=j,m=m: np.divide((x_in-x[m]),(x[j]-x[m]))
            else:
                l_jm[j][m] = lambda x_in: 1
    #devuelve la matriz de funciones en forma de lista de listas
    return l_jm

def pitatoria_evaluar(x_in,lista_de_funciones):
    #tomo la lista que tiene listas dentro y la paso a nparray
    nplist=np.array(lista_de_funciones)
    #guardo su forma
    orig_shape = nplist.shape
    #lo transformo a una sola dimension
    nplist=nplist.reshape(-1)
    #evaluo el término dado para cada f dentro de la matriz
    evaluar=np.array(list(map(lambda f,x_in=x_in: f(x_in),nplist)))
    # devuelvo la forma original
    evaluar=evaluar.reshape(orig_shape)
    #pitato = np.prod(evaluar,axis=1)
    #devuelve, para un x, todas las pitatorias asolciadas, en un vector
    evaluar = np.prod(evaluar,axis=1)
    return evaluar


# polinomio con Lagrange

class Lagrange:

    def __init__(self,x_vec,y_vec):
        self.x = x_vec
        self.y = y_vec
        self.pit = matriz_pitatoria(x_vec)

    def eval_lagrange(self,x):
        if isinstance(x, Iterable):
            y=[]
            for element in x:

                eval = pitatoria_evaluar(element,self.pit)

                y.append(np.dot(eval,self.y))
            return y

        else:
            eval = pitatoria_evaluar(x, self.pit)
            return np.dot(eval,self.y)


################################### P2  ###################################





