class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def findexpression(root):

    if root==None:
        return 0

    if root.left==None and root.right==None:
        return root.val

    l=int(findexpression(root.left))
    r=int(findexpression(root.right))

    if root.val=='+':
        root.val=l+r

    elif root.val=='-':
        root.val=l-r

    elif root.val=='*':
        root.val=l*r

    elif root.val=='/':
        root.val=l/r
    return root.val

root = Node('+')
root.left = Node('*')
root.left.left = Node('5') 
root.left.right = Node('4')
root.right = Node('-')
root.right.left = Node('100')
root.right.right = Node('20')
print(findexpression(root))


