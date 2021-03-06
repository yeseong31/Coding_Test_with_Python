# 떡볶이 떡 만들기

# 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형의 문제
# '파라메트식 서치': 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제라면 이진 탐색으로 결정 문제를 해결하면서 범위를 좁혀갈 수 있다.

# 절단기의 높이(탐색 범위)는 1부터 10억까지의 정수 중 하나인데, 이처럼 큰 수를 보면 당연하다는 긋이 가장 먼저 이진 탐색을 떠올려야 한다.

# 일반적으로 이 문제와 같은 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 구현하지 않고 반복문을 이용하여 구현하면 더 간결하다.

# --------------------------------------------------------------------------------------------------------------------
# 떡의 개수(N)와 요청한 떡의 길이(M) 입력
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 총 길이 계산
        if x > mid:
            total += (x - mid)
    # 떡의 총 길이가 기준 미달이라면 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 총 길이가 기준치 이상이라면 덜 자르기(오른쪽 부분 탐색)
    else:
        start = mid + 1
        result = mid    # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result를 기록

print(result)