# 알고리즘 수업 - 깊이 우선 탐색 1
# DFS

# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어짐 
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1
# 정점 R에서 시작하여 깊이 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력
# 인접 정점은 오름차순으로 방문

# 답은 잘 출력 되는데 왜 시간초과? -> 해결!
# 그냥 visit 배열에 True가 아닌 count를 넣으면 되었다!!
import sys

input = sys.stdin.readline

def dfs() :
    stk = [R]
    visit = [0] * (N+1)
    count = 1
    while stk :
        cur = stk.pop()
        if visit[cur] : continue
        visit[cur] = count
        stk.extend(graph[cur][::-1])
        count += 1
    for i in range(1, N+1) :
        print(visit[i])

N, M, R = map(int, input().split()) # node수, edge수, 시작 node 번호

graph = [[] for _ in range(N+1)]
for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
graph = list(map(sorted, graph))

dfs()