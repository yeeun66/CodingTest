# 큐빙
'''
로직 
큐브돌리는 사이트 (https://rubiks-cube-solver.com/fr/) 보고 디버깅함. 이거 없었으면 더 오래걸렸을 듯.. 
명령대로 모두 돌린 다음, 가장 윗 면의 색상 구하기
0. 배열 관리
    - 전개도로 하지 말고, 각 위치별 배열 따로 관리
    - up, down, front, back, left, right : 6면 (위, 아래, 앞, 뒤, 왼, 오)
    - 처음에는 각 면에 초기 색상 넣기 
1. 큐브 돌리기 (반시계는 시계 방향 3번이니까 굳이 구현X)
    '' U, D는 방향 서로 반대 ''
    (0) 본인 돌리기 (시계방향 or 시계 3번)
    (1) U (윗면 돌리기) => (front, back, left, right) 서로 0번째 행 바꾸기 
        - (+) 이면 => temp = front, front = right, right = back, back = left, left = temp
        - (-) 이면 => 위 3번 수행
    (2) D (아랫면 돌리기) => (front, back, left, right) 서로 2번째 행 바꾸기 
        - (+) 이면 => temp = right, right = front, front = left, left = back, back = temp
    (3) F (앞면 돌리기) => (up의 2번째 행, right의 0번째 열, down의 0번째 행, left의 2번째 열) 바꾸기 
        - (+) 이면 => temp = right, right = up, up = left, left = down, down = temp
    (4) B (뒷면 돌리기) => (up의 0번째 행, right의 2번째 열, down의 2번째 행, left의 0번째 열) 바꾸기 
        - (+) 이면 => temp = right, right = down, down = left, left = up, up = temp
    (5) L (왼쪽 돌리기) => (up의 0번째 열, front의 0번째 열, down의 0번째 열, back의 2번째 열) 바꾸기 
        - (+) 이면 => temp = up, up = back, back = down, down = front, front = temp
    (6) R (오른쪽 돌리기) => (up의 2번째 열, front의 2번째 열, down의 2번째 열, back의 0번째 열) 바꾸기 
        - (+) 이면 => temp = up, up = front, front = down, down = back, back = temp

'''

import copy
cube = [[] for _ in range(6)]
def init_() : 
    # cube = [[] for _ in range(6)]
    cube[0] = [['w' for _ in range(3)] for _ in range(3)] # up
    cube[1] = [['g' for _ in range(3)] for _ in range(3)] # left
    cube[2] = [['r' for _ in range(3)] for _ in range(3)] # front
    cube[3] = [['b' for _ in range(3)] for _ in range(3)] # right
    cube[4] = [['o' for _ in range(3)] for _ in range(3)] # back
    cube[5] = [['y' for _ in range(3)] for _ in range(3)] # down 
    
# print(cube)
def rotate_self(s, iterate) : 
    for _ in range(iterate) : 
        new_lst = [c[:] for c in cube[s]]
        for i in range(3) : 
            for j in range(3) : 
                cube[s][i][j] = new_lst[2-j][i]
    
def rotate_other(s, iterate) : 
    if s == 0 : # up
        for _ in range(iterate) : 
            origin_cube = copy.deepcopy(cube)
            cube[2][0] = origin_cube[3][0]; cube[3][0] = origin_cube[4][0]; cube[4][0] = origin_cube[1][0]; cube[1][0] = origin_cube[2][0]

    elif s == 5 : # down
        for _ in range(iterate) : 
            origin_cube = copy.deepcopy(cube)
            cube[3][2] = origin_cube[2][2]; cube[2][2] = origin_cube[1][2]; cube[1][2] = origin_cube[4][2]; cube[4][2] = origin_cube[3][2]

    elif s == 2 : # front
        for _ in range(iterate) : 
            origin_cube = copy.deepcopy(cube)
            for i in range(3) : 
                cube[0][2][i] = origin_cube[1][2-i][2]
                cube[1][i][2] = origin_cube[5][0][i]
                cube[5][0][i] = origin_cube[3][2-i][0]
                cube[3][i][0] = origin_cube[0][2][i]

    elif s == 4 : # back
        for _ in range(iterate) :
            origin_cube = copy.deepcopy(cube) 
            for i in range(3) : 
                cube[0][0][i] = origin_cube[3][i][2]
                cube[3][i][2] = origin_cube[5][2][2-i]
                cube[5][2][i] = origin_cube[1][i][0]
                cube[1][i][0] = origin_cube[0][0][2-i]

    elif s == 1 : # left
        for _ in range(iterate) :
            origin_cube = copy.deepcopy(cube) 
            for i in range(3) : 
                cube[0][i][0] = origin_cube[4][2-i][2]
                cube[4][i][2] = origin_cube[5][2-i][0]
                cube[5][i][0] = origin_cube[2][i][0]
                cube[2][i][0] = origin_cube[0][i][0]

    else : # right
        for _ in range(iterate) : 
            origin_cube = copy.deepcopy(cube)
            for i in range(3) : 
                cube[0][i][2] = origin_cube[2][i][2]
                cube[2][i][2] = origin_cube[5][i][2]
                cube[5][i][2] = origin_cube[4][2-i][0]
                cube[4][i][0] = origin_cube[0][2-i][2]

T = int(input())
for _ in range(T) : 
    init_() 
    n = int(input())
    cmd = list(map(str, input().split()))
    for i in range(n) : 
        side, d = cmd[i]
        if d == '+' : iters = 1
        else : iters = 3
        if side == 'U' : num = 0
        elif side == 'L' : num = 1
        elif side == 'F' : num = 2
        elif side == 'R' : num = 3
        elif side == 'B' : num = 4
        else : num = 5

        rotate_self(num, iters)
        rotate_other(num, iters)
        
        ## 디버깅 ## 
        # print(side, d)
        # for i in range(6) : 
        #     for c in cube[i] : print(c)
        #     print('-'*8)
        
    ## 정답
    for c in cube[0] : print(''.join(c))
