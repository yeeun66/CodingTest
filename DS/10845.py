# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
from collections import deque
import sys

a = deque()

N = int(input())

for _ in range(N) :
    string = sys.stdin.readline().split()
    if string[0] == 'push' :
        a.append(string[1])
    elif string[0] == 'pop' :
        if len(a) == 0 :
            print("-1")
        else :
            p = a.popleft()
            print(p)
    elif string[0] == 'size' :
        print(len(a))
    elif string[0] == 'empty' :
        if len(a) == 0 :
            print("1")
        else : print("0")
    elif string[0] == 'front' :
        if len(a) == 0 :
            print("-1")
        else :
            print(a[0])
    elif string[0] == 'back' :
        if len(a) == 0 :
            print("-1")
        else :
            print(a[-1])