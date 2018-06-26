import numpy as np 
from Utilities import laplace_section
from scipy.integrate import odeint

t = np.arange(0, 100, 0.1)

f = lambda i, t, l: t % 1.0 == 0

l = np.arange(0,1000)
 
r = laplace_section(f, t, l)

print(t[len(t)])