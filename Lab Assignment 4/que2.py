INT_MAX=1000000
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
            if self.q[p].path_cost > self.q[i].path_cost:
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
        if l<len(self.q) and self.q[l].path_cost<self.q[mi].path_cost:
            mi=l
        if r<len(self.q) and self.q[r].path_cost<self.q[mi].path_cost:
            mi=r
        if mi!=i:
            self.q[i],self.q[mi]=self.q[mi],self.q[i]
            self.heapify(mi)
            
class Node:
    def __init__(self,state,parent,action,path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

class Problem:
    def __init__(self,start,goal,grid):
        self.initial_state=start
        self.goal_state=goal
        self.grid=grid
        self.r=len(grid)
        self.c=len(grid[0])
    
    def INITIAL(self):
        return self.initial_state

    def Is_Goal(self,state):
        return state==self.goal_state
    
    def ACTIONS(self,s):
        res=[]
        r,c=s
        steps=[(-1,0),(1,0),(0,1),(0,-1)]

        for i,j in steps:
            a=i+r
            b=j+c
            if 0<=a<self.r and 0<=b<self.c:
                if self.grid[a][b]!=1 and self.grid[a][b]!=5:
                    res.append((a,b))

        return res
    def RESULT(self,state,action):
        return action
    
    def ACTION_COST(self,s,a,S):
        return 1
    

def Expand(problem, node):
    n=[]
    s=node.state

    for action in problem.ACTIONS(s):
        ns =problem.RESULT(s, action)
        cost = node.path_cost + problem.ACTION_COST(s, action, ns)

        child = Node(state=ns,parent=node,action=action,path_cost=cost)
        n.append(child)
    return n


def bestfirstsearch(problem):
    frontier = PQ()

    i,j=problem.initial_state
    a,b=problem.goal_state

    start_node=Node(state=problem.INITIAL(),parent=None,action=None,path_cost=0)
    
    frontier.insert(start_node)
    reached = {problem.INITIAL(): start_node.path_cost}

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.Is_Goal(node.state):
            return node

        for child in Expand(problem, node):
            f_cost=child.path_cost

            if child.state not in reached or f_cost<reached[child.state]:
                reached[child.state]=f_cost
                frontier.insert(child)

    return None


def get_best_path(goal_node):
    path = []
    n = goal_node
    while n:
        path.append(n.state)
        n = n.parent
    return path[::-1]


def main():
    #In grid 0 is for free space agent can move there, 1 is for room where agent cannot move and 5 is for internal walls agent cannot pass through them
    grid = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,1,0,1,5,0,0,5,0,5,0,0,0,1], 
        [1,0,0,0,5,0,0,5,0,5,0,0,0,1],
        [1,1,0,1,5,0,0,0,0,5,0,0,0,1],
        [1,0,0,1,5,0,0,0,0,5,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,'S',1],
        [1,1,1,1,1,1,0,0,1,1,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,1,1],
        [1,1,1,1,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,1,1,1,1,1],
        [1,1,1,1,1,1,0,0,0,0,0,0,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,1],
        [1,1,1,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,'G',0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ]

    start = (5, 12)
    goal  = (13, 6)

    problem = Problem(start, goal,grid)
    result = bestfirstsearch(problem)

    if result:
        path = get_best_path(result)
        print("Best-First path:", path)
        print("Path length:", len(path))
    else:
        print("No path found")

main()


