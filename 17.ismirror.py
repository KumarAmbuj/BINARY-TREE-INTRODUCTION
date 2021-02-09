class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def ismirror(node1,node2):

    if node1==None and node2==None:
        return True
    if node1!=None and node2!=None:
        return (node1.val == node2.val) and ismirror(node1.left, node2.right) and ismirror(node1.right, node2.left)
    else:
        return False

root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(ismirror(root,root))


root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.right = Node(3)

root.right.right = Node(3)
print(ismirror(root,root))

