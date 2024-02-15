# 아직 하는 중

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
#  다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.

# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력

# 정렬 + 이분 탐색
import sys

def binary_search(data, target):
    data.sort()
    for i in range(len(target)) :
        st = 0
        end = len(data)
        v = int(target[i])
        print("v: ", v)
        exist = 0
        while st <= end :
            mid = (st + end) // 2
            if data[mid] == v : 
                print("1")
                exist = 1
                break
            elif data[mid] < v : 
                st = mid + 1
            else :
                end = mid -1
        if exist == 0 : print("0")

    return

N = map(int, sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

M = map(int, sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

# print(a)
# print(b)
binary_search(a, b)