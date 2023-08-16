# 회의실 배정
# 최대 사용할 수 있는 회의의 최대 개수를 출력
n = int(input())
d = []
for i in range(n) :
    a, b = map(int, input().split())
    d.append((a,b))

d.sort()
interval = abs(d[0][1]- d[0][0])
max = 0

while n > 0 and abs(d[0][1]- d[0][0]) <= interval :
    count = 1
    end = d[0][1]
    i = 1
    while True :
        start = d[i][0]
        if start >= end :
            count += 1
            end = d[i][1]
        i += 1
        if i == n : 
            n -= 1
            break
    if max < count : 
        max = count
    interval = abs(d[0][1]- d[0][0])
    d.pop(0)

print(max)