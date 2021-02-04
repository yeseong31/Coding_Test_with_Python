# 만들 수 없는 금액

# 정렬을 이용한 그리디 알고리즘으로 해결할 수 있는 문제
# 동전에 대한 정보가 주어졌을 때, 화폐 단위를 기준으로 오름차순 정렬한 뒤 1부터 차례대로 특정한 금액을 만들 수 있는지 확인하면 된다.
# 1부터 target - 1까지의 모든 금액을 만들 수 있다고 가정해보자. 우리는 화폐 단위가 작은 순서대로 동전을 확인하며,
# 현재 확인하는 동전을 이용하여 target 금액 또한 만들 수 있는지 확인하면 된다.
# 만약 target 금액을 만들 수 있다면, target 값을 업데이트하는(증가시키는) 방식을 이용한다.

# 구체적으로 현재 상태를 '1부터 target - 1까지의 모든 금액을 만들 수 있는 상태'라고 보자.
# 이때 매번 target인 금액도 만들 수 있는지(현재 확인하는 동전의 단위가 target 이햐인지) 체크하는 것이다.
# 만약 해당 금액을 만들 수 있다면, target의 값을 업데이트(현재 상태를 업데이트)하면 된다.

# ---------------------------------------------------------------------------------------------------------------------
# <예시> --- N = 4 / 화폐 단위 1, 2, 3, 8
# [step 0] 처음에는 금액 1을 만들 수 있는지 확인, target = 1
# [step 1] target = 1을 만족할 수 있는지 확인. 화폐 단위 1인 동전이 있으므로 이를 이용하면 target 만족. target = 1 + 1 = 2
# [step 2] target = 2를 만족할 수 있는지 확인. 화폐 단위 2인 동전이 있으므로 이를 이용하면 target 만족. target = 2 + 2 = 4
# [step 3] target = 4를 만족할 수 있는지 확인. 화폐 단위 3인 동전이 있으므로 이를 이용하면 target 만족. target = 4 + 3 = 7
# [step 4] target = 7을 만족할 수 있는지 확인. 화폐 단위가 8이므로 target을 만족할 수 없음. 따라서 정답은 7

# 이러한 원리를 이용하면, 단순히 동전을 화폐 단위 기준으로 정렬한 뒤에, 화폐 단위가 작은 동전부터 하나씩 확인하면서
# target 변수를 업데이트하는 방법으로 최적의 해를 구할 수 있다. 이 문제가 어렵다면 그리디 알고리즘 유형의 문제에 익숙해질 필요가 있다.

# ---------------------------------------------------------------------------------------------------------------------

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

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