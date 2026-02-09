from random import choices


class Node:
    def __init__(self, id_num, type, nearest_nei_id_nums):
        self.id_num = id_num
        self.type = type
        assert type in ["X", "Y"]
        self.nearest_nei_id_nums = nearest_nei_id_nums
        self.probs = [.5, .5]
        self.mutual_info = 0
        self.entropy = 0

    def describe_self(self):
        print("id_num=", self.id_num)
        print("type=", self.type)
        print("nearest neighbors=", self.nearest_nei_id_nums)
        print("probs=", [f"{num:.{3}f}" for num in self.probs])
        print("mutual info=", f"{self.mutual_info:.{3}f}")
        print("entropy=", f"{self.entropy:.{3}f}")


    def sample(self):
        return choices([-1, 1], self.probs)[0]


if __name__ == "__main__":
    def main():
        nd = Node(1, "Y", [2, 6])
        print('sample=', nd.sample())
        nd.describe_self()
    main()
