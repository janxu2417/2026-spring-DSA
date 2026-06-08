import sys

class BinaryHeap:  ## 小根堆
    def __init__(self):
        self.heap = []

    def _perc_up(self, i):
        while i:
            f = i - 1 >> 1
            if self.heap[i] < self.heap[f]:
                self.heap[i], self.heap[f] = self.heap[f], self.heap[i]
                i = f
            else:
                break

    def _perc_down(self, i, size):
        while i < size // 2:
            min_idx = self.get_min_child(i, size)
            if self.heap[i] <= self.heap[min_idx]:
                break
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            i = min_idx

    def get_min_child(self, i, size):
        if i * 2 + 2 >= size:
            return i * 2 + 1
        if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
            return i * 2 + 1
        return i * 2 + 2

    def insert(self, val):
        self.heap.append(val)
        self._perc_up(len(self.heap) - 1)

    def delete(self):
        t = len(self.heap) - 1
        self.heap[0], self.heap[t] = self.heap[t], self.heap[0]
        self._perc_down(0, t)
        return self.heap.pop()

def main():
    bh = BinaryHeap()
    it = iter(sys.stdin.read().split())
    n = int(next(it))
    ans = []
    for _ in range(n):
        tp = int(next(it))
        if tp == 1:
            x = int(next(it))
            bh.insert(x)
        else:
            ans.append(bh.delete())

    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
