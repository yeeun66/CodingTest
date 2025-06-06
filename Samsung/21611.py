# 마법사 상어와 블리자드
# 4시간 걸림
from itertools import repeat

# 0. 구슬 정보 입력 받기, 필요한 배열 초기화
    # 색 정보 (1,2,3)
    # 번호 정보 (좌하우상 순으로 반복하며 해당 칸의 번호 만들기, 근데 이제 1 1 2 2 3 3 4 4 ... 이런식으로 증가)
        # 이거 배열 보다는 이 흐름으로 흘러가는 함수 만들어두기
# 아래 1-4번을 M번 반복
# 1. 블리자드 마법 시전
    # 마법 시전 횟수(M) 마다 d(방향)와 s(거리)가 주어짐
    # 상어(가장 가운데)는 d방향으로 s만큼 떨어진 거리의 구슬 다 파괴 -> -1로 만듦
# 2. 구슬의 이동 (구슬 이동 없을때까지 반복) <- 이거 구현 잘해야 함
    # 원래 flow 흐름을 따라갈건데, 새로운 배열 new 에 color 값을 더해주는 식으로 갈거임
    # num_arr에 -1이 제거된 순서로 저장 되어 있으므로 이 순서로 그냥 다시 차곡차곡 넣어주면 됨
    # pop하면 오래걸리니까 그냥 있는 갯수만큼 넣어주기
# 3. 구슬 폭발
    # 4개 이상 연속되는 구슬 있을시 모두 -1로 만들기
        # 폭발한 구슬의 갯수는 각 색깔별로 저장해두기 -> count_ball[1~3]
    # 이후 2번 (구슬 이동) 진행
    # 아래를 더이상 폭발할 구슬이 없을 때 까지 반복 - delete_ball()
        # 또 같은 flow 로 1번칸 부터 탐색
        # 다른 색 만날때까지 임시 배열에 좌표 저장
        # 다른 색 만났을 때, 이전 색의 배열 길이가 4이상이면
        # 해당 좌표에 해당하는 color 칸을 모두 -1로 바꿈 -> 그리고 count_ball[1~3]에 += 배열 길이
        # flag = True로 바꿈
# 4. 구슬의 변화
    # 연속하는 같은 색 구슬은 같은 그룹 (1개인 그룹도 가능) - change_ball()
        # 아까 delete_ball()에서 -1 매달았던 것 처럼, 같은 색이면 계속 group 에 저장하고,
            # 다른 색 만났을 때, 배열 ab에 새로 만들어진 A와 B를 순서대로 저장함
            # A: 그룹 구성원수, B: 해당 그룹 색깔 번호
        # 최종 완성된 배열 ab를 새로운 배열 new에 플로우 순서대로 넣어주고, new 리턴
# 5. 출력
    # 1×(폭발한 1번 구슬의 개수) + 2×(폭발한 2번 구슬의 개수) + 3×(폭발한 3번 구슬의 개수)

from collections import deque
N, M = map(int, input().split())
color = []
magic = [] # 마법 시전시 필요한 d와 s 저장
for _ in range(N) : color.append(list(map(int, input().split())))
for _ in range(M) : magic.append(list(map(int, input().split())))

arr = [[0 for _ in range(N)] for _ in range(N)]
cent_r, cent_c = (N+1) // 2 -1, (N+1) // 2 -1
dx = [0, 1, 0, -1] # 좌 하 우 상
dy = [-1, 0, 1, 0]
mdx = [-1, 1, 0, 0] # 마법 시전용 방향 (0상하좌우)
mdy = [0, 0, -1, 1]


def flow(): # 1번칸 ~ N-1번칸 만드는 흐름 [완벽한 플로우] <- 이거 계속 활용함
    repeat = 1 # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0 # 현재 방향
    nx, ny = cent_r, cent_c # 시작 위치 가운데
    i = 1
    while i < N ** 2 :
        for _ in range(repeat) :
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            arr[nx][ny] = i
            i += 1
            if i >= N ** 2 : break
        if cur_dir == 1 or cur_dir == 3: repeat += 1 # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir =  (cur_dir + 1) % 4

def pick_color(): # 1번칸 ~ N-1번칸 만드는 흐름 -> 구슬 번호 값을 하나씩 꺼내오는 용도로 사용
    # 그냥 여기서 큐에 1번부터 N-1번까지의 구슬 번호를 모두 담아서 리턴
    que = deque()
    repeat = 1 # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0 # 현재 방향
    nx, ny = cent_r, cent_c # 시작 위치 가운데
    i = 1
    while i < N ** 2 :
        for _ in range(repeat) :
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            if color[nx][ny] > 0 : que.append(color[nx][ny]) # 0보다 큰 값만 추가
            i += 1
            if i >= N ** 2 : break
        if cur_dir == 1 or cur_dir == 3: repeat += 1 # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir =  (cur_dir + 1) % 4
    que = list(que)
    return que

