# 연결 요소의 개수
# DFS

# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. 
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 같은 간선은 한 번만 주어진다.

# (연결 요소의 조건)
# 1. 연결 요소에 속한 모든 정점을 연결하는 경로가 있어야 한다.
# 2. 다른 연결 요소에 속한 정점과 연결하는 경로가 있으면 안된다.

import sys

def dfs(v) :
    stk = [v]

    while stk :
        cur = stk.pop()
        if visit[cur] : continue
        visit[cur] = True
        stk.extend(graph[cur])
    return

count = 0
N, M = map(int, sys.stdin.readline().split()) # node 수, edge 수

visit = [0]*(N+1)
# graph 생성
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)    
    graph[y].append(x)

# dfs 이용해서 연결요소 갯수 세기
for i in range(1, N+1) :
    if visit[i] == 0 :
        dfs(i)
        count +=1
print(count)