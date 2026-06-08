## 双单调栈构建笛卡尔树
import sys
class Node:
    def __init__(self, data, h):
        self.val = data
        self.left = None
        self.right = None
        self.h = h # 这里的 height 代表优先级，行号越大优先级越高

def preorder(root):
    res = []
    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ''.join(res)

def process_data(all_nodes):
    # 1. 按照字母排序，获取中序遍历序列
    all_nodes.sort(key = lambda x: x.val)
    # 2. 寻找根节点：height 最大的节点是整棵树的根
    root = max(all_nodes, key=lambda x: x.h)
    # 3. 正向单调栈找左孩子
    st = []
    for node in all_nodes:
        left = None
        while st and st[-1].h < node.h:
            left = st.pop()
        node.left = left
        st.append(node)
    # 4. 反向单调栈找右孩子
    st = []
    for node in all_nodes[::-1]:
        right = None
        while st and st[-1].h < node.h:
            right = st.pop()
        node.right = right
        st.append(node)

    print(preorder(root))

def solve():
    all_nodes = []
    current_height = 0
    lines = sys.stdin.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == '*' or line == '$':
            process_data(all_nodes)
            all_nodes.clear()
            current_height = 0
            if line == '$':
                break
        else:
            for c in line:
                all_nodes.append(Node(c, current_height))
            current_height += 1

if __name__ == '__main__':
    solve()