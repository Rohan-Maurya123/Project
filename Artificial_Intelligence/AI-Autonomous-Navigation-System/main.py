from src.simulation import load_map, get_start_goal, generate_random_map
from src.path_planning import astar
from src.visualization import plot_grid

def main():
    # Use generate_random_map for variety
    grid = generate_random_map(20, 20, 0.2)
    start, goal = get_start_goal(grid)

    path, nodes_visited = astar(grid, start, goal, allow_diagonal=True)

    print(f"Path found! Length: {len(path)}")
    print(f"Nodes visited: {nodes_visited}")

    plot_grid(grid, path)

if __name__ == "__main__":
    main()