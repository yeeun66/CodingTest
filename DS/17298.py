# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 
# 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다. 
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 
# 그러한 수가 없는 경우에 오큰수는 -1이다.

# 로직1
# 수열 A1 .. AN 에 대해 각각의 결과를 출력
# 1. 자신의 바로 오른쪽 부터 시작해서 자신 보다 큰 걸 만나면 바로 출력 후 break
# 2. 자신의 오른쪽에 큰 숫자를 발견 했는지 못했는지를 flag로 처리
# -- 마지막은 굳이 비교 안하고 그냥 -1 s출력 (어차피 오른쪽 없으니까)
# ==> 시간 초과 ... 

# 로직2 (스택을 써야하는 것 같다..) --> 성공
# 예시 3 5 2 7

# 입력 역순으로 하나씩 검사.
# 가장 뒤 7에 대하여, 현재 stack에 있는 값이 자신 보다 작으면 (혹은 empty이면) 자신의 인덱스에 -1 값을 넣는다. 
    # [이 때 새로운 ans 배열에 넣어줌]
# 그리고 이제 stack에 방금 검사한 7을 넣는다.
# 이제 그 다음 2를 검사한다. 
# 현재 stack에 top에는 2보다 큰 7이 있으므로 이 친구의 ans 인덱스에는 7을 넣는다.
# 그러고 stack에 2를 넣는다. 

# 이제 그 다음 5를 검사한다. 
# 현재 stack에 top에는 5보다 작은 2가 있으므로 2는 pop한다. 그러고 이제 stack의 top인 7이 5보다 크므로 5의 인덱스에는 7을 넣는다.
# 그러고 stack에 5를 넣는다. 

# 이제 그 다음 3을 검사한다. 
# 현재 stack에 top에는 3보다 큰 5가 있으므로 3의 인덱스에는 5을 넣는다.

# 그러고 ans를 출력한다. 

import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

a = a[::-1] # 역순으로 뒤집기
stack = []
ans = [-1 for _ in range(N)]

for i in range(N) : 
    # print("i: ", i, "   | stack: ", stack)
    if i == 0 or not stack: 
        stack.append(a[i])
        continue

    while stack :
        if a[i] < stack[-1] :
            ans[i] = stack[-1]
            break
        else : 
            stack.pop()
    
    stack.append(a[i])

ans = ans[::-1]
print(*ans)