def iter_z(c, max_iter=100):
    """
    Determines the number of iterations for a complex number `c` to diverge 
    under the Mandelbrot iteration z = z**2 + c.

    Parameters
    ----------
    c : complex
        The complex number to test for divergence.
    max_iter : int, optional
        The maximum number of iterations to check for divergence (default is 100).

    Returns
    -------
    int
        The number of iterations it took for |z| to exceed 2. If it never exceeds
        2 within `max_iter` iterations, returns `max_iter`.
    """
    z = 0
    for i in range(max_iter):
        z = z**2 + c
        if abs(z) > 2:
            return i
    return max_iter
