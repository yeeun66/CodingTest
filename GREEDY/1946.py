# 신입 사원
# 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 
# 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.
# 이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입사원의 최대 인원수를 구하는 프로그램을 작성

# 배열에 입력 순으로 집어 넣고 배열 하나에 대해서 검사 --- 반복
# 위 로직이 아니고 현재 a, b 에 대해 모두 높은 사람이 나타나면 현재  a b 성적의 사람은 결코 카운트 될 수 없음
# 나머지 다 카운트
# 무조건 탈락 할 사람을 우선 제외하는게 빠름
# 시간 초과 ?? 정렬 후 내림차순으로 구해도 시간초과
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input())
    arr = sorted([tuple(map(int, input().split(' '))) for i in range(N)])
    count = 0

    temp = arr[0][1]
    for i in range(N):
        flag = 0
        if i == 0 : count += 1
        else :
            if temp > arr[i][1]: # temp 보다 더 작은게 나오면 그걸로 교체, 이제 이것보단 커야 함 -> 정렬 제대로 활용
                count += 1
                temp = arr[i][1]

    print(count)