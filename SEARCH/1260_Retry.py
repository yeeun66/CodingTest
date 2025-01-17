# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램

# 방법 다시 정리
# 1. 그래프 생성 및 초기화
# 2. DFS (stack)
# 3. BFS (queue)

import sys
from collections import deque
input = sys.stdin.readline

def dfs() :
    stk = [v] # 스택 생성 (사실 걍 리스트임)
    visit = [0] * (n+1)
    while stk : 
        cur = stk.pop()
        if visit[cur] : continue
        visit[cur] = True
        print(cur, end=" ")
        stk.extend(graph[cur][::-1]) # 가장 작은수가 스택의 위쪽에 있어야 하므로 뒤집어서 넣기
    print()

def bfs() :
    queue = deque([v])
    visit = [0] * (n+1)
    while queue :
        cur = queue.popleft() # 큐의 앞쪽 원소를 먼저 꺼내
        if visit[cur] : continue
        visit[cur] = True
        print(cur, end=" ")
        queue.extend(graph[cur])
    print()
    

n, m, v = map(int, input().split()) # 노드수, 엣지수, 시작노드
graph = [[] for _ in range(n+1)] # 노드수 + 1 만큼 만들기

for _ in range(m) : # 엣지수 만큼 반복
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

graph = list(map(sorted, graph)) # 리스트의 각 하위 리스트를 개별적으로 정렬

dfs()
bfs()