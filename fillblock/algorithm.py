from collections import deque
from copy import deepcopy
from terrain import removable,attack
from chess import Dogface

def createPath(index,level=8):
    raw = index[0]
    col = index[1]
    path = [(5,5),(5,4),(5,3),(5,2),(4,2),(4,3),(3,3),(3,4),(3,5)]
    while level:
        level -= 1
    return path

def is_over(path):
    pass
