class Deque:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def popleft(self):
        return self.data.pop(0)

    def __bool__(self):
        return len(self.data) != 0


def bfs_algo(start, goal):
    start = tuple(map(tuple, start))   
    goal  = tuple(map(tuple, goal))

    count = 1

    queue = Deque()
    queue.append((start, [start]))

    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            print(count)
            return path

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    a, b = i, j

        moves = [(-1,0),(1,0),(0,-1),(0,1)]

        for dx, dy in moves:
            x, y = a + dx, b + dy
            if 0 <= x < 3 and 0 <= y < 3:
                new_state = [list(row) for row in state]

                new_state[a][b], new_state[x][y] = new_state[x][y], new_state[a][b]
                new_state = tuple(map(tuple, new_state))

                if new_state not in visited:
                    count = count + 1
                    visited.add(new_state)
                    queue.append((new_state, path + [new_state]))

    return None

start = [
    [7,2,4],
    [5,0,6],
    [8,3,1]
]

goal = [
    [1,2,3],
    [4,5,6],
    [7,8,0]
]

count = 0
result = bfs_algo(start, goal)
print(result)
print(count)