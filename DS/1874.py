# 스택 수열

# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 
# 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
# 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
# 이를 계산하는 프로그램을 작성하라.

# - - - 로직 - - - 
# 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
# push 연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO

# 입력 받은 순서대로 정답 수열 ans 배열을 만들어 놓는다. 
# 출력 배열도 n개로 초기화 <- 여기서 +- 저장

# 오름 차순이니까 i= 1부터 n까지 현재 검사중인 정답 배열과 비교할건데
# - 일단 스택에 하나 넣어
#     - 출력 배열에 + 입력
#     - 현재 스택 마지막 원소와 일치하지 않으면 i 증가 시켜서 다시 스택에 넣어
#     - 현재 스택 마지막 원소와 일치하면 pop 하고 
#         - 출력 배열에 - 넣어
#         - 또 현재 스택 마지막과 일치하는지 확인후, 일치하면 pop하고 위 동작
#         - 일치하지 않으면 i증가후 다시 스택에 넣고 같은 동작~

# 최종 결과 판별: 반복문 끝났을 때 stack empty이면 output 배열 출력
# stack에 뭐가 있으면 “NO” 출력

import sys
input = sys.stdin.readline

n = int(input())
ans = [] # 정답 배열
output = [] # 출력 배열
stack = []
for _ in range(n) :
    x = int(input())
    ans.append(x)

index_ans = 0
for i in range(1, n+1):
    stack.append(i)
    output.append('+')
    if index_ans >= n : break
    while ans[index_ans] == stack[-1] : # 스택 마지막 원소와 정답과 일치
        x =  stack.pop()
        index_ans += 1
        output.append('-')
        if index_ans >= n or not stack: break

if stack : print("NO")
else: 
    for i in output: print(i)