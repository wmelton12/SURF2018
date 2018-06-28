import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from Utilities import laplace_section

def f(r, t, params):
	alpha, dalpha = r
	a, dphi = params

	dda = -a*np.sin(2*alpha-2*dphi*t)  - a*np.sin(2*alpha + 2*dphi*t)
	derivs = [dalpha, dda]
	return derivs

params = [1.0, 0]
r0 = [.1,4*np.pi/5.0]


tStop=10000
tInc=0.0005
t = np.arange(0., tStop, tInc)
psoln = odeint(f, r0, t, args=(params,))

alpha = psoln[:,0]
dalpha = psoln[:,1]
sa = []
sda = []
psoln = []
n=15
for i in range(-n,n):
	nsoln = odeint(f, [np.pi, 2.0*np.pi*(1*i)/5.0], t, args=(params,))
	psoln.append(nsoln)
	sa.append(laplace_section(lambda i, t, l: t % 1.0 == 0.0, t, nsoln[:,0], lambda i, t, l: l % (2*np.pi)))
	sda.append(laplace_section(lambda i, t, l: t % 1.0 == 0.0, t, nsoln[:,1]))

totala = []
totalda = []

for i in range(-n,n):
	totala = np.append(totala, sa[i])
	totalda = np.append(totalda, sda[i])
fig = plt.figure(1,figsize=(39,40))

ax1 = fig.add_subplot(311)
ax1.plot(totala, totalda, marker='.',linestyle='')

plt.show()

