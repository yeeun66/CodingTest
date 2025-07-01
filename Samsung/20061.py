# 모노미노도미노 2
# 2시간 10분 
"""
로직
0. 배열 관리
    - 초록, 파랑 배열 따로 관리
    - 빨강 -> 다른 색으로 넣어주는 과정은 좌표 계산을 통해 진행
    - 빈칸은 0, 타일이 있는 칸은 1로

1. 입력으로 주어진 블록을 초록, 파랑에 최대한 경계쪽으로 밀어 넣기. insert_blue, insert_green
    - 초기 상태 
        - 초록색: 열 고정, 행만 계속 증가하며 다른 타일 있거나, 경계 벗어나기 직전까지 증가하다 멈춰서 고정
        - 파란색: 행 고정, 열만 계속 증가하며 다른 타일 있거나, 경계 벗어나기 직전까지 증가하다 멈춰서 고정

2. 초록색-가득찬 행이 있는지, 파란색-가득찬 열이 있는지 검사하고 처리 (가득찬 행.열이 없을 때까지 반복)
    (초록)
    - 가득찬 행 사라짐
    - 사라진 행의 위에 있는 블록이 사라진 행의 수만큼 아래로 이동
    (파랑)
    - 가득찬 열 사라짐
    - 사라진 열 왼쪽 블록이 사라진 열의 수만큼 오른쪽으로 이동
    (공통)
    - 사라진 행 또는 열의 수 만큼 점수를 획득

3. 특별 칸 처리 
    (초록색의 0, 1번 행)
    - 해당 칸에 블록이 있으면, 블록이 있는 행의 수만큼(최대2개) 아래에서 부터 행의 타일이 사라짐
    - 사라졌다면, 사라진 행의 수만큼 모든 블록이 아래로 이동
    (파란색의 0,1번 열)
    - 해당 칸에 블록이 있으면, 블록이 있는 열의 수만큼(최대2개) 오른쪽 열부터 타일이 사라짐
    - 사라졌다면, 사라진 열의 수만큼 모든 블록이 오른쪽으로 이동

4. 출력:
    - 얻은 점수
    - 파랑 초록에 타일이 들어있는 칸의 개수

"""
N = int(input())
blk = []
for _ in range(N) : blk.append(list(map(int, input().split())))

green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(6)] for _ in range(4)]
score = 0

# 열은 고정, 행만 다룰거임
    # t =1, 2 일 경우 행은 그냥 x로 다루면 됨
    # t =3일 경우 행을 x+1로 일단 다루기
def insert_green(block) : 
    t, x, y = block
    if t < 3 : nx = 0
    else : 
        nx = 1
    ny = y

    while True:
        if nx >= 5 : break
        if t == 1 and green[nx+1][ny] > 0  : break
        if t == 2 and (green[nx+1][ny] > 0 or green[nx+1][ny+1] > 0)  : break
        if t == 3 and green[nx+1][ny] > 0  : break
        nx += 1
    
    if t == 1 : green[nx][ny] = 1
    elif t == 2 : 
        green[nx][ny] = 1
        green[nx][ny+1] = 1
    else : 
        green[nx][ny] = 1
        green[nx-1][ny] = 1
    
    return green

# 행은 고정, 열만 다룰거임
    # t =1, 3 일 경우 열은 그냥 y로 다루면 됨
    # t =2 일 경우 행을 y+1로 일단 다루기    
def insert_blue(block) :
    t, x, y = block
    if t == 1 or t == 3 : ny = 0
    else : 
        ny = 1
    nx = x

    while True:
        if ny >= 5 : break
        if t == 1 and blue[nx][ny+1] > 0  : break
        if t == 2 and blue[nx][ny+1] > 0  : break
        if t == 3 and (blue[nx][ny+1] > 0 or blue[nx+1][ny+1] > 0)  : break
        ny += 1
    
    if t == 1 : blue[nx][ny] = 1
    elif t == 2 : 
        blue[nx][ny] = 1
        blue[nx][ny-1] = 1
    else : 
        blue[nx][ny] = 1
        blue[nx+1][ny] = 1

    return blue

