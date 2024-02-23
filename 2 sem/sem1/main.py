import numpy as np


class SumTree:

    def __init__(self, data: list):
        ln = len(data)
        lb = np.log2(ln)
        if lb == int(lb):
            self.data = data
        else:
            self.data = data
            lb = int(lb) + 1
            for i in range(ln, 2 ** lb):
                self.data.append(0)

        self.tree = [0 for i in range(len(self.data))] + self.data
        self.calc_tree(1)

    def calc_tree(self, v: int) -> int:
        if v >= (len(self.data)):
            return self.tree[v]

        ls = self.calc_tree(v * 2)
        rs = self.calc_tree(v * 2 + 1)
        self.tree[v] = ls + rs

        return ls + rs


def Sum(tree, v: int, l: int, r: int):
    def tree_sum(v: int, l: int, r: int, tl=0, tr=len(tree.data) - 1):
        if l > r:
            return 0

        if l == tl and r == tr:
            return tree.tree[v]

        tm = (tr + tl) // 2
        print("v = ", v)
        return tree_sum(v * 2, l, min(r, tm), tl, tm) + tree_sum(v * 2 + 1, max(l, tm + 1), r, tm + 1, tr)

    return tree_sum(v, l, r)


def update(v: int, tl: int, tr: int, position: int, new_value: int):
    if tl == tr:
        tree.tree[v] = new_value
    else:
        tm = (tl + tr) // 2
        if position <= tm:
            update(v * 2, tl, tm, position, new_value)
        else:
            update(v*2+1, tm+1, tr, position, new_value)
        tree.tree[v] = tree.tree[2*v] + tree.tree[2*v+1]


tree = SumTree([1, 2, 3, 4, 5, 6, 7, 0, 1, 1, 1])
print(tree.tree)

print(Sum(tree, 1, 4, 7))
# запускать надо всегда при v=1(грубо говоря с 1 начинается нумерация, в нулевом элементе массива стоит 0, а само дерево идёт с 1 элемента)
