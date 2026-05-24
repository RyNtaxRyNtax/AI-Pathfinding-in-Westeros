# AI Pathfinding in Westeros

[README in Persian](README_FA.md) 

This project implements various informed and uninformed search algorithms to solve a pathfinding problem in a Westeros-themed grid world. The objective is to guide Arya Stark through a map to reach all targets while managing obstacles, terrain costs, and a moving enemy (the Night King).

## Project Overview

The project is a fully observable, deterministic, sequential, static, discrete environment where an agent (Arya) must navigate to collect multiple targets.

### Key Components

- **Agent (A):** Arya Stark, who moves in four directions (Up, Down, Left, Right).
- **Targets (T):** Specific locations Arya must reach.
- **Enemy (E):** The Night King, who moves along a predefined path. Colliding with him results in a high penalty unless Arya has the weapon.
- **Weapon (W):** A Valyrian steel dagger. Once collected, Arya can "kill" the Night King if they collide, removing him from the map.
- **Terrain Types:**
  - **Snow:** Normal terrain with a passing cost of 5.
  - **Ice (B):** Slippery terrain with a high passing cost of 100.
  - **Rock/Crate (R):** Impassable obstacles.

## Search Algorithms

The project implements the following search strategies:

1.  **Breadth-First Search (BFS):**
    - **Logic:** Explores level by level to find the path with the fewest steps.
    - **Data Structure:** **Queue (FIFO)** (`collections.deque`).
2.  **Uniform Cost Search (UCS):**
    - **Logic:** Explores nodes based on the lowest cumulative path cost ($g(n)$), accounting for terrain weights (Snow vs. Ice).
    - **Data Structure:** **Priority Queue** (`heapq`).
3.  **Depth-Limited Search (DLS):**
    - **Logic:** A depth-first search that terminates at a specified depth to prevent infinite loops.
    - **Data Structure:** **Stack (LIFO)** (Python list).
4.  **A* Search:**
    - **Logic:** Uses $f(n) = g(n) + h(n)$ to prioritize nodes.
    - **Data Structure:** **Priority Queue** (`heapq`).

### The Heuristic: Beyond Manhattan Distance

While Manhattan distance is common, it is insufficient here for two reasons:
- **Obstacles:** It ignores rocks/crates, leading to underestimation.
- **Multiple Targets:** It only considers the nearest goal, ignoring the total work required.

#### Why MST and Dijkstra?
To create a high-performance heuristic:
- **MST (Minimum Spanning Tree):** Used to estimate the total cost to connect and visit *all* remaining targets.
- **Dijkstra Map:** Pre-calculates actual shortest path distances between points *around obstacles*.

By using Dijkstra-informed distances as the edges for an MST of the remaining targets, we get an extremely accurate heuristic that drastically reduces node expansion.

## Project Structure

- `main.py`: The entry point to run the simulations.
- `env/`: Contains the environment logic.
  - `domain.py`: Defines the `GameState` and transition logic.
  - `map.py`: Handles map parsing and loading.
  - `constants.py`: Stores configuration values like costs and rewards.
  - `rendering.py`: Handles the visual representation using Pygame.
- `search/`: Contains the search algorithm implementations (`bfs.py`, `ucs.py`, `dls.py`, `a_star.py`).
- `env/src/maps/`: Contains various map files (`easy`, `medium`, `hard`).

## How to Run

1.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the project using:
    ```bash
    python main.py
    ```

You can modify `main.py` to change the map or the search algorithm used for the simulation.

## License

This project is licensed under the MIT License.
