# 동전 0
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 함. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램

n, k  = map(int, input().split()) # 동전 종류, 동전 값의 합
min = 0 # 동전의 최소 갯수
a = []
for i in range(n) :
    num = int(input())
    if num <= k :
        a.append(num)

while k != 0 and a:
    if(k - a[-1] < 0) : 
        a.pop()
        continue
    min += k // a[-1] 
    k -= (k // a[-1]) * a[-1] 
    a.pop()

print(min)