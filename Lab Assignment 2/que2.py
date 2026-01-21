goal = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


explored = 0   


def dfs(state, depth, visited, limit):
    global explored

    explored += 1   

    if state == goal:
        print("Goal found at depth:", depth)
        return True

    if depth >= limit:
        return False

    visited.add(state)

    x, y = find_blank(state)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            new_tuple = tuple(tuple(row) for row in new_state)

            if new_tuple not in visited:
                if dfs(new_tuple, depth + 1, visited, limit):
                    return True

    visited.remove(state)
    return False



start_state = (
    (7, 2, 4),
    (5, 0, 6),
    (8, 3, 1)
)

visited = set()
depth_limit = 60

found = dfs(start_state, 0, visited, depth_limit)

print("States explored by DFS:", explored)

if not found:
    print("Goal not found within depth limit")