import numpy as np
import pandas as pd
import random

def load_map(file_path):
    try:
        return pd.read_csv(file_path, header=None).values
    except Exception as e:
        print(f"Error loading map: {e}")
        return None

def generate_random_map(rows, cols, obstacle_density=0.2):
    grid = np.zeros((rows, cols))
    for r in range(rows):
        for c in range(cols):
            if random.random() < obstacle_density:
                grid[r][c] = 1
    return grid

def get_start_goal(grid):
    rows, cols = grid.shape
    # Default start at top-left, goal at bottom-right
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    
    # Ensure start and goal are not obstacles
    if grid[start[0]][start[1]] == 1:
        grid[start[0]][start[1]] = 0
    if grid[goal[0]][goal[1]] == 1:
        grid[goal[0]][goal[1]] = 0
        
    return start, goal