import numpy as np
import matplotlib.cm as cm
import matplotlib.colors as mcolors

def coin_toss_entropy(prob):
    """

    Parameters
    ----------
    prob

    Returns
    -------

    """
    if prob < 1e-10 or prob> 1-1e-10:
        return 0
    else:
        return -prob*np.log(prob) -(1-prob)*np.log(1-prob)

