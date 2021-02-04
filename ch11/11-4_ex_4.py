# 만들 수 없는 금액(p.314)

# N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for c in coins:
    if target < c:
        break
    target += c

print(target)

# 입력 예시 1
# 3
# 3 5 7
# 출력 예시 1
# 1

# 입력 예시 2
# 5
# 3 2 1 1 9
# 출력 예시 2
# 8