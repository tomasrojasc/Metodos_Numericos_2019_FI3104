import numpy as np
import matplotlib.pyplot as plt


def f1(t, Omega, phi, g, lambda_var):
    '''
    funcion que decribe la primera edo de primer orden del sistema
    :param t: tiempo a evaluar
    :param phi: angulo a evaluar
    :param Omega: omega a evaluar
    :param g: aceleracion de gravedad
    :param lambda_var: lambda del enunciado
    :return: devuelve la funcion evaluada en ese tiempo en ese omega
    '''
    a = 8*(lambda_var**2)*np.cos(lambda_var*4*np.sqrt(g)*t)
    return -g*(1+a)*np.sin(phi)

def f2(t, Omega, phi):
    '''
    funcion que decribe la segunda edo de primer orden del sistema
    :param t: tiempo a evaluar
    :param phi: angulo a evaluar
    :param Omega: omega a evaluar
    :return: la funcion evaluada en ese omega
    '''
    return Omega

def RK4_2(f1, f2, y1_0, y2_0, t_0, t_max, h, *args):
    '''
    implementacion RK4 para una edo de 2do orden
    :param f_1: funcion que describe la primera ecuacion
    :param f_2: funcion que describe la segunda ecuacion
    :param y1_0: cond inicial primera func
    :param y2_0: cond inicial segunda func
    :param t_0: tiempo inicial
    :param t_max: tiempo upper bound
    :param h: step
    :param args: cualquier cosa extra que reciba alguna funcion
    :return: devuelve la solucion para la edo de 2do orden
    '''

    n = int((t_max - t_0)/h)
    h = (t_max-t_0)/n
    t = np.linspace(t_0, t_max, n)
    t[0] = t_0
    y1, y2 = np.zeros(n), np.zeros(n)
    y1[0], y2[0] = y1_0, y2_0

    for i in range(n-1):
        k_1 = f1(t[i], y1[i], y2[i], *args)
        c_1 = f2(t[i], y1[i], y2[i])
        k_2 = f1(t[i]+h*.5, y1[i]+h*.5*k_1, y2[i]+h*.5*c_1, *args)
        c_2 = f2(t[i]+h*.5, y1[i]+h*.5*k_1, y2[i]+h*.5*c_1)
        k_3 = f1(t[i]+h*.5, y1[i]+h*.5*k_2, y2[i]+h*.5*c_2, *args)
        c_3 = f2(t[i]+h*.5, y1[i]+h*.5*k_2, y2[i]+h*.5*c_2)
        k_4 = f1(t[i]+h, y1[i]+h*k_3, y2[i]+h*c_3, *args)
        c_4 = f2(t[i]+h, y1[i]+h*k_3, y2[i]+h*c_3)
        y1[i+1]=y1[i]+(h/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)
        y2[i+1]=y2[i]+(h/6)*(c_1 + 2*c_2 + 2*c_3 + c_4)

    return t, y2, y1


def pos_masa(t, phi, lambda_var,g):
    '''
    devuelve arreglos que especifican la posicion de la masa en cada momento del tiempo
    :param t: tiempo en el cual tiene alguna pos dada (arreglo de tiempos que devuelve RK4
    :param phi: angulo que define la coord de la masa
    :param lambda_var: lambda usado
    :param g: gravedad usada
    :return: devuelve la pos de la masa en coord cartesiandas
    '''
    x = np.sin(phi)
    omega = 4*np.sqrt(g)*lambda_var
    y = -np.cos(phi)-.5*np.cos(omega*t)
    return x, y

def energia(t, phi, dphi, g, lambda_var):
    '''
    calcula la energia para un tiempo t
    :param t: tiempos a evaluar
    :param phi: vector de angulos
    :param dphi: vector de velocidades angulares
    :param g: gravedad
    :param lambda_var: lambda usada
    :return: vector de energias
    '''

    omega = 4 * np.sqrt(g) * lambda_var
    E_k_f_1 = .5 * (dphi ** 2)
    E_k_f_2 = 2 * np.sqrt(g) * lambda_var * np.sin(omega * t) * np.sin(phi) * dphi
    E_k_f_3 = 2 * g * (lambda_var ** 2) * (np.sin(omega * t)) ** 2
    E_k_f = E_k_f_1 + E_k_f_2 + E_k_f_3
    E_p_f = -g * (np.cos(phi) + .5 * np.cos(omega * t))
    E = E_k_f + E_p_f
    return E, E_k_f, E_p_f


