import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(r, t, params):
	alpha, dalpha = r
	a, dphi = params
	dda = a*np.sin(2*alpha-2*dphi*t)
	derivs = [dalpha, dda]
	return derivs

params = [1.0, 0]
r0 = [.1,1.99999*np.pi/5.0]


tStop=1000
tInc=0.0005
t = np.arange(0., tStop, tInc)
psoln = odeint(f, r0, t, args=(params,))

totala = []
totalda = []

for n in range(-10,11):
	r0[1] = n*.0001
	psoln = odeint(f, r0, t, args=(params,))
	sal = []
	sdal = []
	alpha_list = psoln[:,0]
	dalpha_list = psoln[:,1]
	for i in range(0, len(t)/10000):
			sal.append(alpha_list[10000*i]%(2*np.pi))
			sdal.append(dalpha_list[10000*i])
	totala = np.append(totala, sal)
	totalda = np.append(totalda, sdal)

fig = plt.figure(1,figsize=(8,8))

ax1 = fig.add_subplot(311)
ax1.plot(totala, totalda, marker='.',linestyle='')
plt.tight_layout()
plt.show()

