import matplotlib.pyplot as plt
import numpy as np
import astropy.units as u
import astropy.constants as c

M = 300*u.solMass
m = 2*c.m_p
T = 20*u.K

rho = (3/(4*np.pi*M**2)) * ((3*c.k_B*T)/(2*c.G*m))**3
rho_n = rho/m

print("The Jeans density for a cloud of 300 solar masses, made entirely of molecular Hydrogen, and with a temperature of 20 Kelvin, is:")
print(rho.to(u.kg/u.m**3), " (mass density).")
print(rho_n.to(u.m**-3), "(particle density).")

M = 1*u.solMass
m = 2*c.m_p
T = 20*u.K

rho = (3/(4*np.pi*M**2)) * ((3*c.k_B*T)/(2*c.G*m))**3
rho_n = rho/m

print("The Jeans density for a cloud of 1 solar masses, made entirely of molecular Hydrogen, and with a temperature of 20 Kelvin, is:")
print(rho.to(u.kg/u.m**3), " (mass density).")
print(rho_n.to(u.m**-3), "(particle density).")

rho = np.logspace(-1,1,50)
T = rho**(1/3)
T_mona = rho**(5/3-1)
T_poly = 0.5*rho**(4/3-1)

fig,ax = plt.subplots(1,1,figsize=[4,3],dpi=150)
ax.set_ylim(0.4,1.6)
ax.axes.get_xaxis().set_ticks([])
ax.set_xlim(-1,1)
ax.axes.get_yaxis().set_ticks([])
ax.set_xlabel(r"$\rho$")
ax.set_ylabel("T")
    
ax.plot(np.log10(rho),1+np.log10(T),'k',label='Jeans Density')
ax.fill_between(np.log10(rho), 0, 1+np.log10(T), color='k', alpha=.2)
ax.plot(np.log10(rho),1+np.log10(T_mona),label='Monatomic gas')
ax.plot(np.log10(rho),1+np.log10(T_poly),label='Real gas')
ax.text(0.4,0.5,'Contraction')
ax.text(-0.9,1.3,'Expansion')
plt.legend(loc=1)
plt.savefig("../Figures/Temp_density.png")
plt.show()

M = 1*u.solMass
m = 2*c.m_p
T = 20*u.K
ed = 4.5*u.eV
ei = 13.6*u.eV

rho = (3/(4*np.pi*M**2)) * ((3*c.k_B*T)/(2*c.G*m))**3
r1 = (3*M/(4*np.pi*rho))**(1/3)
r2 = c.G*M**2/((M/(2*c.m_p)*ed+M/(c.m_p)*ei+c.G*M**2/r1))
teff = ((3*np.pi)/(32*c.G*rho))**(1/2)

E_gp = -c.G*M**2/r2
T = -E_gp/(3*M/c.m_p*c.k_B)

print("The critical density is {:e}".format(rho.to(u.kg/u.m**3)))
print("The initial radius is {:e}/{:e}".format(r1.to(u.solRad),r1.to(u.m)))
print("The final radius is {:f}/{:e}".format(r2.to(u.solRad),r2.to(u.m)))
print("The freefall time is {:e}".format(teff.to(u.year)))
print("The internal temperature assuming hydrostatic equilibrium at R2 is {:f}".format(T.to(u.K)))
