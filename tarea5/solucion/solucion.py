from funciones import *
import numpy as np
import scipy.integrate as inte
import timeit

g=10
h=.001

# ============ PRIMERO SE INICIALIZAN LAS CLASES Setup =============


# primer caso
primer_caso = Setup(0, 0.00339, 0, 10, h, g, 1)

# segundo caso
segundo_caso= Setup(0, 0.00339, 0, 10, h, g, 2)

# tercer caso
tercer_caso = Setup(0, 0.00339, 0, 10, h, g, 3)

# cuarto caso
cuarto_caso = Setup(0, np.pi - 0.00339, 0, 10, h, g, 1)

# quinto caso
quinto_caso = Setup(0, np.pi - 0.00339, 0, 10, h, g, 2)

# sexto caso
sexto_caso = Setup(0, np.pi - 0.00339, 0, 10, h, g, 3)


# ============ SE EJECUTAN IMPLEMENTACIONES RK4 =============

print('Ejecutando RK4 para caso 1...')
primer_caso.RK4()
print('...RK4 para caso 1 finalizado')

print('Ejecutando RK4 para caso 2...')
segundo_caso.RK4()
print('...RK4 para caso 2 finalizado')

print('Ejecutando RK4 para caso 3...')
tercer_caso.RK4()
print('...RK4 para caso 3 finalizado')

print('Ejecutando RK4 para caso 4...')
cuarto_caso.RK4()
print('...RK4 para caso 4 finalizado')

print('Ejecutando RK4 para caso 5...')
quinto_caso.RK4()
print('...RK4 para caso 5 finalizado')

print('Ejecutando RK4 para caso 6...')
sexto_caso.RK4()
print('...RK4 para caso 6 finalizado')

# ============ GRÁFICOS BONITOS <3 =============

print('Gráfico xy caso 1')
primer_caso.plt_path()

print('Gráfico xy caso 2')
segundo_caso.plt_path()

print('Gráfico xy caso 3')
tercer_caso.plt_path()

print('Gráfico xy caso 4')
cuarto_caso.plt_path()

print('Gráfico xy caso 5')
quinto_caso.plt_path()

print('Gráfico xy caso 6')
sexto_caso.plt_path()

# ============ GRÁFICOS BONITOS <3 ESPÁCIOS DE FASE =============

print('Gráfico esp fase caso 1')
primer_caso.plt_phase()

print('Gráfico esp fase caso 2')
segundo_caso.plt_phase()

print('Gráfico esp fase caso 3')
tercer_caso.plt_phase()

print('Gráfico esp fase caso 4')
cuarto_caso.plt_phase()

print('Gráfico esp fase caso 5')
quinto_caso.plt_phase()

print('Gráfico esp fase caso 6')
sexto_caso.plt_phase()

# ============ SE GUARDAN LOS GRÁFICOS DE LOS CAMINOS =============
print('guardando gráficos de caminos...')
path = './../informe/imagenes/'
primer_caso.save_path(path+'img1.png')
segundo_caso.save_path(path+'img2.png')
tercer_caso.save_path(path+'img3.png')
cuarto_caso.save_path(path+'img4.png')
quinto_caso.save_path(path+'img5.png')
sexto_caso.save_path(path+'img6.png')
print('guardando finalizado!')

# ============ SE GUARDAN LOS GRÁFICOS DE LOS ESPACIOS DE FASE INTERESANTES =============

print('guardando gráficos de espacios de fase interesantes...')
primer_caso.save_phase(path+'img1_phase.png')
cuarto_caso.save_phase(path+'img4_phase.png')
print('guardando finalizado!')

# ============ SE CRNOMETRA MI IMPLEMENTEICHON DE RK4 Y LA DE SCIPY =============

setup1 = '''
import funciones as f
import numpy as np
g=20
h=.001
# primer caso
cuarto_caso = f.Setup(0, 0.00339, 0, 10, h, g, 1)
'''

code1 = '''
cuarto_caso.RK4()
'''

setup2 = '''
import funciones as f
import scipy.integrate as inte
import numpy as np
'''


code2 = '''
inte.solve_ivp(f.fun, (0,10), [np.pi-0.00339,0],max_step=0.001)
'''
print('cronometrando mi implementeichon RK4')
tiempo_mi_implementacion = timeit.timeit(stmt=code1, setup=setup1, number=100)/100
print('cronometraje finalizado!')

print('cronometrando integrador de scipy solve_ivp con RK45 (default)')
tiempo_scipy = timeit.timeit(stmt=code2, setup=setup2, number=100)/100
print('cronometraje finalizado!')

print('\n')

print('mi implementación tardó en promedio: ' +
      str(tiempo_mi_implementacion) +
      '\n'+'la de scipy tardó en promedio: ' +
      str(tiempo_scipy)
)

# ============ ESPACIO DE FASE USANDO SCIPY =============

sol_scipy = inte.solve_ivp(fun, (0,10), [np.pi-0.00339,0],max_step=0.001)

