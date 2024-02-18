# 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
# 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
# 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.

# 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

# stack 문제인듯
# 여는 괄호면 stack에 push
# 닫는 괄호면 stack의 top 원소 pop
# 닫는 괄호 남아있는데 stack에 아무것도 없으면 반복 종료 -> NO
# 반복문 이후 stack이 empty면 -> YES. 아니면 -> NO

T = int(input())

for _ in range(T) :
    stack = []
    flag = 0
    string = list(map(str, input()))
    for i in range(len(string)):
        if string[i] == '(' :
            stack.append(string[i])
        else :
            if len(stack) == 0 : # 스택이 비었으면
                print("NO")
                flag = 1
                break
            else : pop = stack.pop()
    if flag != 1 :
        if len(stack) == 0 :
            print("YES")
        else : print("NO")