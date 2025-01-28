import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as c
from astropy.modeling.models import BlackBody
from astropy.visualization import quantity_support

def integrate_bb(bb,filt):
    wav = filt[::-1,0]*u.AA #Wavelength stored inverted in the file I just loaded in
    zeta_wav = filt[::-1,1] #Wavelength stored inverted in the file I just loaded in
    
    B_l = Bb_Vega(wav)
    F_l = np.pi*B_l*u.steradian
    L_l = 4*np.pi*(2.6*u.solRad)**2*F_l # Luminosity density of the Sun
    F_l = L_l/(4*np.pi*(7.68*u.pc)**2) # The flux density incident on the Earth
    
    F_filter = np.trapz(F_l*zeta_wav,wav) # Bolometric flux incident on the Earth
    
    top = np.trapz(F_l*zeta_wav*wav,wav)
    bottom = np.trapz(zeta_wav*wav,wav)
    F_l_filter = top/bottom
    return(F_filter.to(u.W/u.m**2),F_l_filter.to(u.erg/u.s/u.AA/u.cm**2))

u_filter = np.genfromtxt("../resources/u_filter_response.txt")
g_filter = np.genfromtxt("../resources/g_filter_response.txt")
r_filter = np.genfromtxt("../resources/r_filter_response.txt")
i_filter = np.genfromtxt("../resources/i_filter_response.txt")
z_filter = np.genfromtxt("../resources/z_filter_response.txt")

wav_pivot_u = 3526.90*u.AA
wav_pivot_g = 4729*u.AA
wav_pivot_r = 6210.34*u.AA
wav_pivot_i = 7730*u.AA
wav_pivot_z = 9662*u.AA

Bb_Vega = BlackBody(temperature=9450*u.K, scale=(1*u.erg/(u.s*u.cm**2*u.steradian*u.AA)))
wav = u_filter[:,0]*u.AA #Wavelength
B_l = Bb_Vega(wav)
F_l = np.pi*B_l*u.steradian
L_l = 4*np.pi*(2.6*u.solRad)**2*F_l # Luminosity density of the Sun
L = np.trapz(L_l,wav) # Total luminosity of the Sun
F_l = L_l/(4*np.pi*(7.68*u.pc)**2) # The flux density incident on the Earth

F_u, F_l_u = integrate_bb(Bb_Vega,u_filter)
F_g, F_l_g = integrate_bb(Bb_Vega,g_filter)
F_r, F_l_r = integrate_bb(Bb_Vega,r_filter)
F_i, F_l_i = integrate_bb(Bb_Vega,i_filter)
F_z, F_l_z = integrate_bb(Bb_Vega,z_filter)


plt.figure(figsize=[5,3],dpi=150)
plt.plot(wav,F_l.to(u.erg/u.s/u.AA/u.cm**2),'k')
plt.plot(u_filter[:,0],(F_l*u_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C0')
plt.plot(g_filter[:,0],(F_l*g_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C2')
plt.plot(r_filter[:,0],(F_l*r_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C1')
plt.plot(i_filter[:,0],(F_l*i_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'C3')
plt.plot(z_filter[:,0],(F_l*z_filter[:,1]).to(u.erg/u.s/u.AA/u.cm**2),'darkred')
plt.plot(wav_pivot_u,F_l_u,'.',color='C0',markersize=20)
plt.plot(wav_pivot_g,F_l_g,'.',color='C2',markersize=20)
plt.plot(wav_pivot_r,F_l_r,'.',color='C1',markersize=20)
plt.plot(wav_pivot_i,F_l_i,'.',color='C3',markersize=20)
plt.plot(wav_pivot_z,F_l_z,'.',color='darkred',markersize=20)

plt.ylabel(r"Flux density (erg/cm$^2$/s/${\rm \AA}$)")
plt.xlabel(r"Wavelength ($\rm \AA$)")
plt.tight_layout()
plt.savefig("../Figures/Vega_Spectrum.png")
plt.show()

print(F_u.to(u.W/u.m**2))
print(F_g.to(u.W/u.m**2))
print(F_r.to(u.W/u.m**2))
print(F_i.to(u.W/u.m**2))
print(F_z.to(u.W/u.m**2))

print(F_l_u.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_g.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_r.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_i.to(u.erg/u.s/u.AA/u.cm**2))
print(F_l_z.to(u.erg/u.s/u.AA/u.cm**2))
