# 순열과 조합

# 순열
# 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것

import itertools

data = [1, 2]
for x in itertools.permutations(data, 2):
    print(list(x))

# 조합
# 서로 다른 n개에서 순서에 상관없이 서로 다른 r개를 선택하는 것

data = [1, 2, 3]
for x in itertools.combinations(data, 2):
    print(list(x), end=' ')

# 이때 permutations(), combinations() 함수를 호출하여 나온 결과의 원소들은
# 리스트 형태가 아니므로 list()를 이용하는 것이 일반적이다.
