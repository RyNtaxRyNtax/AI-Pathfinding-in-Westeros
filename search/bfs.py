from env.domain import GameState
from collections import deque


def bfs(initial_state: "GameState"):
    frontier = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)
    while frontier:
        current_state: "GameState"
        current_state, actions = frontier.popleft()
        if current_state.is_goal_state():
            return actions
        for action, _, next_state in current_state.get_successors():
            if next_state not in visited:
                visited.add(next_state)
                frontier.append((next_state, actions + [action]))
    return []
