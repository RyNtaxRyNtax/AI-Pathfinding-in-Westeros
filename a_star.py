from env.domain import GameState
import heapq
from typing import List, Tuple, Dict


def a_star(initial_state: "GameState") -> List[str]:
    crates = set(initial_state.get_crates_positions())
    grid_shape = initial_state.get_grid_size()
    all_targets = list(initial_state.get_targets_positions())

    def build_dijkstra_map(start_pos: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
        distances = {start_pos: 0}
        pq = [(0, start_pos)]
        while pq:
            d, current = heapq.heappop(pq)
            if d > distances.get(current, float("inf")):
                continue
            r, c = current
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < grid_shape[0] and 0 <= nc < grid_shape[1]:
                    if (nr, nc) not in crates:
                        cost = initial_state.get_terrain_cost((nr, nc))
                        new_dist = d + cost
                        if new_dist < distances.get((nr, nc), float("inf")):
                            distances[(nr, nc)] = new_dist
                            heapq.heappush(pq, (new_dist, (nr, nc)))
        return distances

    dist_maps = {}
    for t in all_targets:
        dist_maps[t] = build_dijkstra_map(t)

    def get_dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
        if p1 in dist_maps:
            return dist_maps[p1].get(p2, 10000)
        if p2 in dist_maps:
            return dist_maps[p2].get(p1, 10000)
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    def heuristic(state: "GameState") -> int:
        player_pos = state.get_agent_position()
        targets = list(state.get_targets_positions())
        if not targets:
            return 0

        def mst_weight(nodes: List[Tuple[int, int]]) -> int:
            if not nodes or len(nodes) < 2:
                return 0
            unvisited = set(nodes)
            start_node = unvisited.pop()
            visited_nodes = {start_node}
            cost = 0
            while unvisited:
                min_edge = float("inf")
                best_node = None
                for v in visited_nodes:
                    for u in unvisited:
                        d = get_dist(v, u)
                        if d < min_edge:
                            min_edge = d
                            best_node = u
                visited_nodes.add(best_node)
                unvisited.remove(best_node)
                cost += min_edge
            return cost

        def cost_to_collect_all(
            start_pos: Tuple[int, int], targets_list: List[Tuple[int, int]]
        ) -> int:
            if not targets_list:
                return 0
            min_dist = min(get_dist(start_pos, t) for t in targets_list)
            return min_dist + mst_weight(targets_list)

        return cost_to_collect_all(player_pos, targets)

    counter = 0
    frontier: List[Tuple[int, int, "GameState", List[str], int]] = []
    initial_priority = heuristic(initial_state)
    heapq.heappush(frontier, (initial_priority, counter, initial_state, [], 0))
    visited: Dict["GameState", int] = {initial_state: 0}
    while frontier:
        _, _, current_state, actions, cost_so_far = heapq.heappop(frontier)
        if cost_so_far > visited.get(current_state, float("inf")):
            continue
        if current_state.is_goal_state():
            return actions
        for action, step_cost, next_state in current_state.get_successors():
            if next_state.is_collision_state():
                continue
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
