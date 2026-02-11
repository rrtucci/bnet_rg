import numpy as np


class Cond_Prob:
    def __init__(self, beta, jj, h, lam):
        self.beta = beta
        self.jj = jj
        self.h = h
        self.lam = lam

    def calc_cond_probs_y_if_abcd_x(self, abcd_states, x_state):
        assert set(abcd_states).issubset(set([-1, 1])), \
            str(abcd_states) + " is illegal"
        assert x_state in [-1, 1]
        abcd_sum = np.sum(abcd_states)
        energy_plus = -self.jj * abcd_sum - self.h - self.lam * (
                    +1 - x_state) ** 2
        energy_minus = self.jj * abcd_sum + self.h - self.lam * (
                    -1 - x_state) ** 2
        cond_prob_p = 1.0
        cond_prob_m = np.exp(-self.beta * (energy_minus - energy_plus))

        # print("cp", cond_prob_m, cond_prob_p)
        zz = cond_prob_m + cond_prob_p
        cond_prob_m /= zz
        cond_prob_p /= zz
        return [cond_prob_m, cond_prob_p, zz]


if __name__ == "__main__":
    def main():
        cpt = Cond_Prob(beta=1.0, jj=0, h=0)
        print(cpt.calc_cond_probs_y_if_abcd_x([1, -1, -1, -1], -1))


    main()
