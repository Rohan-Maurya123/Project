# AI Autonomous Navigation System 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

This project is an AI-powered autonomous navigation system that simulates and visualizes pathfinding algorithms in a grid-based environment. It features a modern, interactive web-based UI for real-time algorithm comparison and map exploration.

---

## ✨ Features

-   **🧠 Multiple Pathfinding Algorithms**:
    -   **A***: Heuristic-driven efficient search (supports Manhattan & Euclidean).
    -   **Dijkstra**: Guaranteed shortest path search.
    -   **BFS**: Step-based search (optimal for unweighted grids).
-   **🎨 Modern Interactive UI**:
    -   Built with **Streamlit** for a seamless user experience.
    -   **Plotly** integration for interactive and responsive grid visualization.
-   **🗺️ Dynamic Map Support**:
    -   Generate **random maps** with customizable obstacle density.
    -   Load **custom maps** from CSV files.
-   **⚙️ Advanced Navigation Settings**:
    -   Support for **8-way (diagonal) movement**.
    -   Configurable start and goal coordinates.
-   **📊 Real-time Performance Metrics**:
    -   Track **nodes visited** and **execution time** for algorithm comparison.

---

## 🛠️ Tech Stack

-   **Core**: Python 3.10+
-   **UI/Frontend**: [Streamlit](https://streamlit.io/)
-   **Visualization**: [Plotly](https://plotly.com/python/), [Matplotlib](https://matplotlib.org/)
-   **Data Processing**: [NumPy](https://numpy.org/), [Pandas](https://pandas.pydata.org/)

---

## 🚀 Getting Started

### Prerequisites

-   Python installed on your system (3.10 or higher recommended).
-   (Optional but recommended) A virtual environment.

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/AI-Autonomous-Navigation-System.git
    cd AI-Autonomous-Navigation-System
    ```

2.  **Create and activate a virtual environment** (optional):
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Linux/macOS
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Running the System

You can run the system in two ways:

#### 1. Interactive Web UI (Recommended)
This provides the best experience for visualization and testing.
```bash
streamlit run app.py
```

#### 2. CLI/Script Mode
For quick execution and static plot generation.
```bash
python main.py
```

---

## 📂 Project Structure

```text
├── app.py              # Main Streamlit application
├── main.py             # CLI entry point
├── src/                # Core logic source code
│   ├── path_planning.py # Pathfinding algorithm implementations
│   ├── simulation.py   # Map loading and generation logic
│   └── visualization.py # Static plotting utilities
├── data/               # Map data storage
├── outputs/            # Generated visualization results
├── requirements.txt    # Project dependencies
└── LICENSE             # MIT License
```

---

## 🧠 Algorithms Explained

### A* (A-Star)
The most popular pathfinding algorithm. It uses a combination of the actual cost from the start and a heuristic estimate to the goal to find the shortest path efficiently.

### Dijkstra's Algorithm
A foundational algorithm that explores nodes in all directions equally until it reaches the goal, guaranteeing the shortest possible path.

### Breadth-First Search (BFS)
An uninformed search that explores all neighbors at the current depth before moving deeper. It finds the shortest path in terms of the number of nodes visited.

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
