import numpy as np

def coin_toss_entropy(prob):
    if prob < 1e-6 or prob> .999999:
        return 0
    else:
        return -prob*np.log(prob) -(1-prob)*np.log(1-prob)