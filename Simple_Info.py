import numpy as np
class Simple_Info:
    """

    Attributes
    ----------
    prob_y_if_x: np.array
    px: list[float]
    py: list[float]


    """

    def __init__(self, prob_y_if_x, px):
        """

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

        Returns
        -------
        [py0, py1]: list[float]


        """
        py0 =0
        py1 = 0
        for x in [0, 1]:
            py0 += self.prob_y_if_x[0, x]*self.px[x]
            py1 += self.prob_y_if_x[1, x]*self.px[x]
        return [py0, py1]

    def mutual_info(self):
        """

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