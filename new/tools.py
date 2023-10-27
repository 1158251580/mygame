from collections import deque
from typing import Any


class Counter:
    # 计算递归次数，返回递归数组
    def __init__(self, fun):
        self._fun = fun
        self.count = 0
        self.path = deque([])

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # 多算一步起始位置
        self.count += 1
        self.path.append(args[1])
        return self._fun(*args,**kwds)
    
    def __del__(self):
        # 析构函数，清除计数器
        self.count = 0
        self.path.clear()