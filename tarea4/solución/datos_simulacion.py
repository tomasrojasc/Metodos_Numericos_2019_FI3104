import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./simulacion.txt',sep='	')
data.set_index('v6',inplace=True)

data=np.abs(data)
maximo=np.max(data.T)

plt.plot(data.index.values,20-maximo.values)
plt.grid()
plt.title('Datos simulación LTSpice')
plt.xlabel('Voltaje $V_2$')
plt.ylabel('Corriente máxima dado un $V_2$')
plt.savefig('./../informe/simulacion.png',ppi=300)
plt.show()