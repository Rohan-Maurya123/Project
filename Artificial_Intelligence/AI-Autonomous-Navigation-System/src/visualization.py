import matplotlib.pyplot as plt

def plot_grid(grid, path=None):
    plt.figure(figsize=(10, 10))
    plt.imshow(grid, cmap='gray_r') # Invert gray for better visibility

    if path:
        x = [p[1] for p in path]
        y = [p[0] for p in path]
        plt.plot(x, y, color='blue', linewidth=2, marker='o', markersize=4)
        # Mark Start/Goal
        plt.plot(path[0][1], path[0][0], 'gs', markersize=10, label='Start')
        plt.plot(path[-1][1], path[-1][0], 'rs', markersize=10, label='Goal')
        plt.legend()
    else:
        print("No path provided to plot.")

    plt.title("AI Autonomous Navigation System - Path Visualization")
    plt.savefig("outputs/result.png")
    plt.show()