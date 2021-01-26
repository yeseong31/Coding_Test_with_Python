# 계수 정렬
# 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
# 모든 데이터가 양의 정수일 때, 데이터의 개수가 N, 데이터 중 최댓값이 K일 때 O(N + K)를 보장하는 알고리즘
# 다만, 계수 정렬은 '데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때'만 사용할 수 있다.
# 이러한 특징을 가지는 이유는, 계수 정렬을 이용할 때는 '모든 범위를 담을 수 있는 크기의 리스트(배열)를 선언'해야 하기 때문이다.

# 계수 정렬은, 먼저 가장 큰 데이터와 가장 작은 데이터의 범위가 모두 담길 수 있도록 하나의 리스트를 생성한다.
# 리스트의 모든 데이터가 0이 되도록 초기화하며, 그다음 데이터를 하나씩 확인하며 데이터의 값과 동일한 인덱스의 데이터를 1씩 증가시키면 된다.
# 리스트에는 각 데이터가 몇 번 등장했는지 그 횟수가 기록된다.

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)):  # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

# 계수 정렬은 모든 데이터가 양의 정수인 경우 데이터의 개수를 N, 데이터 중 최댓값의 크기를 K라고 할 때, O(N + K)의 시간 복잡도를 가진다.
# 따라서 데이터의 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 '기수 정렬'과 더불어 가장 빠르게 동작한다.
# 하지만 계수 정렬은 때에 따라서 심각한 비효율성을 초래할 수도 있다.

