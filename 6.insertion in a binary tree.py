class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,x):
        newnode=Node(x)

        if self.root==None:
            self.root=newnode
            return self.root

        queue=Queue()
        Enqueue(queue,self.root)

        while(Size(queue)):
            rem=Dequeue(queue)

            if rem.left==None:
                rem.left=newnode
                break
            else:
                Enqueue(queue,rem.left)

            if rem.right==None:
                rem.right=newnode
                break
            else:
                Enqueue(queue,rem.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val,end=' ')
            self.inorder(root.right)

b=BinaryTree()
root=b.insert(1)
b.insert(2)
b.insert(3)
b.inorder(root)

