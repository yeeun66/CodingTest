# 안전 영역
# 어떤 지역의 높이 정보가 주어졌을 때, 장마철에 물에 잠기지 않는 안전한 영역의 최대 개수를 계산하는 프로그램

# (높이 K이하인 모든 지점이 물에 잠기면 + BFS) 이걸 브루트포스로 1부터 배열의 max값 까지 계산 후, 
#    안전 영역에 최대 갯수도 어떤 변수에 저장 해 놓고 새로 찾은 안전 영역 갯수가 더 많으면 업데이트
# 지금 문제는 한 영역 구한 후 큐 엠티 되었을 때 다시 스타트 노드 찾아서 또 다른 영역 구하는 거
# -> 그냥 무지성 for 문? 

# dfs 함수 - 이중 for문
#     -1이 아니고, 방문했던 지점이 아니면 그 지점(스타트 노드)으로 부터 queue로 상하좌우 탐색.
#     queue 엠티면 count 1증가 시키고 
#     다시 아까 스타트 노드 였던 점부터 다시 브루트포스로 -1이 아니고, 방문하지 않았던 점을 찾아서 다시 queue에 넣고 상하좌우 탐색

# 왜 자꾸 메모리 초과가 나지 _ 큐 중복 삽입 문제??? --> 해결
import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우
dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1]
safe = 0

def bfs(a) :
    count = 0
    queue = deque()
    visit = [[0] * N for _ in range(N)] # 방문 여부 체크 metrics
    
    for i in range(N) :
        for j in range(N) :
            if not visit[i][j] and graph[i][j] >= a :
                queue.append((i, j)) 
                while queue :
                    x, y = queue.popleft()

                    for m in range(4) :
                        nx = x + dx[m]  
                        ny = y + dy[m]  
                        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny] and graph[nx][ny] >= a :
                            queue.append((nx, ny))
                            visit[nx][ny] = True # 메모리 초과) 이 문장 없어서 났었음! 방문 상태 바로바로 업데이트 해주기!!
                        visit[x][y] = True
                count += 1
    
    global safe
    safe = max(safe, count)
    
N = int(input())

graph = []
[graph.append(list(map(int, input().split()))) for _ in range(N)] # 이것도 메모리 줄이는 방법중 하나 _ 근데 해결 못함

max_v = max(map(max, graph)) # 최대 높이 만큼 반복 위해 최대 높이 구하기
# print("max_v: ", max_v) 
for k in range(1, max_v+1) : bfs(k)

print(safe)