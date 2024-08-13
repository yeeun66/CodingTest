# DFS와 BFS
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램

from collections import deque

def dfs():
    stk = [v]
    visit = [0]*(n+1)
    while stk:
        cur = stk.pop()
        if visit[cur]: continue
        visit[cur] = True
        print(cur, end=" ")
        stk.extend(graph[cur][::-1]) # 리스트 역순으로 뒤집기 (작은걸 top에 위치 시키려고)
    print()

def bfs():
    queue = deque([v]) # 시작 vertex를 먼저 큐에 넣어줌
    visit = [0]*(n+1)
    while queue:
        cur = queue.popleft() # 맨 앞 원소 pop
        if visit[cur]: continue # 방문 한거면 무시
        visit[cur] = True 
        print(cur, end=" ")
        queue.extend(graph[cur]) # 방금 방문 끝낸 원소의 인접 노드들을 큐에 넣어줌

n, m, v = map(int, input().split()) # vertex, edge, start vertex
# graph 생성
graph = [[] for _ in range(n+1)] # n+1 길이의 리스트 생성 (정점번호 1~N 까지라 그냥 n+1 만큼 만들어준거)
for _ in ' '*m: # m번 반복
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

graph = list(map(sorted, graph)) # 인접한 node가 여러개면 오름차순 방문이니까 정렬 해줘야함
print("graph: ", graph)

dfs()
bfs()