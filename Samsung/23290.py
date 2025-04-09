# 마법사 상어와 복제
# 차분하게 생각
# 3시간 10분 걸림

# 로직
    # 1. 복제 마법 시전
        # 초기 배열 copy_fish에 저장 해뒀다가, 5번에서 추가하기

    # 2. 물고기 이동 move_fish()
        # 이동할 정보 업데이트
            # 현재 방향 부터 반시계 45도 돌면서
            # 상어가 있는 칸, 냄새가 있는 칸, 범위를 벗어나는 칸이 아니라면, 이동 가능
            # 이동 가능하면, 이동할 물고기 정보 (nx, ny, nd) 물고기 배열(new_fish)에 저장
            # 8번 돌았는데 불가능하면, 그대로 물고기 배열(new_fish)에 저장
        # 이동하기
            # 새로운 격자(new_arr)에 물고기 갯수만 카운트한거 저장
            # new_arr, new_fish 리턴

    # 3. 상어 이동 move_shark()
        #  가능한 이동 방법(64가지) 중 제외되는 물고기의 수가 가장 많은 방법 선택
            # 백트래킹으로 미리 구현한 조합 사용해서 최대값 업데이트 하며 하기
            # 미리 구현한 comb도 이미 사전 순으로 되어있음

        # 선택된 방법으로 물고기 먹기 ex) [상, 우, 우]
            # 한칸씩 가며 eaten에 먹은 좌표만 저장해둠
        # 이동한 상어의 좌표 shark에 업데이트 [nx, ny]
        # eaten을 리턴

    # 4. 격자에서 물고기 냄새 관리 (update_smell)
        # smell_arr에서 모든 0이상인 값에 대해 -1
        # smell_arr에 3번에서 먹힌 물고기 좌표(eaten 사용)에 냄새를 2로 남김
        # 물고기 정보 삭제 (eaten 사용)
            # fish에서는 eaten에 해당하는 좌표 다 삭제
            # arr에서는 eaten에 해당하는 좌표의 값 다 0으로 만들기

    # 5. 1에서 저장해둔 copy_fish로 현재 arr과 fish 업데이트
        # fish에는 그냥 copy_fish 추가
        # arr에는 copy_fish에서 해당하는 좌표에 물고기 수 카운트

    # 6. len(fish) 출력
# 시간초과 해결 : 무조건 필요할 때 말고는 deepcopy 막 쓰지마
import copy

fdx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
fdy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

sdx = [0, -1, 0, 1, 0] # 0 상 좌 하 우
sdy = [0, 0, -1, 0, 1]

M, S = map(int, input().split())

fishes = [] # (fx, fy, d)
shark = [0, 0] # (sx, sy)
for _ in range(M) : fishes.append(list(map(int, input().split())))
shark = list(map(int, input().split()))

arr = [[0 for _ in range(4) ]for _ in range(4)]
smell_arr = [[0 for _ in range(4) ]for _ in range(4)]

for fish in fishes :
    fish[0], fish[1] = fish[0]-1, fish[1]-1
    x, y = fish[0], fish[1]
    arr[x][y] += 1

shark[0], shark[1] = shark[0]-1, shark[1]-1

# 64개 조합 미리 저장해두기
def backtrack(path, comb) :
    if len(path) == 3 :
        comb.append(path[:]) # 복사본을 저장
        return

    for i in range(1, 5) :
        path.append(i)
        backtrack(path, comb)
        path.pop()
comb = []
backtrack([], comb)

def move_fish(old_arr, old_fishes) :
    sx, sy = shark[0], shark[1]  # 상어가 있는 칸
    new_fish = []
    new_arr = [[0 for _ in range(4)] for _ in range(4)]

    for fish in old_fishes :
        x, y, d = fish

        possible = False
        for i in range(8) :
            nd = (d+8-i) % 8
            if nd == 0 : nd = 8
            nx, ny = x + fdx[nd], y + fdy[nd]
            if nx == sx and ny == sy : continue # 상어 있는 칸이면 못감
            if 0<= nx < 4 and 0<= ny < 4 :
                if smell_arr[nx][ny] == 0:
                    possible = True
                    new_fish.append([nx, ny, nd])
                    break
        if not possible : new_fish.append([x, y, d])

    for fish in new_fish :
        x, y = fish[0], fish[1]
        new_arr[x][y] += 1

    return new_arr, new_fish

def move_shark(shark, arr) :
    eaten = []
    select = [0, 0, 0]
    max_v = -1

    for comb3 in comb : # 최선의 방법 선택
        x, y = shark[0], shark[1]
        cnt = 0
        out_of_range = 0
        new_arr = copy.deepcopy(arr)
        for i in range(3) :
            nd = comb3[i]
            nx, ny = x + sdx[nd], y + sdy[nd]
            if 0 <= nx < 4 and 0 <= ny < 4 :
                cnt += new_arr[nx][ny]
                new_arr[nx][ny] = 0
                x, y = nx, ny
            else :
                out_of_range = 1
                break

        if out_of_range : continue

        if max_v < cnt :
            max_v = cnt
            select = comb3

    # 선택된 방법으로 물고기 먹기 ex) [상, 우, 우]
    x, y = shark[0], shark[1] # 현재 상어
    for i in range(3) :
        nd = select[i]
        nx, ny = x + sdx[nd], y + sdy[nd]
        x, y = nx, ny
        if arr[x][y] > 0 : # 물고기가 존재해야 먹음
            eaten.append([nx, ny])

        if i == 2 : shark = [nx, ny]

    return shark, eaten

def update_smell(smell_arr, eaten) :

    for i in range(4) : # 냄새 -1
        for j in range(4) :
            if smell_arr[i][j] > 0 : smell_arr[i][j] -=1

    for eat in eaten : # 방금 죽은 물고기 냄새 남기기
        x, y = eat
        smell_arr[x][y] = 2

    return smell_arr

#### 마법 시전 ####
for _ in range(S) :
    copy_fishes = copy.deepcopy(fishes) # 1. 복제 마법 시전
    arr, fishes = move_fish(arr, fishes) # 2. 물고기 이동
    shark, eaten = move_shark(shark, arr) # 3. 상어 이동
    smell_arr = update_smell(smell_arr, eaten) # 4. 냄새 관리

    # 4-2. 물고기 정보 삭제 (eaten 사용)
    for eat in eaten :
        x, y = eat
        for i in range(len(fishes)) :
            if fishes[i][0] == x and fishes[i][1] == y :
                fishes[i] = [-1, -1, -1]
        arr[x][y] = 0

    # 5. 복제 시전
    for fish in copy_fishes :
        fishes.append(fish)
        x, y = fish[0], fish[1]
        arr[x][y] += 1

    fishes.sort(reverse=True)
    l = len(fishes)
    while True :
        if fishes[-1][0] != -1 : break
        fishes.pop()
        l -= 1

print(len(fishes))