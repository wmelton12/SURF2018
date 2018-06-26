import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(r, t, params):
	x,y,dx,dy = r # unpack current positions and velocides
	a = params
	derivs = [dx, dy, -a*x/((x*x+y*y)**(3/2)), -a*y/((x*x+y*y)**(3/2))]
	return derivs

params = 1
r0 = [2,0,0,1]

tStop=90000
tInc=0.005
t = np.arange(0., tStop, tInc)
psoln = odeint(f, r0, t, args=(params,))

fig = plt.figure(1,figsize=(8,8))

ax1 = fig.add_subplot(311)
ax1.plot(psoln[:,0], psoln[:,1])
plt.tight_layout()
plt.show()

