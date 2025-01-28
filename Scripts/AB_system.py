import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as c
from astropy.modeling.models import BlackBody
from astropy.visualization import quantity_support

def integrate_bb(F_l,filt):
    wav = filt[:,0]*u.AA #Wavelength stored inverted in the file I just loaded in
    zeta_wav = filt[:,1] #Wavelength stored inverted in the file I just loaded in
    
    top = np.trapz(F_l*zeta_wav*wav,wav)
    bottom = np.trapz(zeta_wav*wav,wav)
    F_l_filter = top/bottom
    return(F_l_filter.to(u.erg/u.s/u.AA/u.cm**2))

u_filter = np.genfromtxt("../resources/u_filter_response.txt")
g_filter = np.genfromtxt("../resources/g_filter_response.txt")
r_filter = np.genfromtxt("../resources/r_filter_response.txt")
i_filter = np.genfromtxt("../resources/i_filter_response.txt")
z_filter = np.genfromtxt("../resources/z_filter_response.txt")

nu = c.c/(u_filter[:,0]*u.AA) #Inverting order for frequency
zeta_nu_u = u_filter[:,1] #Inverting order for frequency
zeta_nu_g = g_filter[:,1] #Inverting order for frequency
zeta_nu_r = r_filter[:,1] #Inverting order for frequency
zeta_nu_i = i_filter[:,1] #Inverting order for frequency
zeta_nu_z = z_filter[:,1] #Inverting order for frequency
F_nu = np.full_like(nu.value,fill_value=3631)*u.Jy

wav_pivot_u = 3526.90*u.AA
wav_pivot_g = 4729*u.AA
wav_pivot_r = 6210.34*u.AA
wav_pivot_i = 7730*u.AA
wav_pivot_z = 9662*u.AA

#F_nu = 3631*u.Jy # The flux density incident on the Earth
F_l = F_nu*c.c/(u_filter[:,0]*u.AA)**2
wav = u_filter[:,0]*u.AA

F_l_u = integrate_bb(F_l,u_filter)
F_l_g = integrate_bb(F_l,g_filter)
F_l_r = integrate_bb(F_l,r_filter)
F_l_i = integrate_bb(F_l,i_filter)
F_l_z = integrate_bb(F_l,z_filter)


fig,ax = plt.subplots(1,2,figsize=[8,3],dpi=150)
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy),'k')
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy)*zeta_nu_u,'C0')
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy)*zeta_nu_g,'C2')
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy)*zeta_nu_r,'C1')
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy)*zeta_nu_i,'C3')
ax[0].plot(nu.to(u.Hz),F_nu.to(u.Jy)*zeta_nu_z,'darkred')
ax[0].set_ylabel(r"Flux density (Jy)")
ax[0].set_xlabel(r"Frequency ($\rm \nu$)")

ax[1].plot(wav,F_l.to(u.erg/u.s/u.AA/u.cm**2),'k')
ax[1].plot(u_filter[:,0],(F_l*u_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C0')
ax[1].plot(g_filter[:,0],(F_l*g_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C2')
ax[1].plot(r_filter[:,0],(F_l*r_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C1')
ax[1].plot(i_filter[:,0],(F_l*i_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C3')
ax[1].plot(z_filter[:,0],(F_l*z_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'darkred')
ax[1].plot(wav_pivot_u,F_l_u,'.',color='C0',markersize=20)
ax[1].plot(wav_pivot_g,F_l_g,'.',color='C2',markersize=20)
ax[1].plot(wav_pivot_r,F_l_r,'.',color='C1',markersize=20)
ax[1].plot(wav_pivot_i,F_l_i,'.',color='C3',markersize=20)
ax[1].plot(wav_pivot_z,F_l_z,'.',color='darkred',markersize=20)

ax[1].set_ylabel(r"Flux density (erg/cm$^2$/s/${\rm \AA}$)")
ax[1].set_xlabel(r"Wavelength ($\rm \AA$)")
plt.tight_layout()
plt.savefig("../Figures/AB_Spectrum.png")
plt.show()

print(F_l_u.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_g.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_r.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_i.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_z.to(u.erg/u.s/u.AA/u.cm**2))
