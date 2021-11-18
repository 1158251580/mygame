from collections import deque
from copy import deepcopy
from terrain import Attack, Removable

# 可移动范围
def movable(m,raw,col,step):
    for i in range(col-step,col+step+1):
        if i >= 0 and i <= m.real_height:
            left = raw - (step-abs(i-col)) if raw - abs(i-col) >= 0 else 0
            right = raw + (step-abs(i-col)) if raw + abs(i-col) <= m.real_width else m.real_width
            for j in range(left,right+1):
                if i == col and j == raw:
                    pass
                else:
                    if not m.empty_map[i][j]:
                        m.empty_map[i][j] = 1

# 洪水算法
def flood(m,cur_obj):
    next_d = deque([cur_obj.get_cur_index()])
    over = deque([])
    step = cur_obj.step+1
    while step:
        cur_d = deepcopy(next_d)
        next_d = deque([])
        while cur_d:
            index = cur_d.popleft()
            raw = index[0]
            col = index[1]
            if raw-1>=0 and (raw-1,col) not in over and m.empty_map[raw-1][col] == 0:
                next_d.append((raw-1,col))
            if raw+1<m.real_height and (raw+1,col) not in over and m.empty_map[raw+1][col] == 0:
                next_d.append((raw+1,col))
            if col-1>=0 and (raw,col-1) not in over and m.empty_map[raw][col-1] == 0:
                next_d.append((raw,col-1))
            if col+1<m.real_width and (raw,col+1) not in over and m.empty_map[raw][col+1] == 0:
                next_d.append((raw,col+1))
            over.append(index)
        step -= 1
    over.popleft()
    for raw,col in over:
        m.empty_map[raw][col] = Removable(raw,col)
    for raw,col in next_d:
        m.empty_map[raw][col] = Attack(raw,col)