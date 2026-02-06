## Air mass & Extinction
The Earth's atmosphere absorbs light, and the amount of light absorbed depends on the angle of the star above the horizon. If we didn't correct this effect, observations of objects at different times of night would give different magnitudes! We'll see how to correct for extinction below, but first we need to work out how extinction depends on the angle of the star above the horizon.

We can derive a simple equation for the extinction correction by assuming the atmosphere is a series of thin plane-parallel layers. The figure below shows such a layer, of thickness dx at an altitude x. The path length through the layer for light from a star at a zenith distance $z$ is equal to $\frac{{\rm d}x}{\cos z}={\rm d}x \sec z$. The term $\sec z$ is known as the airmass, and is sometimes given the symbol $X$. 

At the zenith, $X=\sec z=1$, and this increases to a value of 2 at a zenith distance of 60$^{\rm o}$. Note that the approximation of the atmosphere as being plane-parallel breaks down at larger zenith distances. Due to the amount of extinction, it's a bad idea to observe astronomical objects this low, so we shall not worry about the curvature of the atmosphere here.

![Aberration_2](Figures/Airmass.svg)

If the monochromatic flux from an object incident on the layer is $F_{\lambda}$ then the flux absorbed by the layer $dF_{\lambda}$ will be proportional to both $F_{\lambda}$ and the path length through the layer. Therefore:
$$
dF_{\lambda}=−\alpha_\lambda F_{\lambda} \sec z dx,
$$

where the constant of proportionality, $\alpha_\lambda$ is known as the absorption coefficient, with units of m$^{-1}$. The absorption coefficient is a function of the composition and density of the atmosphere, and hence the altitude of the layer, x. We can re-arrange this equation (and drop the $\lambda$ subscripts for clarity) to give
$$
\frac{dF}{F}=−\sec z \: \alpha \: dx.
$$
Integrating the equation above for x values from the top of the atmosphere, t, to the bottom b, we obtain
$$
\int ^b _t \frac{dF}{F} =−\sec z \: \int ^b _t \alpha \: dx.
$$

Hence
$$
\frac{F_b}{F_t}=\frac{F}{F_0}=\exp\left(−\sec z \: \int ^b _t \alpha \: dx\right)
$$
If you recall the definition of magnitude (from last year, but don't worry, we'll be going over it in the next lecture anyway), then we can say
$$
    m - m_0 = -2.5\log_{10}\left( \frac{F}{F_0} \right) = 2.5 \sec z \log_{10} (e) \int^b_t \alpha {\rm d} x
$$
We will now define, which is some constant.
$$
    k = 2.5 \log_{10} (e) \int^b_t \alpha {\rm d} x
$$
> [!important] This gives us a simple expression to correct for the amount of extinction which our system has experienced
>$$
>   m = m_0 + k \sec (z) = m_0 + k X
>$$
>$k$ is a constant that can be measured experimentally, and for the common observing filters, has values as given below.
>
| Filter | $\lambda_{\rm eff}$ (nm) | k (mags/airmass) |
| ------ | ------------------------ | ---------------- |
| U      | 360                      | 0.55             |
| B      | 430                      | 0.25             |
| V      | 550                      | 0.15             |
| R      | 650                      | 0.09             |
| I      | 820                      | 0.06             |

# Proper Motion
Next, we consider the effects of a stars proper motion across the night sky. Consider an observer, and a star with velocity **v** as shown below. In spherical coordinates, this velocity has two components - a radial component, $v_{\rm r}$, and an angular component $v_{\rm \theta}$. If we're tracking a stars position across the celestial sphere, then we are only measuring $v_{\rm \theta}$, which is known as the **transverse velocity**. Now, consider a time interval $\Delta t$. Over this time, an object will have moved a distance $\Delta d$ relative to our line of sight
$$
 \Delta d = v_{\rm \theta} \Delta t.
$$
If the distance, r, to the object is known, then the angular change across the celestial sphere is given by
$$
 \Delta \theta = \frac{\Delta d}{r} = \frac{v_{\rm \theta} \Delta t}{r}.
$$
The **proper motion** of an object, that is the change of this angle with time, is then given by
$$
 \mu \equiv \frac{d \theta}{d t} = \frac{v_{\rm \theta}}{r}.
$$

So, in practice, what is the expression for $\theta$? Consider a star which moves between point A and B on the celestial sphere, as shown below.

![Celestial Sphere_RA_Dec|300](Figures/Proper_motion.svg)

