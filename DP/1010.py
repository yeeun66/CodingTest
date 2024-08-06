# 강 주변에 다리를 지을 것임
# 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다 (N ≤ M)
# 이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다
# 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
# 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.

# 조합) bCa
import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    com = math.comb(b,a)
    print(com)   