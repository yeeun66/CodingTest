# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램
# 첫째 줄에 주어지는 명령의 수 N
import sys

N = int(input())

stack = []
for _ in range(N) :
    string = sys.stdin.readline().split()
    if string[0] == 'push' :
        stack.append(string[1])
    elif string[0] == 'pop' :
        if len(stack) == 0 :
            print("-1")
        else :
            p = stack.pop()
            print(p)
    elif string[0] == 'size' :
        print(len(stack))
    elif string[0] == 'empty' :
        if len(stack) == 0 :
            print("1")
        else : print("0")
    elif string[0] == 'top' :
        if len(stack) == 0 :
            print("-1")
        else :
            print(stack[-1])