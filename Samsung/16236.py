# 아기 상어

# 0. 필요한 변수 
    # size(상어 현재 크기),
    # fish(현재 상어가 먹은 물고기 수, 근데 상어 크기 업데이트 하면 얘는 다시 0이 됨)
    # sec(경과시간), arr(격자배열 N*N),  dx,dy (상하좌우)
    # !!! 물고기 선택 우선 순위를 만들어 줘야 함. fishes = []
        # 모든 먹을 수 있는 물고기 담아놓고, 우선순위 높은거 하나 먹기 위한 배열

# 종료 조건까지 다음을 반복
# 탐색전, 현재 상어의 위치 따로 x, y에 담아두고 그 위치 값은 0으로 바꿈
# 1.현재 상어 크기보다 작은 물고기 존재 확인
    # 값이 모두 0이거나, 작은 물고기 없으면 반복 종료
# 2. bfs 탐색 시작 (먹을 수 있는 물고기 후보 찾기)
    # 현재 상어 위치를 시작으로, 상좌하우 순으로 탐색
        # 범위 맞고, 아직 방문 전인 칸에 대해 
            # 상어와 같은 크기는 큐에 추가하고 (방문 표시 = 이전 + 1)
            # 상어보다 작은 물고기는 큐에 추가하고 (방문 표시 = 이전 + 1)
            # fishes 배열에 (거리, 좌표 추가)
# 3. 먹을 수 있는 물고기 없으면 종료
    # 있다면, 정렬해서 하나만 꺼내 먹어
        # 시간 추가, 먹은 물고기 비우기, 먹은 고기수 추가, 상어 현 위치 업데이트
        # 상어 크기 증가 조건 만족하면, 증가

from collections import deque
dx = [-1, 0, 1, 0]  # 상좌하우
dy = [0, -1, 0, 1]

N = int(input())
arr = []
for _ in range(N) : arr.append(list(map(int, input().split())))

size = 2
sec, fish = 0, 0

def bfs(x, y) :
    global sec, fish, size

    while True : 
        que = deque()
        que.append((x, y))
        visited = [[-1]* N for _ in range(N)] # 방문 처리
        visited[x][y] = 0
        fishes = [] # 중요!!! 

        # BFS로 먹을 수 있는 물고기 일단 모두 찾기 !!!
        while que : 
            x, y = que.popleft()

            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and visited[nx][ny] == -1 :

                    if arr[nx][ny] == size or arr[nx][ny] == 0: 
                        que.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                    elif 0 < arr[nx][ny] < size : # 먹을 수 있는 물고기
                        que.append((nx, ny))
                        visited[nx][ny] = visited[x][y] + 1
                        fishes.append([visited[nx][ny], nx, ny]) # 거리, x, y 저장
        
        if not fishes : # 이제 먹을 물고기 없으면 종료
            print(sec)
            return
        
        fishes.sort() # 정렬
        fd, fx, fy = fishes[0] # 우선 순위 높은 물고기 하나 먹기
        arr[fx][fy] = 0
        sec += fd
        fish += 1
        x, y = fx, fy # 상어 현위치 업데이트

        if size == fish : # 상어크기 증가
            size += 1
            fish = 0

for i in range(N) :
    for j in range(N) :
        if arr[i][j] == 9 :
            arr[i][j] = 0
            bfs(i, j)