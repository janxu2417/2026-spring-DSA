class BinaryHeap:  ## 大根堆
    def __init__(self):
        self.heap = []

    def _perc_down(self, i):
        size = len(self.heap)
        while i < size // 2:
            min_idx = self.get_max_child(i)
            if self.heap[i] >= self.heap[min_idx]:
                break
            self.heap[i], self.heap[min_idx] = self.heap[min_idx], self.heap[i]
            i = min_idx

    def get_max_child(self, i):
        size = len(self.heap)
        if i * 2 + 2 >= size:
            return i * 2 + 1
        if self.heap[i * 2 + 1] < self.heap[i * 2 + 2]:
            return i * 2 + 2
        return i * 2 + 1

    def heapify(self, not_heap):
        self.heap = not_heap[:]
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._perc_down(i)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    bh = BinaryHeap()
    bh.heapify(a)
    print(' '.join(map(str, bh.heap)))

if __name__ == '__main__':
    main()