# 볼링공 고르기 (p.315)

# 볼링공의 개수 N, 공의 최대 무게 M
# 두 사감은 서로 무게가 다른 볼링공을 고르려고 한다.
# 공의 번호는 1부터 순서대로 부여되며, 같은 무게의 둘 이상의 공은 서로 다른 공으로 간주한다.
# 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

from itertools import combinations

n, m = map(int, input().split())
data = list(map(int, input().split()))
comb = list(combinations(data, 2))

for c in comb:
    a, b = c
    if a == b:
        comb.remove(c)

print(len(comb))

# 입력 예시 1
# 5 3
# 1 3 2 3 2
# 출력 예시 1
# 8

# 입력 예시
# 8 5
# 1 5 4 3 2 4 5 2
# 출력 예시
# 25