from env.domain import GameState


def dls(initial_state: "GameState", limit=50):
    frontier = [(initial_state, [], 0)]
    visited = {initial_state: 0}
    while frontier:
        current_state, actions, depth = frontier.pop()
        if current_state.is_goal_state():
            return actions
        if depth < limit:
            for action, _, next_state in current_state.get_successors():
                next_depth = depth + 1
                if next_state not in visited or visited[next_state] > next_depth:
                    visited[next_state] = next_depth
                    frontier.append((next_state, actions + [action], next_depth))
    return []
