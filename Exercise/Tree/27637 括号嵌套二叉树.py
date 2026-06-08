class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(s):
    i = 0
    n = len(s)
    def parse():
        nonlocal i
        if i >= n or s[i] == '*':
            i += 1
            return None

        node = TreeNode(s[i])
        i += 1
        if i < n and s[i] == '(':
            i += 1
            node.left = parse()
            i += 1 ## skip ','
            node.right = parse()
            i += 1 ## skip ')'
        return node

    return parse()

def inorder(root):
    if root is None:
        return ''
    return inorder(root.left) + root.val + inorder(root.right)

def preorder(root):
    if root is None:
        return ''
    return root.val + preorder(root.left) + preorder(root.right)

def main():
    for _ in range(int(input())):
        s = input().strip().replace(" ", "")
        root = build_tree(s)
        print(preorder(root))
        print(inorder(root))

if __name__ == '__main__':
    main()