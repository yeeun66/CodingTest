# 큐빙
"""
로직
주어지는 명령 (돌릴면, 방향)에 대해 회전 수행
0. 배열 관리 (deque로 관리)
    - 큐브의 한면을 3x3 배열로 생각
    - 큐브 전체는 4x3의 전개도로 생각

1. 회전 로직
(1) L+ L-
    - 전개도에서 왼, 오를 제외한 세로 영역에 대해서 0번째 열들의 원소를 회전
    - (+) 위쪽으로 회전 3 -> 2 -> 1 -> 0 -> 3
    - (-) 아래쪽으로 회전 3-> 0 -> 1 -> 2 -> 3
(2) R+ R-
    - 전개도에서 왼, 오를 제외한 세로 영역에 대해서 2번째 열들의 원소를 회전
    - (+) 위쪽으로 회전 3 -> 2 -> 1 -> 0 -> 3
    - (-) 아래쪽으로 회전 3-> 0 -> 1 -> 2 -> 3
(3) F+ F-
    - 전개도에서 앞, 뒤를 제외한 영역에 대해서 2번째 행들의 원소를 회전
    - (+) 오른쪽으로 회전 w -> b -> y -> g -> w
    - (-) 왼쪽으로 회전 w-> g -> y -> b -> w
(4) B+ B-
    - 전개도에서 앞, 뒤를 제외한 영역에 대해서 0번째 행들의 원소를 회전
    - (+) 오른쪽으로 회전 w -> b -> y -> g -> w
    - (-) 왼쪽으로 회전 w-> g -> y -> b -> w
(5) U+ U-
    - 전개도에서 위, 아래를 제외한 영역에 대해서 0번째 행들의 원소를 회전
    - (+) 오른쪽으로 회전 r -> b -> o -> g -> r
    - (-) 왼쪽으로 회전 r-> g -> o -> b -> r
(6) D+ D-
    - 전개도에서 위, 아래를 제외한 영역에 대해서 2번째 행들의 원소를 회전
    - (+) 오른쪽으로 회전 r -> b -> o -> g -> r
    - (-) 왼쪽으로 회전 r-> g -> o -> b -> r

2. 각 TC마다 윗면의 9칸 값 출력 white 배열
"""

# 근데 사실 전개도로 안하고, 6면 다 따로 배열 만들어도 되긴함 -> 이게 더 편할 것 같아서 이 방법으로 바꿈 

# 고려하지 않은게 있었다.. 큐브 돌리면 배열도 돌아감
    # 돌린면은 해당 방향으로 배열 회전도 함 - roate_arr로 돌리기

# 또 고려하지 않은것!! 통째로 함 -> 근데 행 단위니까 통째로 행 해도 되잖아 

from collections import deque
orange = [['o' for _ in range(3)] for _ in range(3)]
green = [['g' for _ in range(3)] for _ in range(3)]
yellow = [['y' for _ in range(3)] for _ in range(3)]
blue = [['b' for _ in range(3)] for _ in range(3)]
red = [['r' for _ in range(3)] for _ in range(3)]
white = [['w' for _ in range(3)] for _ in range(3)]

def left_right(s, r, lr):
    # s번째 열들의 원소 방향에 따라 회전
    if lr == 'R' :
        if r == '+' : r = '-'
        else : r = '+'

    if r == '+' :
        tmp_org = [o[:] for o in orange]
        for i in range(3) :
            orange[i][s] = yellow[i][s]
            yellow[i][s] = red[i][s]
            red[i][s] = white[i][s]
            white[i][s] = tmp_org[i][s]

    else : 
        tmp_white = [w[:] for w in white]
        for i in range(3) :
            white[i][s] = red[i][s]
            red[i][s] = yellow[i][s] 
            yellow[i][s] = orange[i][s]
            orange[i][s] = tmp_white[i][s]

    return orange, yellow, red, white

def front_back(s, r, fb): # back일때도 바라보는 기준으로 시계 방향이므로 방향 반대임
    # s번째 행들의 원소 방향에 따라 회전
    if fb == 'B' :
        if r == '+' : r = '-'
        else : r = '+'

    tmp_blue = [b[:] for b in blue]
    if r == '+' :
        blue[s] = white[s]
        white[s] = green[s]
        green[s] = yellow[s]
        yellow[s] = tmp_blue[s]
    else :
        blue[s] = yellow[s]
        yellow[s] = green[s]
        green[s] = white[s]
        white[s] = tmp_blue[s]
    
    return blue, white, green, yellow

def up_down(s, r, ud):
    # s번째 행들의 원소 방향에 따라 회전
    if ud == 'D' :
        if r == '+' : r = '-'
        else : r = '+'

    tmp_blue = [b[:] for b in blue]
    if r == '+' :
        blue[s] = orange[s]
        orange[s] = green[s]
        green[s] = red[s]
        red[s] = tmp_blue[s]
    else : 
        blue[s] = red[s]
        red[s] = green[s]
        green[s] = orange[s]
        orange[s] = tmp_blue[s]

    return blue, red, green, orange

def roate_arr(d, arr) :
    new_arr = [a[:] for a in arr]

    if d == '+' : # 시계 
        for i in range(3) :
            for j in range(3) :
                new_arr[i][j] = arr[j][2-i]
    
    else : # 반시계 
        for i in range(3) :
            for j in range(3) :
                new_arr[i][j] = arr[2-j][i]

    return new_arr

T = int(input())
for _ in range(T) :
    n = int(input())
    cmd = list(map(str, input().split()))
    # tc 마다 초기화 
    orange = [['o' for _ in range(3)] for _ in range(3)]
    green = [['g' for _ in range(3)] for _ in range(3)]
    yellow = [['y' for _ in range(3)] for _ in range(3)]
    blue = [['b' for _ in range(3)] for _ in range(3)]
    red = [['r' for _ in range(3)] for _ in range(3)]
    white = [['w' for _ in range(3)] for _ in range(3)]

    for i in range(n):
        side, rot = cmd[i]
        if side == 'L' : 
            orange, yellow, red, white = left_right(0, rot, 'L')
            green = roate_arr(rot, green)
        elif side == 'R' : 
            orange, yellow, red, white = left_right(2, rot, 'R')
            blue = roate_arr(rot, blue)
        elif side == 'F' : 
            blue, white, green, yellow = front_back(2, rot, 'F')
            red = roate_arr(rot, red)
        elif side == 'B' : 
            blue, white, green, yellow = front_back(0, rot, 'B')
            orange = roate_arr(rot, orange)
        elif side == 'U' : 
            blue, red, green, orange = up_down(0, rot, 'U')
            white = roate_arr(rot, white)
        elif side == 'D' : 
            blue, red, green, orange = up_down(2, rot, 'D')
            yellow = roate_arr(rot, yellow)
        
        ### 디버깅
        # if n == 4 :
        #     print('='*7)
        #     for w in white : 
        #         print(''.join(w))
    for w in white : print(''.join(w))
    ### 디버깅
    # for g in green : print(''.join(g))

