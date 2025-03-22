# 연산자 끼워넣기 
# N개의 수와 N-1개의 연산자가 주어졌을 때, 
# 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램

# 되는 경우의 수 다해봐야 할 것 같음 - 백트래킹

# 1. 입력 받기 (수의 갯수 N, N개의 수열 arr, 4가지 연산자 개수 배열 oper_count)
# 2. 연산자가 총 5개라면 [[+, 0], [+, 1], [-, 2], [*,3], [/, 4]] 이런식으로 저장 > compose
# 3. 백트래킹 구현
    # 3-1. 구성한 operator 배열이 N-1개가 되면, 
        # 해당 배열과 arr배열 이용해 계산 후, 
        # 최솟값과 최대값에 각각 update
    # 3-2. 재귀로 operator 구성하기
        # 0부터 N-1까지 반복
            # 해당 인덱스 즉 compose[i] = (+, 0)이 operator에 없다면, 튜플 추가
            # 재귀 호출
            # operator에서 하나 pop

# Python3으로 제출하면 시간초과, Pypy3으로 제출하면 정답 뜸
    # 아마 모든 경우 탐색해서 그런 것 같은데.. 
     
N = int(input())
arr = list(map(int, input().split()))
oper_count = list(map(int, input().split()))

compose = []
indx = 0
for i in range(4) :
    if i == 0 : s = '+'
    elif i == 1 : s = '-'
    elif i == 2 : s = '*'
    else: s = '/'
    
    for _ in range(oper_count[i]) :
        compose.append((s, indx))
        indx += 1

def backtracking() :
    global max_value, min_value
    if len(operator) == N-1 :
        value = arr[0]
        idx = 1 # 현재 연산할 숫자를 가리킬 인덱스
        for i in range(N-1) :
            if operator[i][0] == '+' : value += arr[idx]
            elif operator[i][0] == '-' : value -= arr[idx]
            elif operator[i][0] == '*' : value *= arr[idx]
            else : 
                if value < 0 : 
                    value = -1 * value
                    value //= arr[idx]
                    value = -1 * value
                else : value //= arr[idx]
            
            idx += 1
        
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        
        return
    
    for i in range(N-1) : 
        if compose[i] not in operator : 
            operator.append(compose[i])
            backtracking()
            operator.pop()

max_value, min_value = -1000000000, 1000000000
operator = []

backtracking()
print(max_value)
print(min_value)