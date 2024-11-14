# 후위 표기식(postfix)과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.
# 계산 결과를 소숫점 둘째 자리까지 출력한다.

# 입력
# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# 출력: 6.20

# postfix: ABC*+DE/- 
# infix: (A + (B * C)) - (D / E)

# 로직: 
# 문자에 해당 숫자 대응부터 해주기 <- 이걸 지금 해결 못함
# 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다,
# ==> 0에는 A에 해당하는 값, 1에는 B에 해당하는값 , 2에는 C ...이 주어진다,
    # stk 만큼 반복
    # 아스키 코드 차이로 해당 인덱스에 접근 후 그 값을 넣어줌
    
# postfix 계산법: 
# 아래를 스택 엠티까지 반복
# 1. 피연산자면 결과 스택에 넣음
# 2. 연산자면 현재 결과 스택의 탑원소 2개를 꺼내서 해당 연산 진행. 이후 연산된 값 다시 스텍에 넣음
# -- 결과 스택의 값은 결국 하나만 남기 때문에 그거 출력

import sys
input = sys.stdin.readline
N = int(input())
stk = list(map(str, input().strip()))
out = []
num = []

for i in range(N) :
    x = input().strip()
    num.append(x)

for i in range (len(stk)): 
    if stk[i] >= 'A' and stk[i] <= 'Z' :
        index = ord(stk[i]) - ord('A') # A와의 아스키코드 차이로 인덱스 결정
        stk[i] = num[index]
    
# print(stk)

top1, top2 = 0, 0
stk = stk[::-1] # 뒤집어서 pop
while stk : 
    temp = stk.pop()
    if temp == '+' :
        top1 = out.pop()
        top2 = out.pop()
        out.append(top2+top1)
    elif temp == '-' :
        top1 = out.pop()
        top2 = out.pop()
        out.append(top2-top1)
    elif temp == '*' :
        top1 = out.pop()
        top2 = out.pop()
        out.append(top2*top1)
    elif temp == '/' :
        top1 = out.pop()
        top2 = out.pop()
        out.append(top2/top1)
    else: 
        out.append(int(temp))

if out : result = float(out.pop())
print("%0.2f"%result) # 소수점 둘째 자리까지 출력 