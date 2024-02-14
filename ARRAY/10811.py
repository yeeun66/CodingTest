# 배열 연습용
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 방법은 i j로 나타내고, 
# 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. (1 ≤ i ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.

N, M = map(int, input().split())

a = list()
for k in range(N):
    a.append(k+1)

i, j = [], []
for k in range(M) :
    b = list(map(int, input().split()))
    i.append(b[0])
    j.append(b[1])

for k in range(M) :
    a[i[k] - 1: j[k]] = reversed(a[i[k] -1 : j[k]]) # [i, j) 이므로 j + 1 해줘야 함
    
print(*a) # *a : 리스트의 각 요소를 개별적으로 가져와서 인자로 전달 (기억하기)