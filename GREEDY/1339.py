# 단어 수학
# 단어 수학 문제는 N개의 단어로 이루어져 있으며, 각 단어는 알파벳 대문자로만 이루어져 있다. 
# 이때, 각 알파벳 대문자를 0부터 9까지의 숫자 중 하나로 바꿔서 N개의 수를 합하는 문제이다. 
# 같은 알파벳은 같은 숫자로 바꿔야 하며, 두 개 이상의 알파벳이 같은 숫자로 바뀌어지면 안 된다.
# 예를 들어, GCF + ACDEB를 계산한다고 할 때, A = 9, B = 4, C = 8, D = 6, E = 5, F = 3, G = 7로 결정한다면, 
    # 두 수의 합은 99437이 되어서 최대가 될 것이다.
# N개의 단어가 주어졌을 때, 그 수의 합을 최대로 만드는 프로그램을 작성하라.

from collections import deque

N = int(input())
word = []
for _ in range(N) :
    word.append(deque(map(str, input())))

max_len = -1
for a in word :
    tmp = len(a)
    if tmp > max_len : max_len = tmp

for a in word :
    tmp = len(a)
    if tmp < max_len :
        diff = max_len - tmp
        for _ in range(diff) : a.appendleft('$')

dic = {}
number = 9 
for i in range(max_len) :
    for j in range(len(word)) : # 같은 자릿수 일 때, 즉 i가 같을 때에는 많이 등장한 순으로 높은 숫자 부여해야 함,,
        alpa = word[j][i]
        if alpa == '$' or alpa in dic : continue
        dic[alpa] = number
        number -= 1

result = 0
for a in word :
    tmp_word = ''
    for i in range(max_len) :
        if a[i] == '$' : continue
        tmp_word += str(dic[a[i]])
    result += int(tmp_word)

print(result)