# 코드트리 - 왕실의 기사 대결
# 5시간 30분 걸림
# 처음 3시간은 로직 잘못 짜서 디버깅 하다가 로직 오류 발견하고 로직 다 갈아엎음 - 1번 로직
# 이후에는 로직 잘 짜놔서 금방 해결함

"""
로직
0. 입력 받기
    - L(체스판 크기), N(초기 기사들 정보), Q(명령)
    - 체스판 정보(0 빈칸, 1 함정, 2 벽)
    - 초기 기사들 정보 r, c, h, w, k (초기체력 k) - knight 배열에 저장 (3번을 위해 knight_origin에도 복사 해두기)
    - 명령 정보 (i, d) i번 기사에게 d 방향으로 한칸 이동 (i가 이미 사라진 기사 일수도 있음) (d는 상우하좌)

    - 함정 위치 좌표로 파악
        - 현재 체스판에서 값이 1인 좌표들 모두 set인 hamjeong에 넣기
    - 벽 값 (2)는 -1로 교체

    - 체스판에 기사들 두기 (1번~ N번)

아래 1, 2를  Q번 반복
1. 기사 이동 - move_knight(i, d)    - 이동 완료한 arr과 knight_idx 리턴
    - 현재 존재하는 기사인지 판단 : 초기체력 -1이면 컨티뉴

    - 시작 하는 기사의 모든 영역에 대해서 d 방향으로 인접한 모든 기사 번호를 찾는다 -> que에 넣어둠
    - 시작 기사, que에 들어간 기사 모두 방문 처리
    - 이동 가능한지 여부 판단 (que empty까지 반복)
	- que에서 pop한 좌표로 부터 bfs 탐색 시작
		- 현재 번호에 대해서, 각각 자신의 영역 모두 찾는다 (좌상단 좌표부터)
			- 찾은 모든 좌표에 대해서 d 방향으로 한칸씩 이동 가능한지 본다
			- 이동 불가면(-1이거나 경계 벗어나면), return False
			- 이동 가능이면 (0이면 그냥 계속), (다른 기사이면), 그 기사 번호도 큐에 넣고 방문 처리
				return True, other
				- other은 다른 기사들 들어있을 수도 있는 큐라서 리턴 후 que에 추가(extend) 해줌

    - 이동 가능하다면, 모든 기사 이동 시킴
        - visited에서 방문처리 되어있는 모든 기사 번호에 대해서
        	- d 방향으로 이동 시킨 후 배열 업데이트
        - 이때 i번 기사가 아닌, 다른 기사들 중 이동된 기사들의 번호 저장 - knight_idx
    - 이동 완료한 arr과 knight_idx 리턴


2. 대결 대미지 - give_damage()
     - knight_idx 에 있는 기사들에 대하여,
        - 기사들의 위치에 함정(1)이 있다면, 있는 만큼 체력(k) 1씩 감소
    - 이때, 기사들 중 k <= 0 이 되면 사라짐
        - 체스판에서 모든 좌표 0으로 만들고, k = -1로 업데이트
    - 그리고 knight 배열에 현재 남은 기사들의 좌상단 정보도 업데이트 (r, c)

3. 최종 출력
    - 생존한 기사들에 대해서 (원래 체력 - 현재 체력)의 합 출력
"""

from collections import deque

dx = [-1, 0, 1, 0]  # 상 우 하 좌
dy = [0, 1, 0, -1]

L, N, Q = map(int, input().split())
arr = []  # 체스판
knight = []  # 기사들 정보
cmd = []  # 명령 정보
ham = set()  # 함정 좌표들
for _ in range(L): arr.append(list(map(int, input().split())))
for _ in range(N): knight.append(list(map(int, input().split())))
for n in range(N):
    knight[n][0] -= 1 # 0~N-1 좌표로 사용할거니까
    knight[n][1] -= 1

knight_origin = [k[:] for k in knight]

for _ in range(Q): cmd.append(list(map(int, input().split())))

# 0. 체스판 조작
for i in range(L):
    for j in range(L):
        if arr[i][j] == 1:
            ham.add((i, j))
            arr[i][j] = 0
        if arr[i][j] == 2: arr[i][j] = -1

idx = 1
for r, c, h, w, _ in knight:
    for i in range(r, r + h):
        for j in range(c, c + w):
            arr[i][j] = idx
    idx += 1

