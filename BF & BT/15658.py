# 연산자 끼워넣기 (2)

'''
로직 (시간초과)
입력 받은 숫자, 즉 피연산자는 최종 리스트의 짝수번째에 위치함
이제 홀수번째 위치 1, 3, ... 2*N-1 까지 위치에는 연산자 (+, -, *, /) 이 들어갈 것임
    - 이 연산자 위치는 백트래킹으로 모든 경우의 수 탐색
입력 받은 연산자는 갯수만큼 operator 리스트에 저장해둔다

1. operator 리스트에서 N-1개를 선택하는 백트래킹 수행
2. 백트래킹 함수:
    - 중복 없이 각 N-1개가 채워질 때 마다 calculate 함수에 그 배열 넣어, 계산 값의 최대와 최소 업데이트
3. calculate 함수
    - 리스트의 짝수번째에 피연산자는 이미 위치되어 있고, 홀수번째 위치 1, 3, ... 2*N-1 까지 위치에 연산자 넣어줌
    - 문제에서 시키는 대로 계산 수행
    - 최대, 최소 (전역변수) 업데이트 해줌
'''

'''
(시간초과 해결) - 모든 연산 만들어서 나중에 중복 걸러내는게 아니라, 애초에 중복을 만들면 안돼
중복 만들지 않는 백트래킹 방법
1. 상태 정의 - def backtrack(idx, add, sub, mul, div):
    함수 호출마다 하나의 상태를 대표하게 됨 
    예를 들어, 더하기 연산자가 몇 개 남았는지(add), 현재 사용된 연산자는 몇개인지 (idx)
2. 종료조건 설정
3. 다음 상태로 갈 수 있는 모든 경우 생각 - if add > 0:
    사용가능한 add 가 남아있다면, 사용 


'''
import sys
input = sys.stdin.readline

N = int(input())
operand = list(map(int, input().split()))
a, b, c, d = map(int, input().split())  # + - * /

f_list = [0] * (2*N-1)
j = 0
for i in range(N):
    f_list[j] = operand[i]
    j += 2

max_val = -int(1e9) # -10억
min_val = int(1e9) # 10억 

def calculate():
    global min_val, max_val

    result = f_list[0]
    for i in range(1, 2*N-1, 2):
        op = f_list[i]
        if op == '+': result += f_list[i + 1]
        elif op == '-': result -= f_list[i + 1]
        elif op == '*': result *= f_list[i + 1]
        elif op == '/':
            if result < 0:
                result = -(-result // f_list[i + 1])
            else:
                result = result // f_list[i + 1]

    max_val = max(max_val, result)
    min_val = min(min_val, result)

def backtrack(idx, add, sub, mul, div):
    if idx == N - 1:
        # print(f_list)
        calculate()
        return

    op_idx = 2 * (idx + 1) - 1  # 현재 연산자가 들어갈 위치 (홀수번째)
    if add > 0:
        f_list[op_idx] = '+'
        backtrack(idx + 1, add - 1, sub, mul, div) # depth 하나 늘리고, 방금 사용한 연산자 사용 갯수 하나 줄여
    if sub > 0:
        f_list[op_idx] = '-'
        backtrack(idx + 1, add, sub - 1, mul, div)
    if mul > 0:
        f_list[op_idx] = '*'
        backtrack(idx + 1, add, sub, mul - 1, div)
    if div > 0:
        f_list[op_idx] = '/'
        backtrack(idx + 1, add, sub, mul, div - 1)

backtrack(0, a, b, c, d)
print(max_val)
print(min_val)
