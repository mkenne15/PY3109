import numpy as np
import matplotlib.pyplot as plt
from astropy.modeling.functional_models import AiryDisk2D

x = np.arange(-5,10,0.05)
y = np.arange(-5,5,0.05)
X, Y = np.meshgrid(x, y)
disc_func = AiryDisk2D()
z1 = disc_func.evaluate(X,Y,amplitude=1,x_0=0,y_0=0,radius=1.22)
z2 = disc_func.evaluate(X,Y,amplitude=1,x_0=5,y_0=0,radius=1.22)
z3 = disc_func.evaluate(X,Y,amplitude=1,x_0=1,y_0=0,radius=1.22)

fig,ax = plt.subplots(nrows=1,ncols=3,figsize=[10,2.5],dpi=150)
ax[0].pcolormesh(x,y,z1**0.4,cmap='magma') 
ax[1].pcolormesh(x,y,(z1+z2)**0.4,cmap='magma') 
ax[2].pcolormesh(x,y,(z1+z3)**0.4,cmap='magma')

for axs in ax:
    axs.set_xticks([])
    axs.set_yticks([])
ax[0].set_title("Single Airy Disc")
ax[1].set_title("Resolved Airy discs")
ax[2].set_title("Unresovled Airy discs")
plt.subplots_adjust(left=0,wspace=0,right=1)
plt.savefig("../Figures/Airy_discs.png")
plt.show()
