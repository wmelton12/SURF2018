import numpy as np
from scipy.integrate import odeint
from Utilities import laplace_section
import matplotlib.pyplot as plt 
def f(r, t, params):
	alpha, dalpha = r
	a, dphi, b, n = params

	dda = -a*np.sin(2*alpha-2*dphi*t)*(1 + b*np.cos(n*t))
	derivs = [dalpha, dda]
	return derivs

params = [1.0, 0.0,0.8,1.0]
r0 = [.1,4*np.pi/5.0]

tStop=1000
tInc=0.0005
t = np.arange(0., tStop, tInc)

ecc = []
n=15
for k in range(0,15):
	params = [1.0, 0.0, k/15.0, 1.0]
	sa = []
	sda = []
	psoln = []
	for i in range(-n,n):
		nsoln = odeint(f, [np.pi, 2.0*np.pi*(1*i)/5.0], t, args=(params,))
		psoln.append(nsoln)
		sa.append(laplace_section(lambda i, t, l: t % 1.0 == 0.0, t, nsoln[:,0], lambda i, t, l: l % (2*np.pi)))
		sda.append(laplace_section(lambda i, t, l: t % 1.0 == 0.0, t, nsoln[:,1]))

	totala = []
	totalda = []

	# Prune data
	sap = []
	sdap = []

	for i in range(-n,n):
		sat = []
		sdat = []
		for j in range(0, len(sa[i])):
			if (sa[i][j] < 0.05):
				ecc.append(k/15.0)
				sdat.append(sda[i][j])
		sap.append(sat)
		sdap.append(sdat)

for i in range(-n,n):
	totala = np.append(totala, sap[i])
	totalda = np.append(totalda, sdap[i])
fig = plt.figure(1,figsize=(10,10))

ax1 = fig.add_subplot(311)
ax1.plot(ecc, totalda, marker='.',linestyle='')

plt.show()