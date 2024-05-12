import matplotlib.pyplot as pl
import numpy as np

def F(n, signo):
    return signo*1/(n**2)

def E(n, signo):
    return signo*1/(n**2)


limInf = 0
limSup = 10

#Para fuerza
x1 = np.linspace(limInf, limSup, 50)
y1pos = F(x1, 1)
y1neg = F(x1, -1)

#Para campo electrico
x2 = np.linspace(limInf, limSup, 50)
y2pos = E(x2, 1)
y2neg = E(x2, -1)

pl.figure()
# r > 0
pl.subplot(221)
pl.plot(x1, y1pos)
pl.title("r > 0")
pl.grid(True)

# r < 0
pl.subplot(222)
pl.plot(x1, y1neg)
pl.title("r < 0")
pl.grid(True)

# r > 0
pl.subplot(223)
pl.plot(x2, y2pos)
pl.title("r > 0")
pl.grid(True)

# r < 0
pl.subplot(224)
pl.plot(x2, y2neg)
pl.title("r < 0")
pl.grid(True)

pl.show()





