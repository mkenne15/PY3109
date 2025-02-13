## Interferometry
We finished our discussion last week by looking at how interferometry works. With this method, the condition required for two sources to be resolved is that the difference in the additional path length photons must travel to reach the second telescope is $c \Delta t \sim \lambda$, such that the photons from the source which is $\Delta \theta$ away from source which is on axis are still arriving in phase and may be combined coherently. We also expressed this condition as $\Delta \theta = \frac{\lambda}{L}$, where L is the separation of the telescopes (also known as the baseline).

We only considered two dishes, but radio interferometers are typically composed of multiple dishes so that the image can be properly sampled, and this phase difference must be measured for every pair of telescopes, which is why the computational cost of this technique quickly increases as you add more baselines to the array.

As examples, consider the Very Large Array - this is an array of 27 dishes, each 25 m in diameter, in New Mexico. The dishes can be re positioned to change the baselines, with the largest baseline being 37 km.

Finally, let's ask the question: if this technique can achieve fantastic spatial resolutions, why don't we do it at other wavelengths?

For radio wavelengths (say 10cm), this can be done by accurately time tagging data as it arrives. After all, for $\lambda =$ 10 cm, $\Delta t=$ 0.3 nanoseconds. Such a high accuracy in timing is achievable using GPS, meaning the data can be recorded, digitised, and combined in a correlator.

However, if we wanted to carry out interferometry at optical wavelengths, things becomes trickier. Assume a wavelength of $\lambda=500$ nm. Then $\Delta t=$ 1.6 femtoseconds. As such, time tagging data becomes much more difficult. Instead, the handful of optical interferometers which exist (Very Large Telescope Interferometer or the Large Binocular Telescope interferometer) employ mirrors to redirect light from each mirror into a chamber where the photons can be interfered directly.

# X-ray Astronomy
Now that we've looked at how we account for the Rayleigh criteria at radio wavelengths, let's move to the other side of the spectrum, and discuss X-rays. X-ray astronomers typically work in energy rather than wavelength or frequency. The X-ray regime is considered to be 0.3-70 keV. So what temperature objects are X-rays focused? Let's assume black body radiation, and a peak in the spectrum at an energy of 3 keV (corresponding to a wavelength of 0.41 nm). Using Wien's law, we find that T would be ~ $7\times10^6$ Kelvin. These types of temperatures are typically found in very, very hot plasmas (or the surface of a neutron star), making this an ideal window for studying energetic phenomena.  It is also the perfect window for observing emission from highly ionized isotopes (such as Fe XXIV, XXV,  - that is, Fe with only 2 or 1 electrons left).

So we want to study this wavelength regime as it covers hot, relativistic plasmas. How do we do it? First, the telescopes must be in space, as the Earth's atmosphere absorbs all incident X-rays. Infact, the 2002 Nobel Prize in physics was half-awarded to Riccardo Giacconi for pioneering X-ray detectors onboard first rockets, followed by orbiting satellites.

Second, recall the Rayleigh criteria for X-rays:
- X-ray (0.12 nm - 4.1 nm). Take a 1 m telescope and lambda=1 nm, then $\theta=0.0002^{\rm "}$.

This suggests that for a modest sized telescope, we should achieve outstanding resolution with X-ray telescopes. So why are X-ray images so blurry? The key here is to realise that creating an X-ray telescope which has the collecting area equivalent to a 1m diameter mirror is very difficult.
### Grazing Incidence Optics
X-ray's are absorbed by a lot of materials, and so focusing them using conventional setups doesn't work. Instead, we must rely on grazing incidence optics. In this setup, the angle between an incoming photon and the reflecting mirror, $\theta$, is very small (~ a few degrees). The photons are then focused to a point which is quite far away from the mirrors.

![SingleSlit](Figures/Xray_focus.svg)

Take the NuSTAR X-ray telescope for example. The aperture is roughly 1 m in diameter, and for $\theta=1^{\rm o}$, this means the focal point is 12.5 m away - so X-ray telescopes tend to be very long, making putting them in space complicated. Most modern X-ray telescopes tend to have 2 sets of mirrors, such that the focal point can be reduced further by reflecting the X-rays twice, while increasing the field over which sources are in focus.

![[Wolter-I.svg.png]]

Even worse - because we need $\theta$ to be small, only an annulus of the aperture can be filled - meaning the effective collecting area tends to be quite small. NuSTAR, for example, only has an effective area of 847 cm$^2$ - a lot smaller than if the aperture were filled. This also affects the resolution, which is only about 1" for these types of telescopes.

Another unique aspect of X-ray astronomy (and $\gamma$-ray astronomy) is that the observations are usually photon starved - that is, it is very rare that you would expect more than 1 photon to strike your detector in between read outs. This is very useful because, a well characterised CCD has a known relationship between the amount of charge liberated in a pixel versus incoming photon-energy - and so measuring the charge in a pixel directly gives you the energy of the photon which created the charge.

So for X-ray astronomy not only do we get images, we also get spectra at the same time (as opposed to optical astronomy where these must be two different observations).

Since we are dealing with low-number statistics, the probability distribution fro X-ray astronomy is the poisson distribution encountered earlier. That is
$$
    P(N)=\frac{\mu^N e^{-\mu}}{N!}
$$
where $N$ is the number of detected photons and $\mu$ is the expected number.

# Stellar Formation
A few lectures ago, we generated the H-R diagram. At the time, we simply said that normal stars fall on a diagonal line between the top left and bottom right corners. Now we're going to ask ourselves the question "How do stars form and evolve across that diagram?".

First, we need to create our star. Consider a spherical cloud of dust of radius $R$ and total mass $M$, as shown below. 

![DustCloud](Figures/Spherical_Dust_Cloud.svg)

The mass, $m$, contained within a spherical shell of radius of $r$, is given by
$$
    m(r) = \int^{r}_{0} \rho(r')4\pi r'^2 dr'
$$
where $\rho(r)$ is the density of the cloud, and is a function of the radius. This mass acts as a gravitational point mass giving rise to an inward acceleration of
$$
    g(r)=\frac{Gm(r)}{r^2}.
$$
So we have a expression for the gravitational acceleration that a mass element within the sphere will experience. However, that is not the only force at play here. There is likely to be a pressure gradient across the cloud. To find an expression for this, consider the volume element, $\Delta A \Delta r$, enclosed in the grey area in the above diagram (the $\Delta A$ part is difficult to image due to the 2-d representation of this figure). At the inner face of the volume element (radius=$r$), the force is $P(r)\Delta A$. The force on the outer face (radius=$r+\delta r$) is $(P(r)+\frac{dP}{dr}\Delta r)\Delta A$. The resultant force experienced by the volume element is thus
$$
    \Delta F_{P} = (P(r)+\frac{dP}{dr}\Delta r - P(r))\Delta A = \frac{dP}{dr}\Delta r \Delta A
$$
Now, the mass volume of this element, $\Delta M= \rho(r)\Delta r \Delta A$. By using $F = \Delta M \; g(r) + \Delta F_{P}$, we arrive at
$$
    -\frac{d^2r}{dt^2}=g(r)+\frac{1}{\rho (r)}\frac{dP}{dr}
$$
Now we have an expression which gives us the acceleration, taking into account both gravity and pressure.