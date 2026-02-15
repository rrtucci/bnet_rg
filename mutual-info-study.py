import numpy as np
class SIMPLE_INFO:

    def __init__(self, prob_a_if_b, pb):
        self.prob_a_if_b = prob_a_if_b
        self.pb = pb
        self.pa = self.get_pa()


    def get_pa(self):
        pa0 =0
        pa1 = 0
        for b in [0, 1]:
            pa0 += self.prob_a_if_b[0, b]*self.pb[b]
            pa1 += self.prob_a_if_b[1, b]*self.pb[b]
        return [pa0, pa1]

    def mutual_info(self):
        mi=0
        for a in [0, 1]:
            for b in [0,1]:
                mi += self.prob_a_if_b[a, b]*self.pb[b]*\
                    np.log(self.prob_a_if_b[a, b]/self.pa[a])
        return mi

    @staticmethod
    def entropy_coin_toss(probs):
        ent = 0
        for a in [0,1]:
            ent += probs[a]*np.log(1/probs[a])
        return ent

    def cond_info_a_if_b(self):
        ci=0
        for a in [0, 1]:
            for b in [0,1]:
                ci -= self.prob_a_if_b[a, b]*self.pb[b]*\
                      np.log(self.prob_a_if_b[a, b])
        return ci


    def report(self):
        mi = self.mutual_info()
        ent_a = SIMPLE_INFO.entropy_coin_toss(self.pa)
        ent_b = SIMPLE_INFO.entropy_coin_toss(self.pb)
        print(f"mi={mi:.4f}, ent_a={ent_a:.4f}, ent_b={ent_b:.4f}"
              f", eff={mi/ent_a:.4f}")

if __name__ == "__main__":
    def main():
        zeroish = 1e-9
        oneish = 1 - zeroish
        pb = [.1, .9]

        prob_a_if_b = np.array([[oneish, zeroish], [zeroish, oneish]])
        simp = SIMPLE_INFO(prob_a_if_b, pb)
        np.set_printoptions(precision=3)
        print("prob_a_if_b=", prob_a_if_b)
        simp.report()

        print()
        prob_a_if_b = np.array([[oneish, oneish], [zeroish, zeroish]])
        simp = SIMPLE_INFO(prob_a_if_b, pb)
        print("prob_a_if_b=", prob_a_if_b)
        simp.report()

        print()
        prob_a_if_b = np.array([[zeroish, zeroish], [oneish, oneish]])
        simp = SIMPLE_INFO(prob_a_if_b, pb)
        print("prob_a_if_b=", prob_a_if_b)
        simp.report()

        print()
        prob_a_if_b = np.array([[.5, .5], [.5, .5]])
        simp = SIMPLE_INFO(prob_a_if_b, pb)
        print("prob_a_if_b=", prob_a_if_b)
        simp.report()
    main()