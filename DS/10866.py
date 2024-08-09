# 덱 구현

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

queue = deque()

for _ in range(N) :
    parts = input().split() # parts는 공백을 구분한 리스트 형태로 저장됨 [cmd, value]
    if len(parts) == 2:
        cmd, x = parts[0], parts[1]
    if len(parts) == 1:
        cmd = parts[0]
        x = None
    
    if x is None :
        if parts[0] == 'size' : print(len(queue))
        elif parts[0] == 'empty' :
            if not queue : print(1)
            else : print(0)
        elif parts[0] == 'front' :
            if queue: print(queue[0])
            else : print(-1)
        elif parts[0] == 'back' :
            if queue: print(queue[-1])
            else : print(-1)
        elif parts[0] == 'pop_front' : 
            if queue: print(queue.popleft())
            else : print(-1)
        elif parts[0] == 'pop_back' :
            if queue: print(queue.pop())
            else : print(-1)
    else: 
        if parts[0] == 'push_front' : queue.appendleft(x)
        elif parts[0] == 'push_back' : queue.append(x)