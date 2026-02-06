from Cond_Prob import *
from Node import *
from globals import *


class Net:
    def __init__(self, beta, g, h):
        self.cpt = Cond_Prob(beta, g, h)
        self.nodes = []
        self.fill_nodes()

    def fill_nodes(self):
        nd_id = 1
        while nd_id <= NUM_TOP_ROOT_NODES:
            nd = Node(nd_id, "top_root")
            self.nodes.append(nd)
            nd_id += 1
        row = 2
        while row <= NUM_ROWS:
            while nd_id <= row*NUM_TOP_ROOT_NODES:
                if nd_id != row*NUM_TOP_ROOT_NODES:
                    nd = Node(nd_id, "nonroot")
                    pa1_nd = self.nodes[nd_id - NUM_TOP_ROOT_NODES +1]
                    pa2_nd = self.nodes[nd_id - NUM_TOP_ROOT_NODES + 2]
                    prob_pp = self.cpt.cond_prob_if_pp[0:2]*\
                        pa1_nd.prob_plus*pa2_nd.prob_plus
                    prob_pm = self.cpt.cond_prob_if_pm[0:2] * \
                              pa1_nd.prob_plus * pa2_nd.prob_minus
                    prob_mp = self.cpt.cond_prob_if_mp[0:2] * \
                              pa1_nd.prob_minus * pa2_nd.prob_plus
                    prob_mm = self.cpt.cond_prob_if_mm[0:2] * \
                              pa1_nd.prob_minus * pa2_nd.prob_minus
                    nd.prob_minus = \
                        prob_pp[0] +prob_pm[0] + prob_mp[0] + prob_mm[0]
                    nd.prob_plus = \
                        prob_pp[1] + prob_pm[1] + prob_mp[1] + prob_mm[1]
                    self.nodes.append(nd)
                else:
                    nd = Node(nd_id, "side_root")
                    self.nodes.append(nd)
                nd_id += 1
            row += 1
