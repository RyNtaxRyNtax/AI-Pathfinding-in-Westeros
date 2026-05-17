from env.domain import GameState
import heapq
from typing import List, Tuple, Dict


def a_star(initial_state: "GameState") -> List[str]:
    def heuristic(state: "GameState") -> int:
        player_pos = state.get_agent_position()
        targets = state.get_targets_positions()
        if not targets:
            return 0
        min_distance = float("inf")
        for target in targets:
            dist = abs(player_pos[0] - target[0]) + abs(player_pos[1] - target[1])
            if dist < min_distance:
                min_distance = dist
        return min_distance

    counter = 0
    frontier: List[Tuple[int, int, "GameState", List[str], int]] = []
    initial_priority = heuristic(initial_state)
    heapq.heappush(frontier, (initial_priority, counter, initial_state, [], 0))
    visited: Dict["GameState", int] = {initial_state: 0}
    while frontier:
        current_state: "GameState"
        _, _, current_state, actions, cost_so_far = heapq.heappop(frontier)
        if current_state.is_goal_state():
            return actions
        for action, step_cost, next_state in current_state.get_successors():
            new_cost = cost_so_far + step_cost
            if next_state not in visited or new_cost < visited[next_state]:
                visited[next_state] = new_cost
                priority = new_cost + heuristic(next_state)
                counter += 1
                heapq.heappush(
                    frontier,
                    (priority, counter, next_state, actions + [action], new_cost),
                )
    return []
