# Importing necessary modules
import numpy as np#
import matplotlib.pyplot as plt
from astropy.time import Time
from astropy import units as u
from datetime import datetime, timedelta
from astropy.coordinates import solar_system_ephemeris, EarthLocation, get_sun, get_body

base = datetime(2025,3,20,12,0,0,0)
times = [base - timedelta(days=x) for x in range(365)]
ts = Time(times,format='datetime',scale='utc') #Convering the MJDs to a Time format which Astropy can read.
with solar_system_ephemeris.set('builtin'):
    sun = get_sun(ts) # Get the location of the Sun
EoT = (sun.ra-ts.sidereal_time("mean","greenwich"))
EoT[EoT<-300*u.deg]=EoT[EoT<-300*u.deg]+360*u.deg

plt.figure(figsize=(8,4.2))
plt.subplot(111)
plt.grid(True)
plt.plot(times,EoT.hour*60)
plt.xlabel("Calendar Date")
plt.ylabel("Time Delay (mins)")
plt.savefig("../Figures/EoT.png")
plt.show()
