# 부품 찾기 (p.197)

# 다량의 데이터 검색은 이진 탐색 알고리즘을 이용해 효과적으로 처리할 수 있다.

# N개의 부품을 번호를 기준으로 정렬하고 M개의 찾고자 하는 부품이 각각 매장에 존재하는지 검사하면 된다.
# 부품을 찾는 과정과 부품 정렬의 과정을 거친 이진 탐색의 시간 복잡도는 O((M + N)logN)이다.

# --------------------------------------------------------------------------------------------------------------------
# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
# 이진 탐색을 수행하기 위해 사전에 정렬 수행
array.sort()

# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
