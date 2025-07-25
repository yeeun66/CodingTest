# 이차원 배열과 연산 
# A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간 구하기

'''
로직
각 초마다 R연산 또는 C 연산 수행

- A[r][c]에 들어있는 값이 k이면 현재 초 출력 후 종료

- 정렬 로직 : 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저 (등장 횟수 같다면 오름차순으로 수 정렬)
    ex) [3, 1, 1, 2] => [2, 1, 3, 1, 1, 2] 2한번, 3한번 1두번 

- 현재 행 갯수 vs 열 갯수 비교해서 아래 연산 수행 
1. R연산 (행 갯수 >= 열 갯수 일 때) 모든 행에 대해 정렬 수행
    - 각 행 마다 정렬 수행 후 원래 행에 덮어 씌우기
    - 모든 정렬 끝난 후 최대 행 크기 기준으로 모든 행이 변함
        - 이때 최대 행 크기 기록 => 이건 그럼 열의 갯수가 됨
        - 커진 곳에는 0이 채워짐

2. C연산 (행 갯수 < 열 갯수 일 때) 모든 열에 대해 정렬 수행
    - 시계 방향 90도 회전
    - R연산과 동일 수행
    - 반시계 방향 90도 회전 (복귀)

- 100초 후에도 종료 안되면 -1 출력 

'''

r, c, k = map(int, input().split())
r, c = r-1, c-1
A = []
for _ in range(3) : A.append(list(map(int, input().split())))

row, col = 3, 3 # 현재 행과 열의 갯수 

def operation(rr) :
    new_A = []
    m_size = 0
    for i in range(rr) : 
        num = [0] * 101
        tmp = []
        for a in A[i] : num[a] += 1 # 등장 횟수 세기 
        for n in range(1, 101) :
            if num[n] != 0 : 
                tmp.append((num[n], n)) # 처음에는 (등장횟수, 숫자) 순으로 넣음 
            tmp.sort() # 정렬 후, 튜플 순서 교환 
            fin = []
            for t in range(len(tmp)) :
                x, y = tmp[t]
                fin.append(y)
                fin.append(x)
        
        new_A.append(fin)
        m_size = max(m_size, len(fin))

    # 크기 조정 
    for i in range(rr) : 
        if len(new_A[i]) < m_size : 
            for _ in range(m_size-len(new_A[i])) :
                new_A[i].append(0)
    
    return new_A, m_size

def rotate(rr, cc) :
    new_A = [[0 for _ in range(rr)] for _ in range(cc)]

    for i in range(rr) : 
        tmp = A[i][:]
        for j in range(len(tmp)) : new_A[j][rr-1-i] = tmp[j]

    return new_A

def rotate_reverse(rr, cc) : # 그냥 반시계 90도가 아니라, 하나씩 넣어줘야 함 
    new_A = [[0 for _ in range(cc)] for _ in range(rr)]

    for i in range(cc) :
        tmp = A[i][:]
        for j in range(len(tmp)) : new_A[j][i] = tmp[j]

    return new_A
    
for s in range(101) :

    if 0<= r < row and 0 <= c < col : 
        if A[r][c] == k : 
            print(s)
            exit()
    
    if row >= col : 
        A, col = operation(row)
        row = len(A)
        
    else : 
        A = rotate(row, col)
        row = len(A) 
        A, row = operation(row)
        col = len(A) 
        
        A = rotate_reverse(row, col)

print(-1)