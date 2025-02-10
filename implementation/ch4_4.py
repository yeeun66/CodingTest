# 이것이 코딩테스트다 책 - Ch4 구현 예제 03번) 게임 개발
# 시뮬레이션 - 삼성 로봇청소기 문제랑 거의 유사

# 방법: 
# 1. 입력 받기 (N, M, 현재 위치, 방향(4가지), 맵 정보(0은 육지, 1은 바다))
# 2. 현재 방향 기준으로 반시계로 90도 회전 (동 -> 북 -> 서 -> 남 -> 동 -> ..)
# 3. 회전 한 후 한 칸 앞으로 간 칸이 0이면 캐릭터의 방향도 해당 방향으로 바꾼 후, 그 칸으로 한칸 전진한다. 이후 그 칸은 1로 바꾼다
#    칸이 0이 아니라면 (즉, 바다이거나 이미 방문) 한번 더 90도 회전한다
# 4. 4번 모두 회전 후에도 갈 곳이 없다면 해당 방향 유지한 채로 한칸 뒤로 가고 1단계로 돌아간다. 이 때 한칸 뒤로 갔을 때 칸이 바다 (=1)라면 반복문 종료

# 탐색
# 초기 설정, 처음 캐릭터 위치의 값을 방문(=-1)으로 바꾸고, 처음 방향을 direct 변수에 저장한다
# 해당 위치의 좌표부터 반복 시작한다. (후진 할 때 바다인 경우 반복 종료)
# 방향 반시계 90도로 4번 돌리면서 다음을 반복
    # 방향 바꾼 후 앞 칸이 값이 0 이라면 현재 캐릭터 위치를 거기로 업데이트 한 후, 방향도 업데이트 한 후 for 문에서 나가고 현재 위치를 사용해 다시 while문 수행
    # 앞 칸이 0이 아니라면 방향을 바꿔서 다시 수행
# 4번 모두 회전 후에도 갈 곳이 없다면 원래 방향에서 한칸 뒤로 간 후 다시 while문 수행
# 반복 끝난 후 방문한 칸의 수 (=-1) 출력

N, M  = map(int, input().split())
cx, cy, cdir = map(int, input().split())

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

arr = []
for _ in range(N) :
    arr.append(list(map(int, input().split())))

while True :
    rotate = 0
    arr[cx][cy] = -1
    for i in range(4) :
        cdir = (cdir + 3) % 4
        nx = cx + dx[cdir]
        ny = cy + dy[cdir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or arr[nx][ny] != 0 : continue

        cx, cy = nx, ny
        rotate = 1
        break

    if rotate == 0 : # 후진 해야하는 경우
        tmp_dir = (cdir + 2) % 4
        nx = cx + dx[tmp_dir]
        ny = cy + dy[tmp_dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or arr[nx][ny] == 1 : break # 범위 벗어나거나 바다면

        cx, cy = nx, ny

cnt = 0
for i in range(N) :
    cnt += arr[i].count(-1)

print(cnt)