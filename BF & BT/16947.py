# 서울 지하철 2호선

''' 
로직 
1. 순환선 구하기(cycle 구하기) - 순환선에 해당하는 모든 노드 set에 넣어두기 (DFS)
    - dfs로 탐색
        - 1번 노드부터 탐색 시작.
        - 방문하려는 노드가 아직 방문 안했으면 방문처리 후 스택에 추가
        - 방문하려는 노드가 이미 방문 되어있는데, 그 노드가 현재노드의 부모 노드가 아니라면, 사이클 인 것.
        - 그럼 그 노드는 set에 추가 후 현재 노드도 set에 추가 현재 노드의 부모도 추가 처음 

2. 각 노드별로 순환선과의 거리 탐색 (BFS)
    - 순환선에 해당하는 노드면 바로 0 출력
    - 순환선에 없는 노드면 순환선 만날 때 까지 bfs 탐색하며 만나면 depth 출력
'''

from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)] # 양방향 그래프
for _ in range(N) : 
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def find_cycle_node(st, cur, parent) : 
    cycle = set()
    cycle.add(st)

    while True : 
        cycle.add(cur)
        if not parent[cur] : break
        if cur == parent[st] : break
        cur = parent[cur]
        if cur in cycle : break
    
    return cycle

def dfs() :
    visited = [0] * (N+1)
    stk = [1]
    visited[1] = 1
    parent = {}
    for n in range(N+1) : parent[n] = []
    while stk : 
        cur = stk.pop()
        for g in graph[cur] : 
            if not visited[g] : 
                visited[g] = 1
                parent[g] = cur # g의 부모는 cur
                stk.append(g)
            else : 
                if g != parent[cur] :
                    return find_cycle_node(g, cur, parent)


def bfs(x) : 
    visited = [0] * (N+1)
    que = deque([x])
    visited[x] = 1
    while que : 
        cur = que.pop()
        for g in graph[cur] : 
            if not visited[g] : 
                if g in cycle_node : return visited[cur]
                que.append(g)
                visited[g] = visited[cur] + 1

cycle_node = dfs() 

for i in range(1, N+1) :
    if i in cycle_node : print(0, end=" ")
    else : print(bfs(i), end=" ")