class Node:
    def __init__(self,g,b,boat,parent=None, action="",depth=0):
        self.g=g
        self.b=b
        self.boat=boat
        self.parent=parent
        self.action=action
        self.depth=depth

    def is_goal(self):
        return self.g==0 and self.b==0 and self.boat==1

    def is_valid(self):
        ng=3-self.g
        nb=3-self.b

        if self.g<0 or self.b<0 or ng<0 or nb<0:
            return False
        if (self.g>0 and self.b>self.g):
            return False
        if (ng>0 and nb>ng):
            return False
        return True


moves=[(1,0,"1G"),(2,0,"2G"),(0,1,"1B"),(0,2,"2B"),(1,1,"1G1B")]

def is_cycle(node, child):
    temp=node
    while temp:
        if temp.g==child.g and temp.b==child.b and temp.boat==child.boat:
            return True
        temp=temp.parent
    return False

def expand(node):
    res=[]
    for g,b,name in moves:
        if node.boat==0:
            child=Node(node.g-g,node.b-b,1,node,name,node.depth+1)
        else:
            child=Node(node.g+g,node.b+b,0,node,name,node.depth+1)

        if child.is_valid()  and not is_cycle(node, child):
            res.append(child)
    return res


def DLS(limit,st):
    start=st
    stack=[start]
    explored=0

    while stack:
        node=stack.pop()
        explored+=1

        if node.is_goal():
            return node,explored

        if node.depth < limit:
            stack.extend(expand(node))

    return None,explored


def print_path(node, explored):
    if node is None:
        print("Cutoff occurred — Goal not found within depth limit")
        print("Total states explored:", explored)
        return

    path=[]
    while node:
        path.append(node)
        node=node.parent

    path.reverse()

    print("\nSolution Steps:")
    for p in path:
        print(p.action, (p.g,p.b,p.boat))

    print("\nTotal steps to reach goal:", len(path)-1)
    print("Total states explored:", explored)

st=Node(3,3,0)
limit=int(input("Enter the limit for dls:"))

goal, explored = DLS(limit,st)
print_path(goal, explored)


