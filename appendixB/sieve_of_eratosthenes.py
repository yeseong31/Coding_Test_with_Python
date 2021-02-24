# 에라토스테네스의 체
# 여러 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘
# N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

# (1) 2부터 N까지의 모든 자연수를 나열한다.
# (2) 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
# (3) 남은 수 중에서 i의 배수를 모두 제거한다.(단, i는 제거하지 않는다.)
# (4) 더 이상 반복할 수 없을 때까지 (2)번과 (3)번 과정을 반복한다.

# 매 스텝마다 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾기는 하지만
# 이때 i는 N의 제곱근(가운데 약수)까지만 증가시켜 확인하면 된다.

import math

n = 1000
# 처음엔 모든 수가 소수(True)인 것으로 초기화(단, 0과 1은 제외)
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
   if array[i]:     # i가 소수인 경우(남은 수인 경우)
       # i를 제외한 i의 모든 배수를 지우기
       j = 2
       while i * j <= n:
           array[i * j] = False
           j += 1

# 모든 소수 출력
for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

# 에라토스테네스의 체 알고리즘은 O(NloglogN)의 시간 복잡도를 가지므로 매우 빠르다.
# 하지만 알고리즘을 수행할 때 N의 크기만큼 리스트를 할당해야 하므로
# 메모리 및 공간 복잡도 측면에서는 비효율적일 수 있다.
