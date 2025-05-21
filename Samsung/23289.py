# 온풍기 안녕!
# 한번에 맞긴 했지만, 중복 or 비효율 적인 코드 조금 있는 것 같으니까 한번 더 리뷰 하기!!
# 로직 
# 0. 초기 작업
    # R열 C행 배열 모두 0으로 초기화
    # 배열 정보 받기: 1~4 => 방향이 (오른, 왼, 위, 아래) 인 온풍기 위치 -- 온풍기 배열에 좌표로 저장
        # 5 => 온도 조사해야 하는 칸 -- 좌표로 저장 (5번 종료 조건 시 사용할 것)
# 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴 - increase_temp() 함수
    # 온풀기 배열에서 좌표 하나씩 꺼내며, 주변 온도 상승 시키기 
    # 방문 처리 초기화 후, (BFS)
    # 처음 시작 좌표 = 온풍기 좌표 큐에 넣기
    # 큐 엠티까지 다음을 반복
    # BFS인데, 상하좌우 탐색이 아니라 인접 3칸 탐색
        # (중간 과정 있는 이유는 이 좌표와 x,y 사이가 벽인지 알아보려고)
        # 방향이 양 옆일 때 (0, 1), (0, -1) 
            # 1) (x, y) -> (x-1, y) -> (x-1, y+dy) (최종 좌표만 큐에 넣어)
            # 2) (x, y) -> (x, y+dy)
            # 3) (x, y) -> (x+1, y) -> (x+1, y+dy)
        # 방향이 위 아래일 때 (-1, 0), (1, 0)
            # 1) (x, y) -> (x, y-1) -> (x+dx, y-1)
            # 2) (x, y) -> (x+dx, y)
            # 3) (x, y) -> (x, y+1) -> (x+dx, y+1)
        
        # 위 3가지 중 가는 길에 벽이 있으면 온도 상승 X
            # 벽 정보로 사용해서 (x, y)가 벽 정보 배열에 있으면, 
            # (x-1, y)거나 (x, y+1)인 벽에 대하여 (이건 t값 보고 결정) 해당 방향으로 못가도록 하기 

    # 탐색 되어서 온도 상승한 칸은 방문 처리 후, 큐에 넣음 (방문 처리는 += 1로 하기) + 부모 방문 배열이 5 이상이면 이제 자식은 큐에 추가X
        # 온도 상승은 그냥 원래 배열의 값 += 상승할 값 
        # 상승할 값은 5에서 1로 점점 줄어 듦 (이건 부모 방문 배열 활용: 5 - 부모의 방문 배열) 

# 2. 온도가 조절됨 - control_temp() 함수
    # 모든 인접 칸에 대해서 (상하좌우) 
        # 온도가 높은 칸 -> 낮은 칸으로 (두칸의온도차) / 4 만큼 조절 됨
        # 1) 원래 배열을 사용하여, 각 인접 칸에 대하여 차이를 구한 후 더하거나 뺄 값을 tmp 배열에 저장
            # 두 칸 중 작은 칸 좌표에 += 차이, 큰 칸 좌표에 -= 차이
        # 2) 원래 arr 값에 tmp 값을 더해서 리턴
        # ** 근데 두칸 사이에 벽이 있으면 온도 조절X
        
# 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    # 그냥 메인에서 반복문으로 가장 자리에 대해 1씩 감소
# 4. 초콜릿을 하나 먹는다. (그냥 카운트)
# 5. (종료 조건) 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.

from collections import deque
R, C, K = map(int, input().split())
arr = []
wall = []
hot = [] # 온풍기 배열
exam = [] # 조사할 칸 배열
dx = [0, 0, 0, -1, 1] # 0번, 오, 왼, 위, 아래
dy = [0, 1, -1, 0, 0]

for _ in range(R) : arr.append(list(map(int, input().split())))
W = int(input())
# 벽 입력과 동시에 값 수정 해주고 wall에 추가 - 시간 초과 나면 이거 set으로 바꾸기
for _ in range(W) : 
    x, y, t = map(int, input().split())
    if t == 0 : 
        wall.append([x-1, y-1, x-2, y-1]) # 두 칸 사이니까 순서 상관 없으니까 2개 다 만들기
        wall.append([x-2, y-1, x-1, y-1])
    else : 
        wall.append([x-1, y-1, x-1, y])
        wall.append([x-1, y, x-1, y-1])

for i in range(R) : 
    for j in range(C) :
        if 0 < arr[i][j] < 5 : 
            hot.append([i, j, arr[i][j]]) # 온풍기 배열에 좌표, 방향 저장
            arr[i][j] = 0
        elif arr[i][j] == 5 : 
            exam.append([i, j])
            arr[i][j] = 0

def increase_temp(x, y, i) : # 온풍기 하나로 온도 상승 - bfs 함수
    # 방향 : dx[i], dy[i]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    
    que = deque()
    que.append((x, y))
    while que : 
        x, y = que.popleft()
        if visited[x][y] >= 5 : continue
        if i < 3 : # 방향 오, 왼
            nx, ny = x-1, y+dy[i] # 1
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and visited[x][y] != 0: 
                if [x, y, x-1, y] not in wall and [x-1, y, nx, ny] not in wall :
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
            nx, ny = x, y+dy[i] # 2
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]: 
                if [x, y, nx, ny] not in wall : 
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
            nx, ny = x+1, y+dy[i] # 3
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and visited[x][y] != 0: 
                if [x, y, x+1, y] not in wall and [x+1, y, nx, ny] not in wall :
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
        else : # 방향 위, 아래
            nx, ny = x+dx[i], y-1 # 1
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and visited[x][y] != 0: 
                if [x, y, x, y-1] not in wall and [x, y-1, nx, ny] not in wall :
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
            nx, ny = x+dx[i], y # 2
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]: 
                if [x, y, nx, ny] not in wall : 
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
            nx, ny = x+dx[i], y+1 # 3
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and visited[x][y] != 0: 
                if [x, y, x, y+1] not in wall and [x, y+1, nx, ny] not in wall :
                    que.append((nx, ny))
                    arr[nx][ny] += 5 - visited[x][y]
                    visited[nx][ny] = visited[x][y] + 1
            
    return arr

def control_temp(): # 아오 이거 어려워 
    
    tmp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R) :
        for j in range(C) :
            x, y = i, j
            for k in range(1, 5) : # 상하좌우
                nx, ny = x + dx[k], y + dy[k]
                if 0<= nx < R and 0<= ny <C : 
                    if [x, y, nx, ny] not in wall : # 사이에 벽이 없을 때
                        diff = abs(arr[nx][ny]-arr[x][y]) // 4
                        if arr[nx][ny] < arr[x][y] :
                            tmp[nx][ny] += diff
                            tmp[x][y] -= diff
                        else : 
                            tmp[nx][ny] -= diff
                            tmp[x][y] += diff
    
    for i in range(R) :
        for j in range(C) :
            arr[i][j] += tmp[i][j] // 2 # 틀리면 이거 문제다 
                            
    return arr 

def exit_condition() :
    # (종료 조건) 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사
    for x, y in exam: 
        if arr[x][y] < K : 
            return False
        
    return True

##### main #####
choco = 0 
while exit_condition() == False : 
    for info in hot : 
        x, y, d = info
        arr = increase_temp(x, y, d)
    
    arr = control_temp()

    for i in range(R) :
        for j in range(C) :
            if i == 0 or i == R-1 or j == 0 or j == C-1 :
                if arr[i][j] > 0 : arr[i][j] -= 1
                    
    choco += 1
    if choco > 100 : 
        choco = 101
        break
    
print(choco)