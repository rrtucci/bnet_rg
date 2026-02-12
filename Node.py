from random import choices
from globals import *


class Node:
    def __init__(self, id_num, type):
        self.id_num = id_num
        self.type = type
        assert type in ["X", "Y"]
        self.nearest_nei = self.get_nearest_nei()
        self.probs = [.4, .6]
        self.mutual_info = 0
        self.entropy = 1
        self.efficiency = 0

    def describe_self(self):
        print("id_num=", self.id_num)
        print("type=", self.type)
        print("nearest neighbors=", self.nearest_nei)
        print("probs=", [f"{num:.3f}" for num in self.probs])
        print("mutual info=", f"{self.mutual_info:.3f}")
        print("entropy=", f"{self.entropy:.3f}")
        print("efficiency=", f"{self.efficiency:.3f}")

    def get_nearest_nei(self):
        nearest_nei = [self.id_num + 1, self.id_num - 1,
                       self.id_num + DGRAPH_NUM_COLS,
                       self.id_num - DGRAPH_NUM_COLS]
        row = (self.id_num - 1) // DGRAPH_NUM_COLS + 1
        col = self.id_num - (row - 1) * DGRAPH_NUM_ROWS
        if row == 1:
            nearest_nei.remove(self.id_num - DGRAPH_NUM_COLS)
        if row == DGRAPH_NUM_ROWS:
            nearest_nei.remove(self.id_num + DGRAPH_NUM_COLS)
        if col == 1:
            nearest_nei.remove(self.id_num - 1)
        if col == DGRAPH_NUM_COLS:
            nearest_nei.remove(self.id_num + 1)
        return nearest_nei

    def set_efficiency(self):
        if self.entropy <1e-9:
            self.efficiency = 0.0
        else:
            self.efficiency = round(self.mutual_info / self.entropy, 4)

    def sample(self):
        return choices([-1, 1], self.probs)[0]


if __name__ == "__main__":
    def main():
        print('sample=', Node(1, "Y").sample())
        for i in range(1, NUM_DNODES + 1):
            nd = Node(i, "Y")
            print("_____________________")
            nd.describe_self()


    main()
