# 25년 상반기 오전 01번 - 코드트리) 민트초코 우유
# 2시간 50분 만에 품
# 처음에 틀렸을 때는 초기화 문제 -> 초기화 제대로 하니까 바로 맞음

# F: 신봉 음식 T, C, M
# B: 신앙심

# 1. 각 학생의 F와 B 입력 받기
# --- 아래를 T번 반복
# 2. 아침: 모든 B에 대해 값(신앙심) += 1
# 3. 점심: 같은 F에 대하여 그룹 형성 >> 반복문 - 방문처리 -BFS
    # 3-2. 모든 그룹에 대해 대표자 선정 (대표자는 따로 배열에 i,j, 1 보관) - represent = [] <- 세번째 값은 오늘 전파 가능한지 아닌지 판별 용도
        # B가 가장 큰 사람 > 행이 가장 작은 사람 > 열이 가장 작은 사람
    # 3-3. 대표자 신앙심 += (구성원 수 -1)
        # 나머지 신앙심 -= 1
# 4. 저녁: 모든 그룹 대표자들이 신앙 전파
    # 4-1. 전파 순서) (T, C, M) -> (TC, TM, CM) -> (TCM) 신봉음식 길이 작은 순
        # 각 그룹 내에서 우선순위) 대표자의 B(신앙심) > 대표자의 행번호 작은순 > 열번호 작은순
    # 4-2. 간절함, 방향
        # 전파자는 간절함 x = B-1로 바꿔 전파에 사용
        # 전파 방향 = B % 4 (0~3, 상하좌우)
        # (전파자 신앙심 = 1만 남김)
    # 4-3. 전파 시작
        # 한칸씩 이동하면서 전파 (격자 밖이거나 x==0이면 전파 종료)
        # 전파 대상이 전파자와 같은 음식이면 무시
        # 다른 음식인 경우, x > y 이면 강한 전파
            # 전파 대상의 F는 전파자의 F와 같아짐
            # x -= (y+1), y += 1
                # 이 때 x==0이면 전파 종료
        # x <= y 이면 약한 전파
            # 전파대상의 F는 전파자의 기본음식과 합쳐진 음식이 됨
            # x = 0, 더이상 전파 안함. y += x
        # 전파 당한 학생은 당일에 전파 못함
# 5. 각 날의 신앙심 총합 출력  (TCM-TC-TM-CM-M-C-T 순으로)

from collections import deque
N, T = map(int, input().split())
F = []
B = []
for _ in range(N) : F.append(list(map(str, input().strip())))
for _ in range(N) : B.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    # 같은 그룹을 group에 모두 append [B값, i, j]
    # 이후 큐 엠티이면 group에서 B값은 크고 i, j는 작은 순으로 솔팅 (이때 B를 음수로 바꾸고 솔팅하면됨)
    # 가장 첫번째 값이 대표 학생이됨
    # 대표 학생에게 신앙심 몰아주는 작업 후,
    # 대표 학생 좌표 리턴
    cur = F[x][y]
    que = deque()
    group = []
    que.append((x, y))
    group.append([B[x][y], x, y])
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and F[nx][ny] == cur:
                visited[nx][ny] = 1
                group.append([B[nx][ny], nx, ny])
                que.append((nx, ny))

    for i in range(len(group)) : group[i][0] = -group[i][0]
    group = sorted(group)

    for i in range(len(group)):
        x, y = group[i][1], group[i][2]
        if i == 0 : B[x][y] += len(group) -1
        else : B[x][y] -= 1

    x1, y1 = group[0][1], group[0][2]
    return x1, y1, visited

def sum_food(string) : # 이것도 시험장이랑 다르게 하긴 함 
    # CMT, CM, CT, MT, C, M, T 중 하나로 만들어짐
    new = list(string)
    new = set(new)
    new = list(new)
    new = sorted(new)
    new = ''.join(map(str, new))

    return new

for t in range(T) :
    represent = [] # 문제의 부분 !!!!!!!! 이걸 밖에서 처음 한번만 초기화 해서 두번째 턴부터 망한거 였음..

    # 아침
    for i in range(N) :
        for j in range(N) :
            B[i][j] += 1

    # 점심
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            if not visited[i][j] :
                visited[i][j] = 1
                a, b, visited = bfs(i, j)
                represent.append([len(F[a][b]), -B[a][b], a, b]) # 전파자의 신봉음식 길이, 대표자 신앙심 음수, x좌, y좌

    # 저녁
    represent = sorted(represent) # 전파 순서 정하기
    no_send = [] # 오늘 전파 못하는 대표 학생 모음
    cnt = 0
    for rep in represent :

        a, b = rep[2], rep[3]
        if [a, b] in no_send : continue # 전파 못함

        x = B[a][b] -1 # 간절함
        direct = B[a][b] % 4
        B[a][b] = 1
        food = F[a][b]
        # 전파 시작
        nx, ny = a + dx[direct], b + dy[direct] # 전파 대상자의 위치
        while 0<=nx<N and 0<=ny<N and x>0 :
            if F[nx][ny] == food :
                nx += dx[direct]
                ny += dy[direct]
                continue

            if x > B[nx][ny] :
                F[nx][ny] = food
                x -= (B[nx][ny] + 1)
                B[nx][ny] += 1
            elif x <= B[nx][ny] :
                tmp_food = sum_food(F[nx][ny] + food) # 이거 똑바로된 로직 처리는 다른 함수에서 하기
                F[nx][ny] = tmp_food
                B[nx][ny] += x
                x = 0

            # 전파 당한 학생은 당일에 전파 못함
            no_send.append([nx, ny])

    # 5. 각 날의 신앙심 총합 출력  (TCM-TC-TM-CM-M-C-T 순으로) - BFS
    # CMT, CM, CT, MT, C, M, T

    output = [0] * 7
    for i in range(N):
        for j in range(N):
            if F[i][j] == 'CMT' : output[0] += B[i][j]
            elif F[i][j] == 'CT' : output[1] += B[i][j]
            elif F[i][j] == 'MT': output[2] += B[i][j]
            elif F[i][j] == 'CM': output[3] += B[i][j]
            elif F[i][j] == 'M': output[4] += B[i][j]
            elif F[i][j] == 'C': output[5] += B[i][j]
            elif F[i][j] == 'T': output[6] += B[i][j]

    print(*output)