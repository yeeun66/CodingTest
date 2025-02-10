# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
# 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다

# key 배열에 대해 할 수 있는 걸 다 해보고 되면 True, 모두 안되면 False 리턴
    # M, N 이 최대 20, 즉 20*20은 400이니까 완전 탐색으로도 시간 안에 무조건 가능

# 방법: (교재 518p 참고)
# 1. 완전 탐색을 수월하게 하기 위해 자물쇠 리스트의 크기를 3배 이상으로 변경하면 계산이 수월해진다.
#    가장 먼저 자물쇠를 크기가 3배인 새로운 리스트로 만들어 중앙 부분으로 옮긴다
# 2. 이제 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 차례대로 자물쇠의 모든 홈을 채울 수 있는지 확인하면 된다
#    즉 자물쇠 리스트에 열쇠 리스트의 값을 더한 뒤에, 더한 결과를 확인했을 때, 자물쇠 부분의 모든 값이 정확히 1인지를 확인하면 된다. 그렇다면 정확히 채운 것이다
#    위 구현은 check 함수로 진행
#    이후 다시 자물쇠에 맞지 않으면 다시 열쇠 빼줘야 함
# 3. 또한 효율적인 문제 풀이를 위해 rotate_matrix_90 함수를 구현한다 (가끔 쓰이니 메모해두자)

# 2차원 리스트 90도 회전
def rotate_matrix_90(key) :
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for i in range(m) :
        for j in range(m) :
            result[j][m-i-1] = key[i][j] 
    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock) :
    n = len(new_lock) // 3 # 원래 자물쇠 크기
    for i in range(n, n*2) :
        for j in range(n, n*2) :
            if new_lock[i][j] != 1 : return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    new_lock = [[0] * (n*3) for _ in range(n*3)]
    
    for i in range(n) : # 자물쇠를 크기가 3배인 새로운 리스트로 만들어 중앙 부분으로 옮김
        for j in range(n) :
            new_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4) : # 4번 회전
        key = rotate_matrix_90(key)
        for x in range(2*n) :
            for y in range(2*n) : # x, y는 변화하는 원점
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] += key[i][j]
                # 열 수 있는지 검사
                if check(new_lock) == True : return True
                
                # 자물쇠에 열쇠 다시 빼기
                for i in range(m) :
                    for j in range(m) :
                        new_lock[x+i][y+j] -= key[i][j]
            
    return False