# ============ CLASE SETUP =============


class Setup:
    '''
    clase que facilita el manejo de la tarea
    '''
    def __init__(self, dphi_0, phi_0, t_0, t_max, h, g, lambda_var):
        '''
        metodo init de la clase Setup
        :param dphi_0: vel ang nicial
        :param phi_0: ang inicial
        :param t_0: tiempo inicial
        :param t_max: tiempo upper bound
        :param h: step
        :param args: cualquier cosa extra que reciba alguna funcion
        :return: None, pero setea valores
        '''
        self.dphi_0 = dphi_0
        self.phi_0 = phi_0
        self.t_0 = t_0
        self.t_max = t_max
        self.h = h
        self.g = g
        self.lambda_var = lambda_var
        self.phi = None
        self.dphi = None
        self.t = None
        self.x = None
        self.y = None
        self.path = None
        self.phase = None
        self.E = None
        self.E_k = None
        self.E_p = None

    def RK4(self):
        '''
        implementa RK4 en la clase
        :return: None
        '''
        self.t, self.phi, self.dphi = RK4_2(f1,
                                            f2,
                                            self.dphi_0,
                                            self.phi_0,
                                            self.t_0,
                                            self.t_max,
                                            self.h,
                                            self.g,
                                            self.lambda_var)

        return None

    def plt_phase(self):
        '''
        metodo que muestra el espacio de fase
        :return: None
        '''
        assert self.dphi is not None, self.phi is not None

        self.phase = plt.figure()
        plt.title('Espacio de Fase ($m=1$)')
        plt.xlabel('Posición generalizada')
        plt.ylabel('Momentum generalizado')
        plt.grid()
        plt.plot(self.phi, self.dphi)
        plt.show()
        return None

    def plt_path(self):
        '''
        metodo que muestra el espacio con la pos de la masa
        :return: None
        '''
        assert self.dphi is not None, self.phi is not None
        self.x, self.y = pos_masa(self.t, self.phi, self.lambda_var, self.g)

        self.path = plt.figure()
        plt.xlabel('Posición en el eje horizontal')
        plt.ylabel('Posición en el eje vertical')
        plt.grid()
        plt.plot(self.x, self.y)
        plt.show()

        return None

    def save_path(self, direccion):
        '''
        guarda plot del recorrido de la masa
        :param direccion: donde se guarda
        :return: None
        '''
        assert self.path is not None

        self.path.savefig(direccion, ppi=330)
        return None

    def save_phase(self, direccion):
        '''
        guarda plot del espacio de fase
        :param direccion: donde se guarda
        :return: None
        '''
        assert self.phase is not None

        self.phase.savefig(direccion, ppi=330)
        return None

    def calc_E(self):
        '''
        setea la perdida de energía
        :return: cambio en la energia
        '''
        self.E, self.E_k, self.E_p = energia(self.t, self.phi, self.dphi, self.g, self.lambda_var)
        return self.E, self.E_k, self.E_p

    def plt_E(self):
        '''
        metodo que muestra la energía como función del tiempo
        :return: None
        '''
        self.calc_E()
        plt.figure()
        plt.title('Energía vs tiempo')
        plt.xlabel('Tiempo')
        plt.ylabel('Energía')
        plt.plot(self.t, self.E)
        plt.show()

    def plt_Ek(self):
        '''
        metodo que muestra la energía cinética como función del tiempo
        :return: None
        '''
        self.calc_E()
        plt.figure()
        plt.title('Energía cinética vs tiempo')
        plt.xlabel('Tiempo')
        plt.ylabel('Energía')
        plt.plot(self.t, self.E_k)
        plt.show()

    def plt_Ep(self):
        '''
        metodo que muestra la energía potencial como función del tiempo
        :return: None
        '''
        self.calc_E()
        plt.figure()
        plt.title('Energía potencial vs tiempo')
        plt.xlabel('Tiempo')
        plt.ylabel('Energía')
        plt.plot(self.t, self.E_p)
        plt.show()


# ============== FUNCIONES PARA SCIPY  ===================

def fun(t, U):
    '''
    funcion que se le pasa al integrador
    :param t: escalar que corresponde a los tiempos a evaluar
    :param U: vector, en este caso U[0] es phi_0 y U[1] es Omega(0) ya que son las ci del sistema
    :return: devuelve un vector con las derivadas de cada variable del sistema
    '''
    return [U[1], -10*(1+8*np.cos(4*np.sqrt(10)*t))*np.sin(U[0])]