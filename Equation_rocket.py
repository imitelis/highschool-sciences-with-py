#Eq empuje cohete

#importar libreria de matematicas
from math import pi
#importar libreria para hacer espacio lineal
import numpy as np
#importar libreria para hacer graficas
import matplotlib.pyplot as plt


#Todas las unidades estan en SI, sistema internacional de medidas
#uso float para que el sistema reconozca que se trata de un número real, con dígitos

#Datos
m = float(0.5) #peso del cohete sin combustible, 0.5 kg
r_1 = float(0.1) #radio de orificio de escape del cohete, con radio de 0.1 m (10 cm)
S_1 = float(r_1*(pi**2)) #area de orificio de escape del cohete, con radio r_1
r_2 = float(0.4) #radio de superficie del tanque que conforma el cohete, con radio de 0.2 m (20 cm)
S_2 = float(r_2*(pi**2)) #area de superficie del tanque del cohete, con radio r_2
A = S_1 #llamar al area S_1 como A, por notación
N = float(10) #numero de veces accionada la bomba de aire
g = float(9.8) #constante aceleración gravedad, 9.8 m/s**2
p_atm = float(1.013) #presion atmosferica, supongamos cerca del nivel del mar en milibares
h = float(1.2) #altura total del tanque del cohete, 1.2 m
V_b = float(4) #volumen de la bomba con la que se prepara el cohete, 4 L
v_0 = float(100) #velocidad inicial a la que desciende el nivel de combustible en el tanque, 100 m/s
h_0 = float(1.1) #altura del combustible en el tanque del cohete, 1.1 m
t = np.linspace(0,100,100) #tiempo, desde 0 hasta 100 da 100 valores, 60 seg de vuelo
v_1 = h_0 - (0.1)*t #velocidad del flujo pasando por A., b alguna constante, b=0.1
h_t = -(v_1*t) #altura del combustible en el tanque variando respecto al tiempo
p_t = p_atm*(1 + ((N*V_b)/(S_1*(h - (h_0 - (0.1)*t))))) #presion en instante t, tambien llamado presion absoluta
p_abs = p_t #llamar a p_t como p_abs, por notación

#Eq de fuerza de empuje en el cohete
Empuje = 2*(p_abs - p_atm)*A

#Graficar Empuje
fig = plt.figure()
plt.title('Gráfica con N veces bomba accionada, N=10')
plt.plot(t,Empuje, 'g')
plt.show()