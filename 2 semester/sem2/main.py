import math as m


class Fenvik_tree:

    def __init__(self, data: list):
        self.data = data
        self.tree = [0 for i in range(len(self.data))]
        self.calc_tree()

    def calc_tree(self):
        for i in range(len(self.tree)):
            if (i // 2) * 2 == i:
                self.tree[i] = self.data[i]
            else:
                self.tree[i] = self.data[i]
                for j in range(0, int(m.log2(len(self.tree)))):
                    if (i - 2 ** j) & (i - 2 ** j + 1) == i & (i + 1):
                        self.tree[i] += self.tree[i - 2 ** j]
                        break
                    else:
                        self.tree[i] += self.tree[i - 2 ** j]


def update(tree, pos, new_val):
    val = new_val - tree.data[pos]
    while pos <= len(tree.tree):
        tree.tree[pos] += val
        pos = pos | (pos + 1)


def sum(tree, l: int, r: int) -> int:
    def Sum(pos: int) -> int:
        ans = 0
        if pos == 0:
            return tree.tree[0]
        elif pos < 0:
            return 0
        else:
            while pos > 0:
                ans += tree.tree[pos]
                pos = (pos & (pos + 1)) - 1
            return ans

    if l == r:
        return tree.data[l]
    else:
        return Sum(r) - Sum(l - 1)


tree = Fenvik_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# update(tree, 0, 9)
print(tree.tree)
print(sum(tree, 0, 9))
