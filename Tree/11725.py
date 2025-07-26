# 트리의 부모 찾기

'''
로직
1. 입력으로 양방향 그래프 구축
2. 1번 노드부터 bfs 탐색하며 자식관계 딕셔너리 제작
3. 제작된 자식관계 딕셔너리 2번 노드부터 출력 
'''

from collections import deque 

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

parent = {}

visited = [0] * (N+1)
que = deque([1])
visited[1] = 1
while que : 
    cur = que.popleft()
    for g in graph[cur] :
        if not visited[g] : 
            visited[g] = 1
            que.append(g)
            parent[g] = cur

for i in range(2, N+1) : print(parent[i])