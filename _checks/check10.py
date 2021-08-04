import numpy as np

def fx(x):
    return np.exp(-x**2)

#list for integral values
gvals=[]

#constant offset (would need to obtain for particular problem).
g=0
dx=0.1

xvals=np.arange(-3,3,dx)
for x in xvals:
    g=g+fx(x)*dx
    gvals=gvals+[g]