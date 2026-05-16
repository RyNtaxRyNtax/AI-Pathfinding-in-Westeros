from env.domain import GameState
import heapq


def a_star(initial_state: "GameState"):

    def heuristic(state):
        # TODO: Implement Manhattan Distance here in the next step
        # Returning 0 for now keeps the engine running as UCS (baseline)
        return 0

    counter = 0
    frontier = []
    # Priority Queue stores: (priority_score, counter, current_state, list_of_actions, cost_so_far)
    initial_priority = heuristic(initial_state)
    heapq.heappush(frontier, (initial_priority, counter, initial_state, [], 0))
    visited = {initial_state: 0}
    while frontier:
        current_state: "GameState"
        _, _, current_state, actions, cost_so_far = heapq.heappop(frontier)
        if current_state.is_goal_state():
            return actions
        for action, step_cost, next_state in current_state.get_successors():
            new_cost = cost_so_far + step_cost
            if next_state not in visited or new_cost < visited[next_state]:
                visited[next_state] = new_cost
                # The A* Priority Math: f(n) = g(n) + h(n)
                priority = new_cost + heuristic(next_state)
                counter += 1
                heapq.heappush(
                    frontier,
                    (priority, counter, next_state, actions + [action], new_cost),
                )
    return []
