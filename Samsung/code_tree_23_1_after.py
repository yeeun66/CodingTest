# 코드트리 - 메이즈러너
# 도움 받아서 4시간 걸림 ...
"""
로직
0. 입력 받기 & 사용할 배열
    - 게임판 배열 arr
    - 참가자 각각의 좌표 배열 participants
    - 출구 위치 ex, ey
        - 게임판 배열에 출구 위치 -1로 표시해두기
    - 탈출한 참가자 번호 인덱스 set - exit_part

1. 모든 참가자 이동
    - 아직 탈출 안한 참가자들에 대해, 상하좌우로 움직임
    1) 각 참가자 당 상하좌우로 한 칸 갔을 때와 출구와의 거리 계산해서 가장 짧은 거리인 칸 선택
        (거리는 절댓값 차 + 절대값 차)
        이 때 현재 위치보다 당연히 거리가 작아야 함
    2) 선택된 칸이 없거나, 선택된 칸이 벽이라면 (>0) -> 이동X
        else :
            - 바뀐 좌표로 업데이트
            - result += 이동한 거리

    3) 참가자의 좌표와 현재 출구 위치가 같다면 탈출
        - exit_part에 탈출한 참가자 인덱스 번호 add

2. 가장 작은 정사각형 잡기
    - i = 0 ~ N-1까지 한변의 길이가 1인 사각형 부터 모든 정사각형을 탐색
    - 이때 탐색한 사각형이 사람한명(이상)과 출구위치를 포함한다면, 사각형의 좌상단 좌표와 한변의 길이 리턴

3. 정사각형 90도 회전
    - 2에서 리턴 받은 정사각형 좌상단 좌표와 한변의 길이를 사용해 이중 for문으로 90도 회전
    - 근데 여기서 사람도 회전시켜야 함
        - 회전 하려는 좌표에 사람이 있다면, 사람 좌표도 회전시킨걸로 업데이트
    - 회전 후 정사각형 내에 있는 벽은 내구도 1씩 감소 (0보다 큰값이면 모두 1감소)
    - 원래 배열에 이 정사각형을 덮어서 최종 배열 리턴해줌

    - 사람 회전 용으로도 배열 만들어두기 person = []

4. 종료조건 k >= 8 이거나 exit_part >= M

5. result와 출구 좌표 출력
"""

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M, K = map(int, input().split())
arr = []
for _ in range(N) : arr.append(list(map(int, input().split())))
participants = []
for _ in range(M) : participants.append(list(map(int, input().split())))
for m in range(M) :
    x, y = participants[m]
    participants[m] = [x-1, y-1]
ex, ey = map(int, input().split())
ex, ey = ex-1, ey-1
arr[ex][ey] = -1 # 출구
exit_part = set()
results = 0

def move_part(result):

    for m in range(M) :
        x, y = participants[m]
        if m in exit_part : continue

        # 1) 각 참가자 당 상하좌우로 한 칸 갔을 때와 출구와의 거리 계산해서 가장 짧은 거리인 칸 선택
        min_dist = abs(ex-x) + abs(ey-y)
        cx, cy = x, y # 업데이트 된 칸
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            # 이것도!! 처음부터 벽이 아닌 것만 거리 체크 해야됨
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] <= 0:
                tmp_dist = abs(ex-nx) + abs(ey-ny)
                if tmp_dist < min_dist :
                    min_dist = tmp_dist
                    cx, cy = nx, ny # 가장 짧은 칸으로 업데이트

        # 2) 선택된 칸이 없으면 이동X
        if (cx, cy) == (x, y) : continue
        # 아니면
        participants[m] = [cx, cy]
        result += 1

        # 3) 이동한 좌표와 현재 출구 위치가 같다면 탈출
        if (cx, cy) == (ex, ey) :
            exit_part.add(m)
            participants[m] = [-1, -1]

    return participants, result, exit_part

def make_rect():
    for cur_len in range(1, N+1):
        for i in range(N - cur_len + 1):
            for j in range(N - cur_len + 1):
                cond1, cond2 = False, False
                for a in range(i, i + cur_len):
                    for b in range(j, j + cur_len):
                        if (a, b) == (ex, ey): cond1 = True
                        if [a, b] in participants: cond2 = True
                if cond1 and cond2:
                    return cur_len, i, j
    return N, 0, 0  # fallback


def rotate_90(L, x, y):
    global ex, ey
    new_arr = [a[:] for a in arr]
    rect = [[0] * L for _ in range(L)]

    # 1. 사각형 복사 및 내구도 감소
    for i in range(L):
        for j in range(L):
            ax, ay = x + i, y + j
            val = arr[ax][ay]
            if val > 0: val -= 1
            rect[i][j] = val

    # 2. 회전된 배열 생성
    new_rect = [[0] * L for _ in range(L)]
    for i in range(L):
        for j in range(L):
            new_rect[j][L - 1 - i] = rect[i][j] # 공식 이건 암기 필요

    # 3. 참가자 회전
    for idx in range(M):
        px, py = participants[idx]
        if [px, py] == [-1, -1]:
            continue
        if x <= px < x + L and y <= py < y + L: # 혹시 모를 케이스를 위해 경계 체크 진행
            rx, ry = px - x, py - y # 좌상단 좌표를 빼서 상대 좌표로 변환
            nrx, nry = ry, L - 1 - rx # 공식 적용 (새로운 행에는 이전열, 새로운 열에는 L-1-이전행)
            participants[idx] = [x + nrx, y + nry] # 좌상단 좌표를 다시 더해서 원래 위치로 변환

    # 4. 출구 회전
    if x <= ex < x + L and y <= ey < y + L:
        rx, ry = ex - x, ey - y
        nrx, nry = ry, L - 1 - rx
        ex, ey = x + nrx, y + nry

    # 5. 회전된 사각형 원본 배열에 덮기
    for i in range(L):
        for j in range(L):
            ax, ay = x + i, y + j
            new_arr[ax][ay] = new_rect[i][j]

    # 6. 출구 표시
    new_arr[ex][ey] = -1
    return new_arr, participants, ex, ey

###### Main ######
for k in range(K) :

    participants, results, exit_part = move_part(results) # 1. 참가자 이동
    if len(exit_part) >= M: break
    length, lx, ly = make_rect() # 2. 작은 정사각형 잡기
    arr, participants, ex, ey = rotate_90(length, lx, ly) # 3. 정사각형 90도 회전

print(results)
print(ex+1, ey+1)