# Importing necessary modules
import numpy as np#
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy import units as u
from datetime import datetime, timedelta
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_sun, get_body

times = np.arange(57192,57192+370,1) #This is just arbitrary MJDs I've chosen, sampled at 5 day intervals.
ts = Time(times,format='mjd',scale='utc') #Convering the MJDs to a Time format which Astropy can read.
with solar_system_ephemeris.set('builtin'):
    sun = get_sun(ts) # Get the location of the Sun
    
ra_order = np.argsort(sun.ra)

ra_rad = sun.ra.wrap_at(180 * u.deg).radian
dec_rad = sun.dec.radian

#Finally, just sorting the RA and Dec so that the plot looks nice.
ra_rad_order = np.argsort(ra_rad)
ra_rad = ra_rad[ra_rad_order]
dec_rad = dec_rad[ra_rad_order]

plt.figure(figsize=(8,3.3),dpi=150)
plt.subplot(121)
plt.grid(True)
plt.title("Location of Sun across the\n celestial sphere over one year.",fontsize=8)
plt.plot(sun.ra[ra_order],sun.dec[ra_order],'-', label="Sun (Ecliptic)") 
plt.axhline(0,color='k',ls='--', label="Celestial equator")
plt.ylabel("Dec (deg)")
plt.xlabel("RA (deg)")
plt.xlim(360,0) # Inverting the x-axis
plt.text(82,-3,r"Spring Equinox ($\gamma$)",fontsize=5)
plt.text(90,24.0,"Summer Solstice",fontsize=5)
plt.text(255,2,"Autumn Equinox",fontsize=5)
plt.text(270,-25.5,"Winter Solstice",fontsize=5)
plt.legend(fontsize=8)

ax = plt.subplot(122, projection="aitoff")
ax.grid(True)
ax.set_title("Location of Sun (Ecliptic) using a different projection\n",fontsize=8)
ax.plot(ra_rad*-1, dec_rad, '-') # Mollweide projection doesn't support axes which increase right to left, so we need to invert everything
ax.axhline(0,color='k',ls='--')
ax.text(0,-0.2,"Spring Equinox($\gamma$)",fontsize=5)
ax.text(-np.pi/2,0.5,"Summer Solstice",fontsize=5)
ax.text(np.pi/2,-0.5,"Winter Solstice",fontsize=5)
ax.text(np.pi,0.2,"Autumn Equinox",fontsize=5)
tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210]) # Defining custom labels, as mollweide works in -180 degrees to 180 degrees (and we want 0 to 
ax.set_xticklabels(tick_labels, zorder = 15,fontsize=8)
plt.tight_layout()
plt.savefig("../Figures/Sun_Track.png")
plt.show()
