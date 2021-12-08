from collections import deque
from copy import deepcopy
from terrain import removable,attack
from chess import Dogface

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
        m.empty_map[raw][col] = removable
    for raw,col in next_d:
        m.empty_map[raw][col] = attack


def city_block_distance(cur_index,target_index):
    # 城市街道距离
    c_raw,c_col = cur_index
    t_raw,t_col = target_index
    return abs(c_raw-t_raw)+abs(c_col-t_col)


def priority(m,cur_obj):
    # 目标优先级判断
    target = None
    distance = m.real_width+m.real_height
    for i in m.empty_map:
        for j in i:
            if isinstance(j,Dogface):
                if city_block_distance(cur_obj.get_cur_index(),j.get_cur_index()) < distance:
                    distance = city_block_distance(cur_obj.get_cur_index(),j.get_cur_index())
                    target = j
    return target

def a_start(m,cur_obj,target_obj):
    # A星算法
    step = cur_obj.step+1
    next_d = cur_obj.get_cur_index()
    over = deque([])
    while step:
        raw = next_d[0]
        col = next_d[1]
        distance = []
        coord = []   
        if raw-1>=0 and (raw-1,col) not in over:
            if m.empty_map[raw-1][col]==removable:
                coord.append((raw-1,col))
                distance.append(city_block_distance((raw-1,col),target_obj.get_cur_index())+1)
            elif m.empty_map[raw-1][col]==target_obj:
                over.append((raw,col))
                break
        if raw+1<m.real_height and (raw+1,col) not in over: 
            if m.empty_map[raw+1][col]==removable:
                coord.append((raw+1,col))
                distance.append(city_block_distance((raw+1,col),target_obj.get_cur_index())+1)
            elif m.empty_map[raw+1][col]==target_obj:
                over.append((raw,col))
                break
        if col-1>=0 and (raw,col-1) not in over :
            if m.empty_map[raw][col-1]==removable:
                coord.append((raw,col-1))
                distance.append(city_block_distance((raw,col-1),target_obj.get_cur_index())+1)
            elif m.empty_map[raw][col-1]==target_obj:
                over.append((raw,col))
                break
        if col+1<m.real_width and (raw,col+1) not in over :
            if m.empty_map[raw][col+1]==removable:
                coord.append((raw,col+1))
                distance.append(city_block_distance((raw,col+1),target_obj.get_cur_index())+1)
            elif m.empty_map[raw][col+1]==target_obj:
                over.append((raw,col))
                break
        over.append((raw,col))
        if distance and coord:
            next_d = coord[distance.index(min(distance))]
            step -= 1
        else:
            break
    return over