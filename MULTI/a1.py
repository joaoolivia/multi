import numpy as np
import matplotlib.pyplot as plt 
import random

dw = 600

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
    heights = np.linspace(4444,10000,num=50)
    c = list()
    for h in heights:
        angles = np.linspace(0, np.arctan((dw/2)/h), num=50)
        t = list()
        r = list()
        for a in angles:
            delta_t = (h)/(3E8*np.cos(a))-(h)/(3E8)
            t.append(delta_t)
            r.append(h*np.tan(a))
        p2 = np.polyfit(r, t, 2)
        c.append(p2[0])
        
     
    return(c,heights,t,angles)

def hX(h):
    return(x0*np.exp(-(h)/(H)))
def Xh(x):
    return(H*np.log(x0/x))

c,heights,t,angles = model(dw)


X = list()
for h in heights:
    X.append(x0*np.exp(-(h)/(H)))

p1 = np.polyfit(X, c, 1)
fit = list()
for x in X:
    fit.append(p1[0]*x+p1[1])


#plt.plot(heights,c)
plt.plot(X,c)
plt.plot(X,fit)
plt.axis([230, 550, 0, 4e-13])
plt.show()


def dist(dw,h,nmax,x0,l):
    Xmax = hX(h)
    
    X = np.linspace(0,2*Xmax,50)
    particles = list()
    for x in X:
        a1 = (((x-x0)/(Xmax-x0))**((Xmax-x0)/(l)))
        a2 = np.exp((Xmax-x)/(l))
        n = nmax*a1*a2
        print(n,x)
        for i in range (round(n)):
            h = Xh(x)
            a = random.randint(0,1000)* np.arctan((dw/2)/h)/1000
            delta_t = (h)/(3E8*np.cos(a))-(h)/(3E8)
            r = h*np.tan(a)
            particles.append((x,r,delta_t))

    return(particles)

result = dist(dw,6500,100,x0,-100)
x = list()
r = list()
t = list()
for i in range (len(result)):
    x.append(result[i][0])
    r.append(result[i][1])
    t.append(result[i][2])

plt.scatter(r,t)
plt.show()


