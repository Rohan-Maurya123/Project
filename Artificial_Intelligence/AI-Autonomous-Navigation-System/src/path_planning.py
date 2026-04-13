import heapq
import numpy as np

def heuristic(a, b, mode="manhattan"):
    if mode == "manhattan":
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    elif mode == "euclidean":
        return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return 0

def get_neighbors(current, rows, cols, allow_diagonal=True):
    neighbors = []
    # 4-way connectivity
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if allow_diagonal:
        # 8-way connectivity
        directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        
    for dx, dy in directions:
        nx, ny = current[0] + dx, current[1] + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            # For diagonal movement, the cost is sqrt(2), otherwise 1
            cost = np.sqrt(dx**2 + dy**2)
            neighbors.append(((nx, ny), cost))
    return neighbors

def astar(grid, start, goal, allow_diagonal=True, heuristic_mode="manhattan"):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    cost_so_far = {start: 0}
    nodes_visited = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_visited += 1

        if current == goal:
            break

        for neighbor, move_cost in get_neighbors(current, rows, cols, allow_diagonal):
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
                
            new_cost = cost_so_far[current] + move_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(goal, neighbor, heuristic_mode)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    path = []
    if goal in came_from:
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
    
    return path, nodes_visited

def dijkstra(grid, start, goal, allow_diagonal=True):
    # Dijkstra is A* with zero heuristic
    return astar(grid, start, goal, allow_diagonal, heuristic_mode=None)

def bfs(grid, start, goal, allow_diagonal=True):
    rows, cols = len(grid), len(grid[0])
    queue = [start]
    came_from = {start: None}
    nodes_visited = 0

    while queue:
        current = queue.pop(0)
        nodes_visited += 1

        if current == goal:
            break

        for neighbor, _ in get_neighbors(current, rows, cols, allow_diagonal):
            if grid[neighbor[0]][neighbor[1]] == 1:
                continue
            if neighbor not in came_from:
                queue.append(neighbor)
                came_from[neighbor] = current

    path = []
    if goal in came_from:
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
    
    return path, nodes_visited