# BFS 문제 다시 풀기
# 바이러스 - 실버3

# 1. 입력 & 그래프에 연결 표시
    # 연결 노드쌍 입력 받을 때에는 양 방향 그래프로, 양쪽에 모두 표시
    # 편의상 그래프 (n+1) 크기로 생성
# 2. BFS 탐색 시작 (1번부터 시작, 큐에 1넣고 시작)
    # queue empty까지 다음을 반복
        # queue에서 현재 값을 popleft 한다
        # 방금 pop한 값과 연결 값, 즉 graph[cur]의 값들을 중 방문하지 않은 값을 
        #   모두 큐에 넣고, 해당 값들은 방문 처리한다
# 3. visit 배열의 합 -1 값 출력

from collections import deque
N = int(input())
E = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(E) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
que = deque([1])
visit = [0] * (N+1)
visit[1] = 1

while que : 
    cur = que.popleft()
    for i in graph[cur] :
        if not visit[i] : 
            que.append(i)
            visit[i] = 1

print(sum(visit)-1)