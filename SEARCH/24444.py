# N개의 정점과 M개의 간선으로 구성된 무방향 그래프(undirected graph)가 주어진다. 
# 정점 번호는 1번부터 N번이고 모든 간선의 가중치는 1이다. 
# 정점 R에서 시작하여 너비 우선 탐색으로 노드를 방문할 경우 노드의 방문 순서를 출력하자.
# 너비 우선 탐색 의사 코드는 다음과 같다. 인접 정점은 오름차순으로 방문한다.

# 입력
# 첫째 줄에 정점의 수 N (5 ≤ N ≤ 100,000), 간선의 수 M (1 ≤ M ≤ 200,000), 시작 정점 R (1 ≤ R ≤ N)이 주어진다.
# 다음 M개 줄에 간선 정보 u v가 주어지며 정점 u와 정점 v의 가중치 1인 양방향 간선을 나타낸다. 
# (1 ≤ u < v ≤ N, u ≠ v) 모든 간선의 (u, v) 쌍의 값은 서로 다르다.

# 출력
# 첫째 줄부터 N개의 줄에 정수를 한 개씩 출력한다. 
# i번째 줄에는 정점 i의 방문 순서를 출력한다. 시작 정점의 방문 순서는 1이다. 시작 정점에서 방문할 수 없는 경우 0을 출력한다.

import sys
from collections import deque

def bfs() :
    queue = deque([R])
    visit = [0] * (N+1)
    result = [0] * (N+1) # 이 문제용 결과 저장 리스트
    count = 1
    while queue: 
        cur = queue.popleft()
        if visit[cur] : continue
        visit[cur] = True
        queue.extend(graph[cur])
        result[cur] = count
        count += 1
    for i in range(1, N+1) :
        print(result[i])

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)] # (정점 수 + 1) 만큼 2차원 배열 초기화
for _ in range(M) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
graph = list(map(sorted, graph))

bfs()