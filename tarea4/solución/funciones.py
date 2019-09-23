import numpy as np
import scipy.linalg as la


def corrientesxcables(I):
    '''
    Esta func se encarga de, una vez calculadas las corrientes de la 1 a 8, devolver el vector correspondiente
    a las magnitudes de las corrientes que pasan por cada resistencia.
    :nota: Para que esto funcione, las corrientes deben entregarse en un vector, ordenadas de 1 a 8
    :param I: Las corrientes de la 1 a 8 en un vector
    :return: las magnitudes de todas las corrientes que pasan por las resistencias
    '''
    M = np.array([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, -1],
        [0, 0, 0, 0, 0, 0, 1, 1]
    ])
    return np.abs(M@I)

def crearVectorVoltajes(x):
    '''
    Func que se encarga de generar un vector de voltajes dado un valor para v_2
    :param x: Valor del voltaje V_2
    :return: Devuelve el vector de voltajes
    '''
    V = 20
    V_1 = 30
    return np.array([V, V, V, V_1, V_1, V_1, V_1 , x])


def cramer(M,b):
    '''
    implementacion del metodo de Cramer para resolver M x a = b
    donde M es una matriz cuadrada, y tanto a como b son vectores
    :param M: Matriz del sistema
    :param b: Vector de salida
    :return: devuelve el vector a
    '''
    sol = []
    delta = np.linalg.det(M)
    M_i = np.copy(M)
    for i in range(len(M[0,:])):
        M_i[:,i] = b
        delta_i = np.linalg.det(M_i)
        sol.append(delta_i/delta)
        M_i = np.copy(M)

    return np.array(sol)




def compuestaConCramer(x,M):
    '''
    Funcion que se va a entregar al buscador de ceros
    :param v_2: parametro que varia y donde se busca el 0, en este caso corresponde a los voltajes de la fuente variable
    :param M: matriz del sistema, en este caso corresponde a la matriz del metodo de mallas
    :param b: salida esperada, en este caso corresponde a los voltajes dado el v_2
    :return: devuelve el cero del sistema, vale decir, donde la corriente maxima es 20 amperes dado un valor x de v_2
    '''
    b = crearVectorVoltajes(x)
    I = cramer(M, b)
    corrientes_por_cables = corrientesxcables(I)
    maximo = np.max(corrientes_por_cables)
    salida = 20 - maximo
    return salida




def compuestaConCramer_nr(x,M):
    '''
    Funcion que se va a entregar al buscador de ceros
    :param v_2: parametro que varia y donde se busca el 0, en este caso corresponde a los voltajes de la fuente variable
    :param M: matriz del sistema, en este caso corresponde a la matriz del metodo de mallas
    :param b: salida esperada, en este caso corresponde a los voltajes dado el v_2
    :return: devuelve el cero del sistema, vale decir, donde la corriente maxima es 20 amperes dado un valor x de v_2
    '''
    b = crearVectorVoltajes(x)
    I = cramer(M, b)
    maximo = np.max(I)
    salida = 20 - maximo
    return salida



def encontrarDifSignosCramer(a, b, M, n):
    '''
    ve donde se cambia signo para poder encontrar los puntos para un bisect con compuesta Cramer
    :param f: funcion a evaluar
    :param a: limite inferior
    :param b: limite superior
    :param M: matriz para la funcion
    :param n: nro de puntos a evaluar en el intervalo
    :return: devuelve puntos para bisect
    '''
    estado = -100
    v = np.linspace(a,b,n)
    for i in range(len(v)):
        signo = np.sign(compuestaConCramer(v[i], M))
        if signo==0:
            return i
        if i==0:
            estado = signo
        else:
            if signo == 0:
                return i
            else:
                if signo != estado:
                    return [v[i-1],v[i]]
    print('no se puede usar bisect en este intervalo uwu')
    return None




def usandoScipy(x, M):
    '''
    Implementacion de descomposicion plu usando scipy
    :param x: valor de voltaje de v_2
    :param M: matriz del sistema
    :return: devuelve el valor maximo de corriente que pasa por el circuito usando el valor xpara v_2
    '''
    P,L,U = la.lu(M)
    b = np.transpose(P)@crearVectorVoltajes(x)
    y = la.solve_triangular(L, b)
    x = la.solve_triangular(U, y)
    corrientes = corrientesxcables(x)
    maximo = np.max(corrientes)
    return 20-maximo



def usandoScipy_nr(x, M):
    '''
    Implementacion de descomposicion plu usando scipy
    :param x: valor de voltaje de v_2
    :param M: matriz del sistema
    :return: devuelve el valor maximo de corriente que pasa por el circuito usando el valor xpara v_2
    '''
    P,L,U = la.lu(M)
    b = np.transpose(P)@crearVectorVoltajes(x)
    y = la.solve_triangular(L, b)
    corrientes = la.solve_triangular(U, y)
    maximo = np.max(corrientes)
    return 20-maximo