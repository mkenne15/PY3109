# Errors and their meaning
When a report presents a result for a variable $x$ as $x\pm\sigma$, what does the $\sigma$ actually represent? This is an important question, especially since you are constantly being ask and reminded to present results with errors included.

Without explicitly defining $\sigma$, it is impossible to know how you should interpret the error - which is why you always need to say what it represents. Normally, an error bar is a convenient way of representing the probability distribution function $p(x)$. Commonly this probability distribution function is Gaussian, which has the form
$$
P(x) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\left[{-\frac{1}{2}\left( \frac{x-\mu}{\sigma} \right)^2}\right]
$$
where this distribution has a central value of $\mu$ and standard deviation of $\sigma$.

## Fitting data
Imagine now we have some data and we wish to fit a model to it. How do we judge whether the model is a good fit to the data?