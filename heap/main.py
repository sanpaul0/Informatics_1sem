class Leaf:
    def __init__(self, value=None):
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.value = value


class Heap:

    def __init__(self):
        self.root = None
        self.tree = []

    def PrintHeap(self):
        for i in range(len(self.tree)):
            if self.tree[i] is None:
                print(None, end=' ')
            else:
                print(self.tree[i].value, end=' ')

    def add(self, val):
        newItem = Leaf(val)
        if len(self.tree) == 0:
            self.tree.append(newItem)
            """if len(self.tree)%2 == 0:
                self.tree[len(self.tree)//2].left_child = self.tree[len(self.tree)-1]"""
        else:
            parent = self.tree[(len(self.tree) - 1) // 2]
            if parent.value <= val:
                self.tree.append(newItem)
                if len(self.tree) % 2 == 0:
                    parent.left_child = newItem
                    self.tree[len(self.tree) - 1].parent = parent
                else:
                    parent.right_child = newItem
                    self.tree[len(self.tree) - 1].parent = parent
            else:
                for i in range(len(self.tree)):
                    if self.tree[i].value >= val:
                        point1 = (i - 1) * 2
                        point = i - 1
                        break
                newItem.left_child = self.tree[point].left_child
                self.tree[point].left_child = newItem
                newItem.parent = self.tree[point]
                self.tree.append(newItem)
                sorted_heap = [None for i in range(len(self.tree))]
                for i in range((len(self.tree) // 2) + 2):
                    if sorted_heap[i] is not None:
                        if (self.tree[i].left_child is None) or (self.tree[i].right_child is None):
                            if self.tree[i].left_child is not None:
                                sorted_heap[2 * i + 1] = self.tree[i].left_child
                            if self.tree[i].right_child is not None:
                                sorted_heap[2 * i + 2] = self.tree[i].right_child
                            continue
                        sorted_heap[2 * i + 2] = self.tree[i].right_child
                        sorted_heap[2 * i + 1] = self.tree[i].left_child
                    else:
                        sorted_heap[i] = self.tree[i]
                        sorted_heap[2 * i + 1] = self.tree[i].left_child
                        sorted_heap[2 * i + 2] = self.tree[i].right_child
                self.tree = sorted_heap

    def pop(self, index):
        ans = self.tree[index].value
        n = self.tree[index]
        self.tree.pop(index)
        if n.parent.left_child == n:
            while n is not None:
                if n.left_child.value <= n.right_child.value:
                    n.parent.left_child = n.left_child





a = Heap()
a.add(1)
a.add(2)
a.add(4)
a.add(5)
a.add(6)
a.add(7)
a.add(8)
a.add(9)
a.add(10)
a.add(12)
a.add(13)
a.add(3)
a.PrintHeap()
"""for i in range((len(self.tree) - index - 1) // 2):
            if n.left_child <= n.right_child:
                if self.tree[index // 2].left_child == n:
                    self.tree[index // 2].left_child = n.left_child
                    index = 2 * index + 1
                    n = self.tree[index]
                else:
                    self.tree[index // 2].right_child = n.left_child
                    index = 2 * index + 1
                    n = self.tree[index]"""
