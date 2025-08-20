# 사다리 조작
# i번 세로선의 결과가 i번이 나오도록, 추가해야하는 가로선 갯수의 최솟값 구하기
'''
로직
0. 사다리를 2차원 배열에서 관리할 아이디어 (H+1) x (N) 크기의 2차원 배열로 관리
    - 초기 보드 세팅: 사다리가 b, b+1로 이루어져있다면, 
        b: 오른쪽으로 가라고 표시(r) / b+1 : 왼쪽으로 가라고 표시(l)
    - 사다리 타기: 그래서 r또는 l을 만나면 그 방향으로 한칸 전진 후 한칸 아래로 내려가기
        그냥 빈칸일 경우 계속 한칸 아래로 내려가기
        경계 밖으로 넘어가면 그 열이 도착 번호가 됨

모든 j번 세로선의 결과가 j번이 나올 때 까지 아래를 반복 (추가할 다리의 갯수가 4미만일 때 까지 아래를 반복)
1. 놓을 수 있는 모든 가능한 곳 (두 가로선이 연속하거나 접하면 안됨)을 n만큼 탐색한다 (완탐) - bruteforce()
    - 원본 보드가 둘다 'o'인 칸만 가능

2. 각 탐색한 곳에 다리를 놓기 (원본 보드 복사해서 거기서 다리 추가) - install_bridge()
3. 모든 j번 세로선의 결과가 j번인지 탐색 - search_result()
    - 어느 하나의 j번의 결과가 j번이 아니라면, 바로 탐색 종료 후 다른 경우 탐색
    - 모든 탐색 결과가 다 j번이 나왔다면, n 출력 후 그냥 종료

4. n이 4이상이면 그냥 -1 출력 후 종료

'''
import sys; input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [['o' for _ in range(N)] for _ in range(H+1)]

for _ in range(M) : 
    a, b = map(int, input().split())
    board[a][b-1] = 'r'; board[a][b] = 'l'

candidate = []  # 후보 미리 저장해두기 
for i in range(1, H+1) : 
    for j in range(N-1) : 
        if board[i][j] == 'o' and board[i][j+1] == 'o':
            candidate.append((i, j))

def is_inrange(x, y) : 
    return 0<= x < H+1 and 0 <= y < N

def search_result(num, n_board) : 
    for j in range(N) : 
        nx, ny = 0, j
        while is_inrange(nx, ny) :
            if n_board[nx][ny] == 'r' : 
                ny += 1
            elif n_board[nx][ny] == 'l' : 
                ny -= 1
            nx += 1
        if j != ny : return 
    print(num)
    exit()

def install_bridge(num, lst) : 
    # 새로운 배열 깊은 복사보다는, 그냥 지금 몇개만 바꾼 후에 작업 끝나면 다시 빈칸으로 바꾸는게 더 효율적임
    for i, j in lst : 
        board[i][j] = 'r'
        board[i][j+1] = 'l'
    
    search_result(num, board)

    for i, j in lst : 
        board[i][j] = 'o'
        board[i][j+1] = 'o'

def bruteforce(num, idx) : 
    if num == 0 : 
        search_result(num, board)
        return
    
    if len(arr) == num : 
        install_bridge(num, arr)
        return 
    
    for a in range(len(candidate)) : 
        if idx < a : 
            arr.append((candidate[a]))
            bruteforce(num, a)
            arr.pop()

for n in range(4) : 
    arr = []
    bruteforce(n, -1) # 1

print(-1)