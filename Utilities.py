import numpy as np




def laplace_section(f, t, l, g = lambda x,y,z: z):
	'''
	Does the laplace section.  f is a function that returns True if the data should be included.  f should accept three arguments, i, t[i], and l[i] in that order.
	g transforms the data as it is entered.  If no parameter is specified, it appends l[i] simply to the list. 
	'''
	rl = []
	for i in range(0, len(t)):
		if f(i, t[i], l[i]):
			rl = np.append(rl, g(i,t[i],l[i]))
	return rl


