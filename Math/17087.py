# 수빈이는 동생 N명과 숨바꼭질을 하고 있다. 수빈이는 현재 점 S에 있고, 동생은 A1, A2, ..., AN에 있다.
# 수빈이는 걸어서 이동을 할 수 있다. 수빈이의 위치가 X일때 걷는다면 1초 후에 X+D나 X-D로 이동할 수 있다. 
# 수빈이의 위치가 동생이 있는 위치와 같으면, 동생을 찾았다고 한다.
# 모든 동생을 찾기위해 D의 값을 정하려고 한다. 가능한 D의 최댓값을 구해보자.

# 풀이법: 간격들의 최대공약수 구하기
# 원래는 S와 가장 가까운 Ai 와의 간격을 사용하려 했으나, 이러면 그 간격으로 다른 곳에 접근하지 못하는 문제 발생
# 따라서 A에 S까지 넣어준 후, 오름차순 정렬한다.
# 이후 총 배열 갯수 -1 만큼의 간격을 구한 후, 그 간격들의 최대 공약수가 정답임
    # 이제 여러개의 차이들 중 최대공약수를 어케 구하냐
    # 모든 수들의 gcd 다 구해야 함 (하나씩 pop해가면서 하면 됨)

import sys
import math
input = sys.stdin.readline

N, S = map(int, input().split())
A = list(map(int, input().split())) # 동생들 위치

A.append(S)
arr = sorted(A)
diff = []
for i in range(len(arr)-1) :
    gap = arr[i+1] - arr[i]
    diff.append(gap)

if len(diff) == 1 : print(diff[0])
else : 
    result = -1
    while diff : 
        if diff : a = diff.pop()
        if result == -1 : result = diff.pop()
        result = math.gcd(a, result)
    print(result)