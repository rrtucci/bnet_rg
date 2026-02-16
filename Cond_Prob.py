import numpy as np


class Cond_Prob:
    """
    This class provides a method that calculates the conditional
    probability

    P(S_i^Y | S_a^X, S_b^X, S_c^X, S_d^X)

    where the spins S are all either -1 or +1.

    Attributes
    ----------
    beta: float
        1/T, inverse temperature
    h: float
        magnetic field, coupling, energy contribution is $-h* S_i^Y$, h=0 in
        this study
    jj: float
        coupling constant, energy contribution is
        $-jj* S_i^Y(S_a^X + S_b^X + S_c^X + S_d^X)$
    lam: float
        coupling constant, energy contribution is $-lam* S_i^X S_i^Y$. lam=0
        in this study

    """

    def __init__(self, beta, jj, h, lam):
        """
        constructor

        Parameters
        ----------
        beta: float
        jj: float
        h: float
        lam: float
        """
        self.beta = beta
        self.jj = jj
        self.h = h
        self.lam = lam

    def calc_cond_probs_y_if_abcd_x(self, abcd_states, x_state):
        """
        This method which calculates the conditional probability

        P(S_i^Y | S_a^X, S_b^X, S_c^X, S_d^X)

        where the spins S are all either -1 or +1. This conditional prob is
        taken to be proportional to exp(-beta*Ising Energy). The
        normalization constant is denoted  by zz. The method returns

        [P(S_i^Y=-1 | S_a^X, S_b^X, S_c^X, S_d^X),

        P(S_i^Y=+1 | S_a^X, S_b^X, S_c^X, S_d^X),

        zz]

        Parameters
        ----------
        abcd_states: list[int]
            a list of ints (len =coord_num) which must be either -1
            or 1. The coordination number is the number of nearest neighbors,
            4 for internal points, 2 for corners, 3 for boundary points that
            are not corners
        x_state: int
            state of  S_i^X, either -1 or 1

        Returns
        -------
        [cond_prob_m, cond_prob_p, zz]: list[float]


        """
        assert set(abcd_states).issubset(set([-1, 1])), \
            str(abcd_states) + " is illegal"
        assert x_state in [-1, 1]
        abcd_sum = np.sum(abcd_states)
        energy_plus = -self.jj * abcd_sum - self.h - self.lam * x_state
        energy_minus = self.jj * abcd_sum + self.h + self.lam * x_state
        cond_prob_p = 1.0
        cond_prob_m = np.exp(-self.beta * (energy_minus - energy_plus))

        # print("cp", cond_prob_m, cond_prob_p)
        zz = cond_prob_m + cond_prob_p
        cond_prob_m /= zz
        cond_prob_p /= zz
        return [cond_prob_m, cond_prob_p, zz]


if __name__ == "__main__":
    def main():
        cpt = Cond_Prob(beta=1.0, jj=0, h=0, lam=1)
        print(cpt.calc_cond_probs_y_if_abcd_x([1, -1, -1, -1], -1))


    main()