First, we can write the expression:
$$
    \frac{\sin{\Delta\theta}}{\sin{\Delta\alpha}} = \frac{\sin(90^{\rm o}-(\delta+\Delta\delta))}{\sin{\phi}}
$$
This result relies on knowing what the law of sines is for arcs on a great circle, which I encourage you to look up in your own time.

This can  be rewritten as 
$$
    \sin\Delta\alpha \cos(\delta+\Delta\delta) = \sin\Delta\theta \sin\phi.
$$
Now using the small angle approximation for anything with $\Delta$ in it (which is likely true for objects moving across the night sky!), we get
$$
    \Delta\alpha \cos(\delta+\Delta\delta) = \Delta\theta \sin\phi.
$$
$\cos(\delta+\Delta\delta)$ can be Taylor expanded around $\Delta\delta\sim0$ to give
$$
    \cos(\delta+\Delta\delta) = \cos(\delta)-\Delta\delta\sin(\delta)+... \approx \cos(\delta)
$$
which then leaves us with 
$$
    \Delta\alpha = \Delta\theta \frac{\sin\phi}{\cos(\delta)}.
$$
Now, in order to solve for $\Delta\theta$ and remove $\phi$, we need to use the law of cosines:
$$
\cos[90^{\rm o}-(\delta+\Delta\delta)]=\cos(90^{\rm o}-\delta)\cos(\Delta\theta)+\sin(90^{\rm o}-\delta)\sin(\Delta\theta)\cos(\phi)
$$
Again, this is for arcs on a great circle, which you may need to look over.

By substituting $\cos[90^{\rm o}-(\delta+\Delta\delta)]=\sin(\delta+\Delta\delta)=\sin(\delta)\cos(\Delta\delta)+\cos(\delta)\sin(\Delta\delta)$ and using the small angle approximation becomes
$$
    \Delta\delta=\Delta\theta\cos\phi
$$
Combining this with the equation above gives
$$
    (\Delta\theta)^2=(\Delta\delta)^2+(\Delta\alpha\cos\delta)^2
$$
This gives a very handy expression for calculating the angular separation between two objects.

As an example of why measuring proper motion and velocities is important, see [this paper on the "cannonball" pulsar](https://iopscience.iop.org/article/10.3847/2041-8213/ab18f7)

# Distances, Magnitudes, and the Hertzsprung-Russell Diagram
>[!info] How do we measure the distances to stars, and define how bright stars are? Once we know these parameters, what can they tell us about the structure of our Galaxy, and the hierarchy of stars?

Note that this is nearly a perfect repeat of a lecture from PY2106, but the material is very relevant for what lies ahead, so it's worth tackling it again.

## The distance and brightness of stars
The most direct method of measuring the distance to a star is to measure its parallax. Consider a nearby star which is a distance D from the Sun. Over a half a year, it's position on the sky will vary relative to the background of stars which are far enough away that they don't show any motion.

![Parallax|600](Figures/Parallax.svg)

The Earth lies 1 astronomical unit (1 AU $=1.49\times10^{11}$ m) away from the Sun. As such, an object which exhibits a parallax of $\theta=1"$ has to be a distance
$$
    D = \frac{1.49\times10^{11} \: {\rm m}}{\tan(\theta)} \approx \frac{1.49\times10^{11} \: {\rm m}}{\theta} = 3.0856\times10^{16}{\rm m} \equiv 1 {\rm pc}
$$
Alternatively
$$
D = \frac{1}{\theta}
$$
when $\theta$ is given in arc-seconds. Note that D will be given in parsecs when using this form of the equation.
Note that the nearest star to Earth, Proxima Centauri, is 1.3 parsecs away. This means the observed parallax is less than 1". This is a very small angle, smaller than the average seeing from an observing site (where seeing is the dispersion of starlight by atmospheric turbulence.)

A parallax measurement of 0.1-0.01" can be done from the ground under exceptional observing conditions, but this only gets us out to a distance of 100 pc. Considering the Milky Way is 32kpc across, this is barely scratching the surface. As such, we need to get above the atmosphere to observe smaller parallaxes.

>[!example] Example: Stars on the far side of the Milky Way
>
>The furthest star from Earth in the Milk way is roughly 24kpc away. How sensitive would a telescope need to be to measure the parallax of this object?
>$$
>\theta=\frac{1}{24000}=4\times10^{-5}\: ^{"}
>$$
>For reference, GAIA is a space telescope which has achieved parallax measurements of $(1\times10^{-4})$". As such, it is capable of constraining the distances of objects which are up to 10 kpc away.

