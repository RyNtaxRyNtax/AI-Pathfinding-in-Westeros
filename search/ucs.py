from env.domain import GameState
import heapq


def ucs(initial_state: "GameState"):
    counter = 0
    frontier = []
    heapq.heappush(frontier, (0, counter, initial_state, []))
    visited = {initial_state: 0}
    while frontier:
        current_state: "GameState"
        cost_so_far, _, current_state, actions = heapq.heappop(frontier)
        if current_state.is_goal_state():
            return actions

        for action, step_cost, next_state in current_state.get_successors():
            new_cost = cost_so_far + step_cost
            if next_state not in visited or new_cost < visited[next_state]:
                visited[next_state] = new_cost
                counter += 1
                heapq.heappush(
                    frontier, (new_cost, counter, next_state, actions + [action])
                )
    return []
