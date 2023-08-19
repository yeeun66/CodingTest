# 보물
# S = A[0] × B[0] + ... + A[N-1] × B[N-1]
# A의 수를 재배열. B에 있는 수는 재배열X => S의 최솟값 구하기
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

sorted_a = sorted(a)
sorted_b = sorted(b)
sorted_a.reverse()

s = 0
for i in range(n) :
    s += sorted_a[i] * sorted_b[i]
print(s)