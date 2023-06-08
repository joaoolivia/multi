import numpy as np
import matplotlib.pyplot as plt 

dw = 100

x0 = 1030
H = 6500


#def t(dw,h,a,x0):
#    return((h)/(3E8*np.cos(a))-(h)/(3E8))
#    
#    
#
#angles = np.linspace(0.0001, np.arctan((dw/2)/h), num=50)
#y = list()
#for n in angles:
#    y.append(t(100,10000,n,50))
#
#p2 = np.poly1d(np.polyfit(angles, y, 2))
#
#def p(x):
#    return(p2[0]+ p2[1]*x+p2[2]*x**2)
#
#y2 = list()
#
#for n in angles:
#    y2.append(p(n))
#
#
def model(dw):
    heights = np.linspace(2000,12000,num=50)
    c = list()
    for h in heights:
        angles = np.linspace(0.0001, np.arctan((dw/2)/h), num=50)
        t = list()
        for a in angles:
            delta_t = (h)/(3E8*np.cos(a))-(h)/(3E8)
            t.append(delta_t)
        p2 = np.poly1d(np.polyfit(angles, t, 2))
        c.append(p2[2])
    return(c,heights)


c,heights = model(dw)
X = list()
for h in heights:
    X.append(x0*np.exp(-(h)/(H)))

plt.plot(X,c)
plt.show()