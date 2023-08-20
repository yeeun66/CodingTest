# 바이러스
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램
n = int(input())
edge = int(input())
count = -1
d = [[] for _ in ' '*(n+1)] 
for _ in range(edge) :
    x, y = map(int,input().split())
    d[x].append(y)
    d[y].append(x)
d = list(map(sorted, d))
for i in d :
    i.reverse()

visit = [0]*(n+1)
stk = [1]
while stk :
    top = stk.pop()
    if visit[top] : continue
    visit[top] = True
    stk.extend(d[top])
    count += 1
print(count)