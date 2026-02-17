import numpy as np


class Simple_Info:
    """
    This is a stand alone class for calculating various information theory 
    metrics for the trivial case of a distribution P(x, y) where x and y \in 
    {0, 1}
    
    P(x, y) = P(y|x) P(x)
    
    Attributes
    ----------
    prob_y_if_x: np.array
        P(y|x) specified as an array with column label y and row label x
    px: list[float]
        P(x) specified as a list [P(x=0), P(x=1)]
    py: list[float]
        P(y) specified as a list [P(y=0), P(y=1)]
        


    """

    def __init__(self, prob_y_if_x, px):
        """
        constructor

        Parameters
        ----------
        prob_y_if_x: np.array
        px: list[float]
        """
        self.prob_y_if_x = prob_y_if_x
        self.px = px
        self.py = self.get_py()


    def get_py(self):
        """
        This method returns P(y) specified as a list [P(y=0), P(y=1)]

        Returns
        -------
        list[float]

        """
        py0 =0
        py1 = 0
        for x in [0, 1]:
            py0 += self.prob_y_if_x[0, x]*self.px[x]
            py1 += self.prob_y_if_x[1, x]*self.px[x]
        return [py0, py1]

    def mutual_info(self):
        """
        This method returns the mutual information H(y:x)

        Returns
        -------
        mi: float

        """
        mi=0
        for y in [0, 1]:
            for x in [0,1]:
                mi += self.prob_y_if_x[y, x]*self.px[x]*\
                    np.log(self.prob_y_if_x[y, x]/self.py[y])
        return mi

    @staticmethod
    def entropy_coin_toss(probs):
        """
        This static method returns the entropy for probs = [P(a=0), P(a=1)]

        Parameters
        ----------
        probs: list[float]

        Returns
        -------
        ent: float

        """
        ent = 0
        for y in [0,1]:
            ent += probs[y]*np.log(1/probs[y])
        return ent

    def cond_info_y_if_x(self):
        """
        This method returns the conditional information H(y|x)

        Returns
        -------
        ci: float

        """
        ci=0
        for y in [0, 1]:
            for x in [0,1]:
                ci -= self.prob_y_if_x[y, x]*self.px[x]*\
                      np.log(self.prob_y_if_x[y, x])
        return ci


    def report(self):
        """
        This method prints a report with the values it is given and the
        values it calculates.

        Returns
        -------
        None

        """
        mi = self.mutual_info()
        ent_y = Simple_Info.entropy_coin_toss(self.py)
        ent_x = Simple_Info.entropy_coin_toss(self.px)
        cond_info = self.cond_info_y_if_x()
        print("px=",f"[{self.px[0]:.3f}", f"{self.px[1]:.3f}]")
        print(f"mi={mi:.4f}, ent_y={ent_y:.4f}, ent_x={ent_x:.4f}"
              f", eff={mi/ent_y:.4f}")
        print(f"ent_y={ent_y:.4f}, cond_info={cond_info:.4f}")

if __name__ == "__main__":
    zeroish = 1e-9
    oneish = 1 - zeroish
    def main(px):
        print("---------------------------------")
        prob_y_if_x = np.array([[oneish, zeroish], [zeroish, oneish]])
        simp = Simple_Info(prob_y_if_x, px)
        np.set_printoptions(precision=3)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()

        print()
        prob_y_if_x = np.array([[zeroish, oneish], [oneish, zeroish]])
        simp = Simple_Info(prob_y_if_x, px)
        np.set_printoptions(precision=3)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()

        print()
        prob_y_if_x = np.array([[oneish, oneish], [zeroish, zeroish]])
        simp = Simple_Info(prob_y_if_x, px)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()


        print()
        prob_y_if_x = np.array([[zeroish, zeroish], [oneish, oneish]])
        simp = Simple_Info(prob_y_if_x, px)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()

        print()
        prob_y_if_x = np.array([[.5, .5], [.5, .5]])
        simp = Simple_Info(prob_y_if_x, px)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()
        print(f"ln(2)={np.log(2):.4}")

        print()
        prob_y_if_x = np.array([[.3, .1], [.7, .9]])
        simp = Simple_Info(prob_y_if_x, px)
        print("prob_y_if_x=", prob_y_if_x)
        simp.report()
        print("---------------------------------")
    main([.3, .7])

    main([.5, .5])

    main([oneish, zeroish])

    main([zeroish, oneish])