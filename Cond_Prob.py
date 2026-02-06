import numpy as np

class Cond_Prob:
    def _init_(self, beta, g, h):
        self.beta = beta
        self.g= g
        self.h = h
        self.cond_prob_if_mm = Cond_Prob.calc_cond_probs(-1, -1, beta, g, h)
        self.cond_prob_if_mp = Cond_Prob.calc_cond_probs(-1, +1, beta, g, h)
        self.cond_prob_if_pm = Cond_Prob.calc_cond_probs(+1, -1, beta, g, h)
        self.cond_prob_if_pp = Cond_Prob.calc_cond_probs(+1, +1, beta, g, h)

    @staticmethod
    def calc_cond_probs(pa_spin1, pa_spin2, beta, g, h):
        energy_plus = g*(pa_spin1 + pa_spin2)/2 + h
        energy_minus = -g*(pa_spin1 + pa_spin2)/2 - h
        zz = energy_plus + energy_minus
        prob_minus = np.exp(-beta* energy_minus)/zz
        prob_plus = np.exp(-beta* energy_plus)/zz
        return [prob_minus, prob_plus, zz]





