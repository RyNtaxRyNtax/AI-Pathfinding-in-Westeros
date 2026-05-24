"""
University: University of Isfahan
Faculty: Mathematics and Statistics
Branch: Computer Science
Course: Artificial Intelligence
Professor: Dr. Faria Nasiri Mofakham
TAs: MehrAzin Marzough, Mohammad Karimi, Anahita Honarmandian
Project: Implementing Informed and Uninformed Search Algorithms for a
Fully Observable, Deterministic, Sequential, Static, Discrete, Multi-Agent Environment
"""

import os
import warnings
import time
from tabulate import tabulate

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
os.environ["PYTHONWARNINGS"] = "ignore"
warnings.filterwarnings("ignore")

from env import play
from search.bfs import bfs
from search.dls import dls
from search.ucs import ucs
from search.a_star import a_star

CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"


def print_banner():
    banner = f"""
{CYAN}{BOLD}========================================================
         WINTER IS COMING: PATHFINDING AI SUITE
========================================================{RESET}
    """
    print(banner)


def run_benchmark():
    ALGORITHMS = {
        "BFS Search": bfs,
        "DLS Search": dls,
        "UCS Search": ucs,
        "A* Search": a_star,
    }
    MAPS = [
        "easy-no-weapon",
        "medium-no-weapon",
        "hard-no-weapon2",
        "medium-weapon",
    ]
    benchmark_results = []
    print_banner()
    for algo_name, algo_func in ALGORITHMS.items():
        print(f"{MAGENTA}{BOLD}>>> INITIALIZING ALGORITHM: {algo_name} <<<{RESET}\n")
        time.sleep(1)
        for map_name in MAPS:
            print(f"{MAGENTA}▶️ Algorithm:{RESET} {BOLD}{algo_name}{RESET}")
            print(f"{YELLOW}▶️ Target Map:{RESET} {BOLD}{map_name}{RESET}")
            try:
                score, expanded_nodes = play(map_name, algo_func, delay=1)
                benchmark_results.append([algo_name, map_name, score, expanded_nodes])
            except Exception as e:
                print(f"Error running {map_name}: {e}")
                benchmark_results.append([algo_name, map_name, "Error", "Error"])
            print(f"{GREEN}{'-'*56}{RESET}\n")
            time.sleep(0.5)
    print(f"\n{CYAN}{BOLD}=== FINAL BENCHMARK REPORT ==={RESET}")
    headers = ["Algorithm", "Map", "Score", "Expanded Nodes"]
    print(
        tabulate(
            benchmark_results,
            headers=headers,
            tablefmt="fancy_grid",
            stralign="center",
            numalign="center",
        )
    )
    print("\n")


if __name__ == "__main__":
    try:
        run_benchmark()
        print(f"{CYAN}{BOLD}=== BENCHMARK COMPLETE ==={RESET}\n")
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Execution aborted by user.{RESET}\n")
