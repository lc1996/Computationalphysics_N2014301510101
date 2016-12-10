from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = [0.5*i-10 for i in range(41)]
Y = X
X, Y = np.meshgrid(X, Y)
Z=[[0 for i in X] for j in Y]
for j in [19,20,21]:
    for i in [19,20,21]:
        Z[i][j]=1
n=0
x1=[]
y1=[]
while n<1000:
    for i in range(1,40):
        for j in range(1,40):
            if (i-20)**2+(j-20)**2>2:
                Z[i][j]=(Z[i+1][j]+Z[i-1][j]+Z[i][j+1]+Z[i][j-1])*0.25
    n=n+1
plt.plot(x1,y1,'.')
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
