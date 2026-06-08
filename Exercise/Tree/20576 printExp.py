class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def infix_to_postfix(expr, pre):
    out = []
    st = []
    for token in expr:
        if token in ('True', 'False'):
            out.append(token)
        elif token == '(':
            st.append(token)
        elif token == ')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()
        else:
            while st and st[-1] != '(' and pre[st[-1]] >= pre[token]:
                out.append(st.pop())
            st.append(token)
    while st:
        out.append(st.pop())
    return out

def build_tree(postfix, pre):
    st = []
    for token in postfix:
        node = TreeNode(token)
        if token in pre:
            node.left = st.pop()
            if token != 'not':
                node.right = st.pop()
        st.append(node)
    return st[-1]

def to_infix(root, pre):
    val = root.val
    if val in ('True', 'False'):
        return [val]

    left = root.left
    if val == 'not':
        res = to_infix(left, pre)
        if pre[left.val] < pre[val]:
            res = ['('] + res + [')']
        return ['not'] + res

    right = root.right
    left_exp = to_infix(left, pre)
    right_exp = to_infix(right, pre)
    if pre[left.val] < pre[val]:
        left_exp = ['('] + left_exp + [')']
    if pre[right.val] < pre[val]:
        right_exp = ['('] + right_exp + [')']

    return right_exp + [val] + left_exp

def main():
    pre = {'not': 3, 'and': 2, 'or': 1}
    s = input().strip().split()
    postfix = infix_to_postfix(s, pre)
    # print(' '.join(postfix))
    root = build_tree(postfix, pre)
    pre['True'] = 4
    pre['False'] = 4
    print(' '.join(to_infix(root, pre)))

if __name__ == '__main__':
    main()