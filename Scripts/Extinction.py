import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import astropy.constants as c
from dust_extinction.averages import GCC09_MWAvg


fig, ax = plt.subplots(figsize=[4,3],ncols=1, dpi=150)

# generate the curves and plot them
x = np.arange(0.3,10.0,0.1)/u.micron
ext_model = GCC09_MWAvg()

ax.plot(1./x,ext_model(x))

ax.set_title('Normalized Extinction, with enhancement at 217.5 nm.',fontsize=11)
ax.set_xlabel('$\lambda$ [$\mu m$]')
ax.set_ylabel('$A(\lambda)/A(V)$')
ax.set_xscale('log')
ax.set_xlim(0.09,4.0)
ax.axvline(0.2175,linestyle='--',color='k')

plt.tight_layout()
plt.savefig("../Figures/Extinction_Curve.png")
plt.show()

print("Ratio of extinction in K band to V band is:",ext_model(2*u.micron))
