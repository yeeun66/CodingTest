# 집합
import sys
input = sys.stdin.readline

s = set()
M = int(input())
for _ in range(M) :
    parts = input().split()
    cmd = parts[0]

    if len(parts) == 2 :
        x = int(parts[1])
        if cmd == 'add' :
            if x not in s :
                s.add(x)
        elif cmd == 'remove' :
            if x in s : s.remove(x)
        elif cmd == 'toggle' :
            if x in s : s.remove(x)
            else : s.add(x)
        elif cmd == 'check' :
            if x in s : print(1)
            else : print(0)

    else :
        if cmd == 'all' :
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        elif cmd == 'empty' :
            s = set()