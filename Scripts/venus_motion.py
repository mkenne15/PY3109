import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, EarthLocation
from astropy.coordinates import get_body_barycentric, get_body, get_moon

times = np.arange(57192,57322,2) #This is just arbitrary MJDs I've chosen, sampled at 2 day intervals.
ts = Time(times,format='mjd',scale='utc') #Convering the MJDs to a Time format which Astropy can read.
loc = EarthLocation.of_site('greenwich') #Our observations have to be taken somwhere, let's use Greenwich for ease of use.
with solar_system_ephemeris.set('builtin'):
    venus = get_body('venus', ts, loc) # Get the location of venus
plt.figure(figsize=[4,3],dpi=200)
plt.plot(venus.ra,venus.dec,'-') #Plotting the RA and Dec of venus
plt.arrow(venus.ra.value[4],venus.dec.value[4],3,-1.5,width=0.3)
plt.arrow(venus.ra.value[29],venus.dec.value[29],-2.5,0.7,width=0.3)
plt.arrow(venus.ra.value[-4],venus.dec.value[-4],3,-0.9,width=0.3)
plt.title(f"Location of Venus from \n {ts[0].isot[:10]} to {ts[-1].isot[:10]}")
plt.ylabel("Dec (deg)")
plt.xlabel("RA (deg)")
plt.gca().invert_xaxis() #RA normally increases from right to left - we'll explain why this is later on
plt.tight_layout()
plt.savefig("../Figures/Planet_motion.png")
plt.show()