# 모든 행에 대해서 합이 4인지 체크 
    # 합이 4라면 해당 행은 가득참
    # 해당 행은 모두 0으로 처리
    # 사라진 행 번호 리스트에 저장
    # 위 리스트를 가지고 사라진 행 위에 있는 모든 블록들을 사라진 행의 수만큼 아래로 이동 (x좌표만 활용)
# 근데 이제 가득찬 행이 없을 때 까지 반복
def check_fill_row(s):
    
    new_green = [g[:] for g in green]
    fill_list = []
    for i in range(6) :
        if sum(green[i]) == 4 : 
            fill_list.append(i)
            for j in range(4) : 
                new_green[i][j] = 0

    if not fill_list : return new_green, False, s

    if fill_list : 
        cnt = len(fill_list)
        s += cnt 
        th = fill_list[0]
        for i in range(th-1, -1, -1) :
            for j in range(4) :
                new_green[i+cnt][j] = green[i][j]
                new_green[i][j] = 0
    
    return new_green, True, s

# 모든 열에 대해서 합이 4인지 체크 
    # 합이 4라면 해당 열은 가득참
    # 해당 열은 모두 0으로 처리
    # 사라진 열 번호 리스트에 저장
# 위 리스트를 가지고 사라진 열 위에 있는 모든 블록들을 사라진 열의 수만큼 오른쪽으로 이동 (y좌표만 활용)
# 근데 이제 가득찬 열이 없을 때 까지 반복
def check_fill_col(s):
    
    new_blue = [b[:] for b in blue]
    fill_list = []
    for j in range(6) : # 열
        sums = 0
        for i in range(4) : # 행 
            sums += blue[i][j]

        if sums == 4 :
            fill_list.append(j)
            for i in range(4) : new_blue[i][j] = 0


    if not fill_list : return new_blue, False, s

    if fill_list : 
        cnt = len(fill_list)
        s += cnt
        th = fill_list[0]
        for j in range(th-1, -1, -1) :
            for i in range(4) :
                new_blue[i][j+cnt] = blue[i][j]
                new_blue[i][j] = 0
    
    return new_blue, True, s

# (초록색의 0, 1번 행)
    # - 해당 칸에 블록이 있으면, 블록이 있는 행의 수만큼(최대2개) 아래에서 부터 행의 타일이 사라짐
    # - 사라졌다면, 사라진 행의 수만큼 모든 블록이 아래로 이동
def special_row() : 
    new_green = [g[:] for g in green]
    cnt = 0
    for i in range(2) : 
        for j in range(4) :
            if green[i][j] > 0 : 
                cnt += 1
                break
    
    if not cnt : return new_green

    new_green[5] = [0, 0, 0, 0]
    if cnt == 2 : new_green[4] = [0, 0, 0, 0]

    for i in range(5-cnt, -1, -1) : 
        for j in range(4) :
            new_green[i+cnt][j] = green[i][j]
            new_green[i][j] = 0
    
    return new_green

# (파란색의 0,1번 열)
    # - 해당 칸에 블록이 있으면, 블록이 있는 열의 수만큼(최대2개) 오른쪽 열부터 타일이 사라짐
    # - 사라졌다면, 사라진 열의 수만큼 모든 블록이 오른쪽으로 이동

def special_col() : 
    new_blue = [b[:] for b in blue]
    cnt = 0
    for j in range(2) : 
        for i in range(4) :
            if blue[i][j] > 0 : 
                cnt += 1
                break
    
    if not cnt : return new_blue

    for i in range(4) : 
        new_blue[i][5] = 0
    if cnt == 2 : 
         for i in range(4) : 
            new_blue[i][4] = 0

    for j in range(5-cnt, -1, -1) : 
        for i in range(4) :
            new_blue[i][j+cnt] = blue[i][j]
            new_blue[i][j] = 0
    
    return new_blue


#### Main ####
for n in range(N) :
    # print('- '*10, n, ' -'*10) # 디버깅 
    
    green = insert_green(blk[n])
    blue = insert_blue(blk[n])

    is_fill = True
    while is_fill : 
        green, is_fill, score = check_fill_row(score)
    is_fill = True
    while is_fill : 
        blue, is_fill, score = check_fill_col(score)

    green = special_row()
    blue = special_col()

print(score)
total = 0
for g in green : total += sum(g)
for b in blue : total += sum(b)
    
print(total)