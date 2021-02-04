# 모험가 길드(p.311)

n = int(input())
fear = list(map(int, input().split()))  # 공포도
result = 0  # 총 그룹 수

fear.sort(reverse=True)
i = 0
while i < len(fear):
    # i의 수만큼 끊어서 그룹의 수를 셈
    result += 1
    i += fear[i]

print(result)

# 입력 예시
# 5
# 2 3 1 2 2
# 출력 예시
# 2