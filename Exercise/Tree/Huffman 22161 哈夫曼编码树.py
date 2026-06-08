import heapq

class Node:
    def __init__(self, weight : int, char = None):
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None
    def __lt__(self, other):
        if self.weight == other.weight:
            return self.char < other.char
        return self.weight < other.weight

def build_huffman_tree(char_freq):
    heap = [Node(weight, char) for char, weight in char_freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(left.weight + right.weight, min(left.char, right.char))
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heap[0]

def encoding(root):
    char_code = {}
    stack = [(root, '')]
    while stack:
        node, path = stack.pop()
        if not node.left:
            char_code[node.char] = path
            continue
        stack.append((node.left, path + '0'))
        stack.append((node.right, path + '1'))
    return char_code

def decoding(code, root):
    node = root
    ans = []
    for c in code:
        if not node.left:
            ans.append(node.char)
            node = root
        if c == '0':
            node = node.left
        else:
            node = node.right
    ans.append(node.char)
    return ''.join(ans)

def main():
    n = int(input())
    char_freq = {}
    for _ in range(n):
        data = input().split()
        char_freq[data[0]] = int(data[1])
    root = build_huffman_tree(char_freq)
    char_code = encoding(root)
    while True:
        try:
            s = input()
            if s[0] in ('0', '1'):
                print(decoding(s, root))
            else:
                print(''.join(char_code[c] for c in s))
        except EOFError:
            break

if __name__ == '__main__':
    main()