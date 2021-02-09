class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Stack():
    s=[]
    return s
def Push(s,x):
    s.append(x)
def Pop(s):
    return s.pop()
def Size(s):
    return len(s)

def isop(ch):
    return  ch=='+' or ch=='-' or ch=='*' or ch=='/'

class BinaryTree():
    def __init__(self):
        self.root=None

    def expression(self,s):

        stack=Stack()

        for ch in s:
            newnode=Node(ch)

            if not isop(ch):
                Push(stack,newnode)
            else:
                node1=Pop(stack)
                node2=Pop(stack)

                newnode.right=node1
                newnode.left=node2
                Push(stack,newnode)

        return Pop(stack)

    def inorder(self,root):

        if root:
            self.inorder(root.left)
            print(root.val,end=' ')
            self.inorder(root.right)


postfix = "ab+ef*g*-"
b=BinaryTree()
root=b.expression(postfix)
b.inorder(root)