def do_magic(idx) :
    d, s = magic[idx][0]-1, magic[idx][1]

    nx, ny = cent_r, cent_c
    for _ in range(s) : # 여기 경계 처리 해야하나..?
        nx += mdx[d]
        ny += mdy[d]
        color[nx][ny] = -1  # 구슬 파괴

    return color

def move_ball() :
    new = [[0 for _ in range(N)] for _ in range(N)]

    num_arr = pick_color() # 구슬 번호 값 순서대로 받아옴

    repeat = 1  # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0  # 현재 방향
    nx, ny = cent_r, cent_c  # 시작 위치 가운데
    i = 0
    while i < len(num_arr):
        for _ in range(repeat):
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            new[nx][ny] = num_arr[i]
            i += 1
            if i >= len(num_arr): break
        if cur_dir == 1 or cur_dir == 3: repeat += 1  # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir = (cur_dir + 1) % 4

    return new

count_ball = [0] * 4
def delete_ball() :
    flag = False # 한번도 폭발한게 없다면 폭발 멈추게끔 하는 것도 여기서

    repeat = 1  # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0  # 현재 방향
    nx, ny = cent_r, cent_c  # 시작 위치 가운데
    i = 1
    temp = []
    cur_num = color[cent_r][cent_c-1] # 현재 구슬 번호 (1~3)
    while i < N ** 2:
        for _ in range(repeat):
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            if color[nx][ny] == cur_num : temp.append((nx, ny))
            else :
                if len(temp) >= 4 :
                    for a, b in temp : color[a][b] = -1
                    count_ball[cur_num] += len(temp) # 폭발한 수
                    flag = True
                # 다시 temp 초기화
                temp = [(nx, ny)]
                cur_num = color[nx][ny]

            i += 1
            if i >= N ** 2: break
        if cur_dir == 1 or cur_dir == 3: repeat += 1  # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir = (cur_dir + 1) % 4

    return flag

def change_ball() :
    repeat = 1  # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0  # 현재 방향
    nx, ny = cent_r, cent_c  # 시작 위치 가운데
    i = 1
    ab = []
    group = []
    cur_num = color[cent_r][cent_c - 1]  # 현재 구슬 번호 (1~3)
    while i < N ** 2: # 1) 새로운 구슬 두개씩 저장해놓기 (그냥 여기서 부터 N**2 개 넘으면 컷)
        for _ in range(repeat):
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            if color[nx][ny] == cur_num:
                group.append((nx, ny))
            else:
                a, b = len(group), cur_num
                ab.append(a)
                if len(ab) >= N ** 2 -1 : break
                ab.append(b)
                if len(ab) >= N ** 2 -1: break
                # 다시 temp 초기화
                group = [(nx, ny)]
                cur_num = color[nx][ny]

            i += 1
            if i >= N ** 2: break
        if len(ab) >= N ** 2 -1: break
        if cur_dir == 1 or cur_dir == 3: repeat += 1  # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir = (cur_dir + 1) % 4

    # 2) 이제 ab를 새로운 배열에 차곡차곡 넣기
    # ** 주의) 만약, 구슬이 칸의 수보다 많아 칸에 들어가지 못하는 경우 그러한 구슬은 사라진다.
    new = [[0 for _ in range(N)] for _ in range(N)]

    repeat = 1  # 현재 반복 횟수 # 좌하 / 우상 <- 즉 하에서 우로 갈때, 상에서 좌로 갈 때 반복값 하나씩 증가

    cur_dir = 0  # 현재 방향
    nx, ny = cent_r, cent_c  # 시작 위치 가운데
    i = 0
    while i < len(ab):
        for _ in range(repeat):
            nx += dx[cur_dir]
            ny += dy[cur_dir]
            new[nx][ny] = ab[i]
            i += 1
            if i >= N**2 or i >= len(ab): break
        if cur_dir == 1 or cur_dir == 3: repeat += 1  # 현재 하를 끝냈거나, 상을 끝냈을 때
        cur_dir = (cur_dir + 1) % 4

    return new

### Main ###
for m in range(M) :

    color = do_magic(m) # 1. 블리자드 마법 시전
    color = move_ball() # 2. 구슬의 이동

    flag = True
    while flag : # 더이상 폭발할 구슬이 없을 때 까지 반복 (flag == True 이면 계속 진행)
        flag = delete_ball() # 3. 구슬 폭발
        color = move_ball() # 3-1. (2. 구슬 이동) 진행

    color = change_ball() # 4. 구슬의 변화

print(count_ball[1]+2*count_ball[2]+3*count_ball[3])