# 제로
# 재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.
# 재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
# 스택

k = int(input())
stack = []

for _ in range(k) :
    temp = int(input())
    if temp != 0 :
        stack.append(temp)
    else :
        if len(stack) != 0 :
            stack.pop()

print(sum(stack))