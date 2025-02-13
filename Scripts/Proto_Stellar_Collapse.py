import astropy.units as u
import astropy.constants as c
import numpy as np
import matplotlib.pyplot as plt

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
