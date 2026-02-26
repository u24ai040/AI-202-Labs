class PQ:
    def __init__(self):
        self.q=[]

    def isEmpty(self):
        return len(self.q)==0
    def right(self,i):
        return 2*i + 2 
    def left(self,i):
        return 2*i + 1
    def parent(self,i):
        return (i-1)//2
    def insert(self, val):
        self.q.append(val)
        i = len(self.q) - 1

        while i>0:
            p=self.parent(i)
            if self.q[p].f > self.q[i].f:
                self.q[p], self.q[i] = self.q[i], self.q[p]
                i=p
            else:
                break

    def pop(self):
        if self.isEmpty():
            return None
        if len(self.q)==1:
            return self.q.pop()
        r=self.q[0]
        self.q[0]=self.q.pop()
        self.heapify(0)
        return r
    def heapify(self,i):
        l=self.left(i)
        r=self.right(i)
        mi=i
        if l<len(self.q) and self.q[l].f<self.q[mi].f:
            mi=l
        if r<len(self.q) and self.q[r].f<self.q[mi].f:
            mi=r
        if mi!=i:
            self.q[i],self.q[mi]=self.q[mi],self.q[i]
            self.heapify(mi)

def heuristic(pos, remaining):
        if len(remaining)==0:
            return 0
        x,y=pos
        return min(abs(x-rx)+abs(y-ry) for rx,ry in remaining)
class Node:
    
    def __init__(self,state,parent,action,g,remaining):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g
        self.remaining = remaining
        self.h = heuristic(state,remaining)
        self.f = self.g + self.h

    def __lt__(self,other):
        return (self.f,self.g) < (other.f,other.g)


class MazeProblem:

    def __init__(self,grid):
        self.grid=grid
        self.n=len(grid)
        self.start=None
        self.rewards=set()

        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j]==2:
                    self.start=(i,j)
                if grid[i][j]==3:
                    self.rewards.add((i,j))

    def INITIAL(self):
        return self.start,self.rewards

    def Is_Goal(self,state):
        pos,remaining=state
        return len(remaining)==0

    def ACTIONS(self,state):
        x,y=state[0]
        acts=[]
        for dx,dy,a in [(1,0,'D'),(-1,0,'U'),(0,1,'R'),(0,-1,'L')]:
            nx,ny=x+dx,y+dy
            if 0<=nx<self.n and 0<=ny<self.n and self.grid[nx][ny]!=1:
                acts.append((nx,ny,a))
        return acts

    def RESULT(self,state,action):
        (nx,ny,a)=action
        pos,remaining=state
        new_remaining=set(remaining)
        if (nx,ny) in new_remaining:
            new_remaining.remove((nx,ny))
        return ( (nx,ny), frozenset(new_remaining) )

    def ACTION_COST(self,s,S):
        return 1
def Expand(problem,node):

    children=[]
    state=(node.state,node.remaining)

    for action in problem.ACTIONS(state):

        new_state,new_remaining = problem.RESULT(state,action)
        child_g=node.g+1

        child=Node(
            state=new_state,
            parent=node,
            action=action[2],
            g=child_g,
            remaining=new_remaining
        )

        children.append(child)

    return children
def A_star(problem):

    frontier=PQ()

    start_pos,start_rem=problem.INITIAL()
    start=Node(start_pos,None,None,0,frozenset(start_rem))

    frontier.insert(start)
    reached={(start.state,start.remaining):start}

    while not frontier.isEmpty():

        node=frontier.pop()

        if problem.Is_Goal((node.state,node.remaining)):
            return node

        for child in Expand(problem,node):

            s=(child.state,child.remaining)

            if s not in reached or child.g<reached[s].g:
                reached[s]=child
                frontier.insert(child)

    return None
def get_path(node):
    p=[]
    while node:
        p.append(node.state)
        node=node.parent
    return p[::-1]
       
maze=[
[2,0,0,0,1],
[0,1,0,0,3],
[0,3,0,1,1],
[0,1,0,0,1],
[3,0,0,0,3]
]

problem=MazeProblem(maze)
result=A_star(problem)

if result:
    p=get_path(result)
    print("Path:")
    for i in p:
        print(i)
    print("Steps:",len(p)-1)
else:
    print("No Solution")
