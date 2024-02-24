class Heap:
    def __init__(self):
        self.tree = []

    def sift_up(self, index):
        while self.tree[index] < self.tree[(index - 1) // 2]:
            changer = self.tree[index]
            self.tree[index] = self.tree[(index - 1) // 2]
            self.tree[(index - 1) // 2] = changer
            index = (index - 1) // 2

    def sift_down(self, index):
        while 2 * index + 1 < len(self.tree):
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            j = left_child
            if len(self.tree)-1 <= j:
                break
            if (right_child < len(self.tree)-1) and (self.tree[right_child] < self.tree[left_child]):
                j = right_child
            if self.tree[index] <= self.tree[j]:
                break
            changer = self.tree[index]
            self.tree[index] = self.tree[j]
            self.tree[j] = changer
            index = j

    def add(self, val):
        if len(self.tree) == 0:
            self.tree.append(val)
        else:
            index = len(self.tree)
            self.tree.append(val)
            self.sift_up(index)

    def print_heap(self):
        for i in range(len(self.tree)):
            print(self.tree[i], end=' ')

    def replace(self, index):
        changer = self.tree[index]
        self.tree[index] = self.tree[-1]
        self.tree[-1] = changer
        self.sift_down(index)
        self.tree.pop(-1)
        return changer

    def heap_sort(self):
        sorted_heap = []
        while len(self.tree) != 0:
            sorted_heap.append(self.replace(0))
        self.tree = sorted_heap


a = Heap()
a.add(1)
a.add(2)
a.add(3)
a.add(6)
a.add(5)
a.add(9)
a.add(8)
a.add(11)
a.add(4)
a.add(11)
a.add(112)
a.add(133)
a.add(12)
a.add(17)
a.add(19)
a.add(7)
a.replace(4)
a.heap_sort()
a.print_heap()
