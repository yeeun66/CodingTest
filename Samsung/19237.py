# 어른 상어

# priorities : 미리 정해진 방향정보를 저장할 리스트
# smell : 현재 시간에 냄새의 상황을 보여주는 리스트
# data : 상어의 현재 위치를 나타내는 리스트

# 큰 로직
    # 1. 냄새 정보 먼저 업데이트 update_smell()
    # 2. 상어들 이동 move()
    # 3. 종료 조건 - 메인에서 2가지 체크

# 세부로직
    # update_smell():
        # 냄새가 남아있는 경우, 1줄여
        # 상어가 존재하는 위치면, 냄새를 k로 업데이트
    # move():
        # 상어가 있는 위치에서
            # 냄새 안나는 곳 발견 -> 이동
            # 냄새 안나는 곳이 없으면 -> 자신에게 이동
            # 이 때, 이동 시 우선순위 고려

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, k = map(int, input().split())

# 처음상어 위치
data = []
for _ in range(n): data.append(list(map(int, input().split())))

# 상어의 초기 방향
directions = list(map(int, input().split()))

# 상어의 방향별 우선순위 (상 하 좌 우)
priorities = []
for i in range(m):
    temp = []
    for _ in range(4):
        temp.append(list(map(int, input().split()))) # 4방향 다 각 리스트로 temp에 넣고
    priorities.append(temp) # temp를 리스트에 추가해줌

# 현재 냄새 상황 (특정 냄새의 상어 번호, 특정 냄새의 남은 시간)
smell = [[[0, 0]] * n for _ in range(n)]

# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남아있는 경우
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 위치의 경우
            if data[i][j] != 0: # 현재 상어가 존재하는 위치는 무조건 k초 남아있으니까
                smell[i][j] = [data[i][j], k]

# 상어 이동
def move():
    new_data = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if data[x][y] != 0: # 현재 위치에 상어가 있으면
                direction = directions[data[x][y] - 1] # 상어 초기 방향
                found = False

                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 나지 않는 곳이라면
                            directions[data[x][y] - 1] = idx # 방향 바꾸고
                            # 상어 이동시키기
                            if new_data[nx][ny] == 0:
                                new_data[nx][ny] = data[x][y]
                            else :
                                new_data[nx][ny] = min(data[x][y], new_data[nx][ny])
                            found = True
                            break
                if found:
                    continue

                # 주변에 모두 냄새가 남아있다면, 자신의 냄새가 있는 곳으로 이동
                for idx in priorities[data[x][y] - 1][direction - 1]:
                    nx = x + dx[idx - 1]
                    ny = y + dy[idx - 1]
                    if 0 <= nx < n and 0 <= ny < n:
                        if smell[nx][ny][0] == data[x][y]: # 자신의 냄새가 있는 곳이라면
                            # 해당 상어 방향 변경
                            directions[data[x][y] - 1] = idx
                            # 상어 이동시키기
                            new_data[nx][ny] = data[x][y]
                            break
    return new_data

answer = 0
while True:
    update_smell() # 냄새 정보 먼저 업데이트
    new_data = move() # 상어 이동
    data = new_data
    answer += 1

    check = True
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                check = False
    if check:
        print(answer)
        break

    if answer >= 1000:
        print(-1)
        break