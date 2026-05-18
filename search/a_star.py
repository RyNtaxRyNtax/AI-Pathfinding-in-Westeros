from env.domain import GameState
import heapq
from typing import List, Tuple, Dict


def a_star(initial_state: "GameState") -> List[str]:
    def heuristic(state: "GameState") -> int:
        player_pos = state.get_agent_position()
        targets = list(state.get_targets_positions())
        if not targets:
            return 0

        def manhattan(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def mst_weight(nodes: List[Tuple[int, int]]) -> int:
            if not nodes or len(nodes) < 2:
                return 0
            unvisited = set(nodes)
            start_node = unvisited.pop()
            visited = {start_node}
            cost = 0
            while unvisited:
                min_edge = float("inf")
                best_node = None
                for v in visited:
                    for u in unvisited:
                        d = manhattan(v, u)
                        if d < min_edge:
                            min_edge = d
                            best_node = u
                visited.add(best_node)
                unvisited.remove(best_node)
                cost += min_edge
            return cost

        def cost_to_collect_all(
            start_pos: Tuple[int, int], targets_list: List[Tuple[int, int]]
        ) -> int:
            if not targets_list:
                return 0
            min_dist = min(manhattan(start_pos, t) for t in targets_list)
            return min_dist + mst_weight(targets_list)

        return cost_to_collect_all(player_pos, targets)

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
