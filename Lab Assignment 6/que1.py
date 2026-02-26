city_map={
    0 : "Chicago",
    1 : "Detroit",
    2 : "Cleveland",
    3 : "Indianapolis",
    4 : "Columbus",
    5 : "Buffalo",
    6 : "Pittsburgh",
    7 : "Syracuse",
    8 : "Philadelphia",
    9 : "Baltimore",
    10 : "New York",
    11 : "Providence",
    12 : "Boston",
    13 : "Portland"
}

heuristic=[860,610,550,780,640,400,470,260,270,360,215,50,0,107]



INT_MAX = 10000000

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
            if self.q[p].h > self.q[i].h:
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
        if l<len(self.q) and self.q[l].h<self.q[mi].h:
            mi=l
        if r<len(self.q) and self.q[r].h<self.q[mi].h:
            mi=r
        if mi!=i:
            self.q[i],self.q[mi]=self.q[mi],self.q[i]
            self.heapify(mi)

class Node:
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action
        self.h = heuristic[state]

class Problem:
    def __init__(self,start,goal,adj):
        self.initial_state=start
        self.goal_state=goal
        self.mat=adj
    
    def INITIAL(self):
        return self.initial_state

    def Is_Goal(self,state):
        return state==self.goal_state
    
    def ACTIONS(self,s):
        res=[]
        for node in range(len(self.mat)):
            if self.mat[s][node]!=INT_MAX and node!=s:
                res.append(node)
        return res
    def RESULT(self,state,action):
        return action
    
    def ACTION_COST(self,s,a,S):
        return self.mat[s][S]
    
def Expand(problem,node):
    res = []
    s = node.state

    for action in problem.ACTIONS(s):
        new = problem.RESULT(s, action)
        child = Node(state=new,parent=node,action=action)
        res.append(child)

    return res

def Greedy(problem):
    frontier=PQ()
    start=Node(state=problem.INITIAL(),parent=None,action=None)

    frontier.insert(start)
    reached={problem.INITIAL() : start}
    count=0

    while not frontier.isEmpty():
        node=frontier.pop()
        count+=1
        if problem.Is_Goal(node.state):
            print("Cities Visited",count)
            return node
        for child in Expand(problem,node):
            s=child.state
            if s not in reached :
                reached[s] = child
                frontier.insert(child)

    return None
        
def get_best_path(goal_node):
    path = []
    node = goal_node

    while node is not None:
        path.append(node.state)
        node = node.parent

    path.reverse()
    return path
def cost(path,adj):
    c=0
    for i in range(len(path)-1):
        c+=adj[path[i]][path[i+1]]
    return c
def addEdge(graph, u, v, d):
    graph[u][v] = d
    graph[v][u] = d

def main():
    n = 14
    adj = []

    for i in range(n):
        row = []
        for j in range(n):
            row.append(INT_MAX)
        adj.append(row)
    for i in range(n):
        adj[i][i] = 0

    addEdge(adj, 0, 1, 283)
    addEdge(adj, 0, 2, 345)
    addEdge(adj, 0, 3, 182)
    addEdge(adj, 3, 4, 176)
    addEdge(adj, 4, 2, 144)
    addEdge(adj, 4, 6, 185)
    addEdge(adj, 2, 1, 169)
    addEdge(adj, 2, 5, 189)
    addEdge(adj, 2, 6, 134)
    addEdge(adj, 1, 5, 256)
    addEdge(adj, 5, 7, 150)
    addEdge(adj, 5, 6, 215)
    addEdge(adj, 6, 8, 305)
    addEdge(adj, 6, 9, 247)
    addEdge(adj, 9, 8, 101)
    addEdge(adj, 8, 10, 97)
    addEdge(adj, 10, 11, 181)
    addEdge(adj, 10, 12, 215)
    addEdge(adj, 12, 11, 50)
    addEdge(adj, 12, 13, 107)
    addEdge(adj, 7, 12, 312)
    addEdge(adj, 7, 8, 253)
    addEdge(adj, 7, 10, 254)

    problem = Problem(0, 12, adj)
    result = Greedy(problem)

    if result is not None:
        path = get_best_path(result)
        print("Best path :")
        for i in path:
            print(city_map[i],sep=" ")

        path_cost=cost(path,adj)
        print(path_cost)
    else:
        print("No path found")

    
main()
    
    