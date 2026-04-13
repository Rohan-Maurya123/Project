import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
from src.simulation import load_map, generate_random_map, get_start_goal
from src.path_planning import astar, dijkstra, bfs

# Set page config
st.set_page_config(page_title="AI Autonomous Navigation System", layout="wide")

# App Title
st.title("🚀 AI Autonomous Navigation System")
st.markdown("---")

# Sidebar - Settings
st.sidebar.header("Navigation Settings")

# 1. Map Selection/Generation
st.sidebar.subheader("🗺️ Map Selection")
map_option = st.sidebar.selectbox("Choose Map Source", ["Random Map", "Default Map (CSV)"])

if map_option == "Random Map":
    rows = st.sidebar.slider("Rows", 5, 50, 20)
    cols = st.sidebar.slider("Cols", 5, 50, 20)
    density = st.sidebar.slider("Obstacle Density", 0.0, 0.5, 0.2)
    if st.sidebar.button("🔄 Generate New Map"):
        st.session_state.grid = generate_random_map(rows, cols, density)
        st.session_state.start, st.session_state.goal = get_start_goal(st.session_state.grid)
elif map_option == "Default Map (CSV)":
    if st.sidebar.button("📂 Load Default Map"):
        st.session_state.grid = load_map("data/grid_map.csv")
        st.session_state.start, st.session_state.goal = get_start_goal(st.session_state.grid)

# Initialize grid if not present
if 'grid' not in st.session_state:
    st.session_state.grid = generate_random_map(20, 20, 0.2)
    st.session_state.start, st.session_state.goal = get_start_goal(st.session_state.grid)

# 2. Algorithm Selection
st.sidebar.subheader("🧠 Pathfinding Algorithm")
algorithm = st.sidebar.selectbox("Choose Algorithm", ["A*", "Dijkstra", "BFS"])
allow_diagonal = st.sidebar.checkbox("Allow Diagonal Movement", value=True)
heuristic_mode = st.sidebar.selectbox("Heuristic (A* only)", ["manhattan", "euclidean"])

# 3. Start/Goal selection (using text inputs for now)
st.sidebar.subheader("📍 Coordinates")
start_x = st.sidebar.number_input("Start X", 0, st.session_state.grid.shape[0]-1, st.session_state.start[0])
start_y = st.sidebar.number_input("Start Y", 0, st.session_state.grid.shape[1]-1, st.session_state.start[1])
goal_x = st.sidebar.number_input("Goal X", 0, st.session_state.grid.shape[0]-1, st.session_state.goal[0])
goal_y = st.sidebar.number_input("Goal Y", 0, st.session_state.grid.shape[1]-1, st.session_state.goal[1])

st.session_state.start = (start_x, start_y)
st.session_state.goal = (goal_x, goal_y)

# Run Pathfinding
if st.sidebar.button("🚀 Find Path"):
    start_time = time.time()
    
    if algorithm == "A*":
        path, nodes_visited = astar(st.session_state.grid, st.session_state.start, st.session_state.goal, allow_diagonal, heuristic_mode)
    elif algorithm == "Dijkstra":
        path, nodes_visited = dijkstra(st.session_state.grid, st.session_state.start, st.session_state.goal, allow_diagonal)
    elif algorithm == "BFS":
        path, nodes_visited = bfs(st.session_state.grid, st.session_state.start, st.session_state.goal, allow_diagonal)
    
    end_time = time.time()
    st.session_state.path = path
    st.session_state.nodes_visited = nodes_visited
    st.session_state.execution_time = (end_time - start_time) * 1000 # in ms
else:
    if 'path' not in st.session_state:
        st.session_state.path = []
        st.session_state.nodes_visited = 0
        st.session_state.execution_time = 0

# Main Area Layout
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ Navigation Grid")
    
    # Visualization using Plotly
    fig = go.Figure()

    # Plot grid
    fig.add_trace(go.Heatmap(
        z=st.session_state.grid,
        colorscale=[[0, 'white'], [1, 'black']],
        showscale=False,
        hoverinfo='skip'
    ))

    # Plot Start/Goal
    fig.add_trace(go.Scatter(
        x=[st.session_state.start[1]], y=[st.session_state.start[0]],
        mode='markers', name='Start', marker=dict(color='green', size=15)
    ))
    fig.add_trace(go.Scatter(
        x=[st.session_state.goal[1]], y=[st.session_state.goal[0]],
        mode='markers', name='Goal', marker=dict(color='red', size=15)
    ))

    # Plot Path
    if st.session_state.path:
        px = [p[1] for p in st.session_state.path]
        py = [p[0] for p in st.session_state.path]
        fig.add_trace(go.Scatter(
            x=px, y=py,
            mode='lines+markers', name='Path', line=dict(color='blue', width=4)
        ))

    fig.update_layout(
        width=700, height=700,
        xaxis=dict(autorange='reversed'),
        yaxis=dict(autorange='reversed'),
        margin=dict(l=20, r=20, t=20, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Performance Metrics")
    
    # Metrics Cards
    m1, m2 = st.columns(2)
    m1.metric("Nodes Visited", st.session_state.nodes_visited)
    m2.metric("Time (ms)", f"{st.session_state.execution_time:.2f}")
    
    st.markdown("---")
    
    if st.session_state.path:
        st.success(f"Path Found! Length: {len(st.session_state.path)}")
        # Show path details
        with st.expander("Show Path Coordinates"):
            st.write(st.session_state.path)
    else:
        st.warning("No path found yet.")

    st.markdown("### Instructions")
    st.info("""
    1. Configure map settings in the sidebar.
    2. Choose a pathfinding algorithm.
    3. Adjust start and goal coordinates.
    4. Click 'Find Path' to see the result.
    """)
