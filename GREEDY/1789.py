# 수들의 합
# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마?

s = int(input())
sum = 0
i = 0
while sum <= s :
    i += 1
    sum += i
i -= 1
print(i)