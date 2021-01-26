# 퀵 정렬
# 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다.
# '피벗'은 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 말한다.
# '호어 분할 방식'은 리스트에서 첫 번째 데이터를 피벗으로 정하는 방식이다.

# 피벗을 설정한 뒤에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 그다음 큰 데이터와 작은 데이터의 위치를 서로 교환하고, 두 값이 엇갈린 경우에는 '작은 데이터'와 '피벗'의 위치를 서로 변경한다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)

# 퀵 정렬은 '재귀 함수'와 동작 원리가 같기 때문에, 재귀 함수를 활용한 구현으로 간결하게 표현할 수 있다.
# 퀵 정렬이 끝나는 조건은 현재 리스트의 데이터 개수가 1개인 경우이다.

# 퀵 정렬의 평균 시간 복잡도는 O(NlogN)이고, 최악의 경우에는 O(N^2)이다.
# 즉 '이미 데이터가 정렬되어 있는 경우'에는 매우 느리게 동작한다.

