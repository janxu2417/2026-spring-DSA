class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(s):
    i = 0
    def parse():
        nonlocal i
        if s[i] == '.':
            i += 1
            return None
        node = TreeNode(s[i])
        i += 1
        node.left = parse()
        node.right = parse()
        return node
    return parse()

def inorder(root):
    if root is None:
        return ''
    return inorder(root.left) + root.val + inorder(root.right)

def postorder(root):
    if root is None:
        return ''
    return postorder(root.left) + postorder(root.right) + root.val

def main():
    preorder = input()
    root = build_tree(preorder)
    print(inorder(root))
    print(postorder(root))

if __name__ == '__main__':
    main()