def bfs(x, y, d):
    visited = [[0 for _ in range(L)] for _ in range(L)]

    tmp = []  # 다른 기사들 담아갈 배열
    que = deque()
    que.append((x, y))
    visited[x][y] = 1
    cur_poss = [] # 같은 기사들 좌표 모두 저장
    cur_poss.append((x, y))
    cur_num = arr[x][y]
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and not visited[nx][ny]:
                if arr[nx][ny] == cur_num:
                    que.append((nx, ny))
                    visited[nx][ny] = 1
                    cur_poss.append((nx, ny))

    for x, y in cur_poss: # 같은 기사들에 대해 모두 d방향으로 옮겨본 후 조건 적용
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= L or ny < 0 or ny >= L: return False, [] # 이동 불가 (경계 나감)
        if arr[nx][ny] == -1: return False, [] # 이동 불가 (벽 만남)
        if arr[nx][ny] != arr[x][y] and arr[nx][ny] > 0: tmp.append(arr[nx][ny])

    return True, tmp # 이동 가능 (인접 기사들 데리고 나감)


def move_knight(cmds):
    new_arr = [a[:] for a in arr]
    num, d = cmds
    _, _, h, w, k = knight[num - 1]
    if k == -1: return new_arr, []  # 존재 하지 않는 기사
    knight_idx = []  # 이동 가능하다면 움질일 기사들 저장
    que = deque()
    visited = [0] * (N + 1)

    for i in range(L):
        for j in range(L):
            if arr[i][j] == num:
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < L and 0 <= ny < L:
                    if arr[nx][ny] == -1: return new_arr, [] # 가려고 하는데 벽있으면 그냥 리턴
                    if arr[nx][ny] != num and arr[nx][ny] > 0 and not visited[arr[nx][ny]]:
                        que.append(arr[nx][ny]) # 처음 기사와 d 방향으로 인접한 기사 추가
                        visited[arr[nx][ny]] = 1
                else:
                    return new_arr, []
    while que: # 인접한 기사들에 대해서 이동 여부 탐색
        cur_num = que.popleft()
        knight_idx.append(cur_num)
        x, y = knight[cur_num - 1][0], knight[cur_num - 1][1] # 해당 기사의 좌상단 좌표
        possible, tmp = bfs(x, y, d) # 이동 가능 여부 받아옴
        if not possible: return new_arr, []
        if tmp: que.extend(tmp) # 이동 가능할 때, 인접 다른 기사도 있으면 que에 추가

    # 여기까지 왔으면 이동 가능한 것
    knight_idx.append(num)
    for num in knight_idx:
        for x in range(L):
            for y in range(L):
                if arr[x][y] == num:
                    new_arr[x][y] = 0 # 원래 자리는 초기화

    for num in knight_idx:
        for x in range(L):
            for y in range(L):
                if arr[x][y] == num:
                    nx = x + dx[d]
                    ny = y + dy[d]
                    new_arr[nx][ny] = num  # 이동

    # knight 배열에 현재 남은 기사들의 좌상단 정보도 업데이트 (r, c)
    for num in knight_idx:
        update = False
        for i in range(L):
            for j in range(L):
                if new_arr[i][j] == num:
                    knight[num - 1][0], knight[num - 1][1] = i, j
                    update = True
                    break
            if update: break

    knight_idx.pop() # 가장 끝에 넣었던 현재 기사는 2번 수행시 체력 소모하면 안되므로 pop
    return new_arr, knight_idx

def give_damage(knight_num):
    for i in range(L):
        for j in range(L):
            if arr[i][j] in knight_num: # 이동당한 기사들에 대해
                if (i, j) in ham:
                    knight[arr[i][j] - 1][4] -= 1  # 함정 있으면 체력 감소

    dead_num = []
    for num in knight_num:
        if knight[num - 1][4] <= 0:
            dead_num.append(num)
            knight[num - 1][4] = -1

    for i in range(L):
        for j in range(L):
            if arr[i][j] in dead_num: arr[i][j] = 0 # 체스판에서 지우기

    # - 그리고 knight 배열에 현재 남은 기사들의 좌상단 정보도 업데이트 (r, c)
    for num in dead_num: knight[num - 1][0], knight[num - 1][1] = -1, -1

    return knight

for q in range(Q):
    arr, knight_idx = move_knight(cmd[q])  # 1. 기사 이동
    if knight_idx:
        knight = give_damage(knight_idx)  # 2. 대결 데미지

# 3. 생존한 기사들에 대해서 (원래 체력 - 현재 체력)의 합 출력
result = 0
for i in range(N):
    if knight[i][4] != -1:
        result += knight_origin[i][4] - knight[i][4]
print(result)