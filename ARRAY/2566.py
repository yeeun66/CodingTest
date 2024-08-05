# <그림 1>과 같이 9×9 격자판에 쓰여진 81개의 자연수 또는 0이 주어질 때, 
# 이들 중 최댓값을 찾고 그 최댓값이 몇 행 몇 열에 위치한 수인지 구하는 프로그램을 작성

import sys
input = sys.stdin.readline

arr = []
for i in range(9) :
    arr.append(list(map(int, input().split())))

max = -1
flag_i = 0
flag_j = 0
for i in range(9) :
    for j in range(9) :
        if max < arr[i][j] :
            flag_i = i + 1
            flag_j = j + 1
            max = arr[i][j]

print(max)
print(flag_i, flag_j)