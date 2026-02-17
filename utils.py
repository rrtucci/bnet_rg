import numpy as np


def coin_toss_entropy(prob):
    """
    This method calculates the entropy for a binary probability distribution
    [P(x=0), P(x=1)]

    Parameters
    ----------
    prob: float
        P(x=0) or P(x=1) (the same for both)

    Returns
    -------
    float

    """
    if prob < 1e-10 or prob> 1-1e-10:
        return 0
    else:
        return -prob*np.log(prob) -(1-prob)*np.log(1-prob)

