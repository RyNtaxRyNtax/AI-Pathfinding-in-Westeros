import os
import warnings

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
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
warnings.filterwarnings("ignore")

from env import play

# from search.bfs import bfs
# from search.dls import dls
from search.ucs import ucs

# from search.a_star import a_star


if __name__ == "__main__":
    play("easy-no-weapon", ucs, delay=500)
    play("medium-no-weapon", ucs, delay=500)
    play("hard-no-weapon2", ucs, delay=500)
