# 기수 정렬
# 기수 정렬은 정렬 순서상 앞서고 뒤섬을 판단하는 비교 연산을 하지 않는다.
# 기수 정렬은 정렬 알고리즘의 이론상 한계인 O(NlogN)을 극복할 수 있는 유일한 알고리즘이다.
# 하지만 '적용할 수 있는 범위가 제한적'이며, 길이가 같은 데이터들을 대상으로는 정렬이 가능하지만, 그렇지 않은 경우 효율성이 떨어진다.
# N진수 정수의 정렬을 위해서는 총 N개의 '버킷'이 필요하다. 정렬 대상은 값에 해당하는 버킷으로 이동하게 된다.

from math import log


# 현재 자릿수(d)와 진법(base)에 맞는 숫자 변환
# ex) 102, d = 1, base = 10, : 2
def get_digit(number, d, base):
  return (number // base ** d) % base


# 자릿수 기준으로 counting sort
# A : input array
# position : 현재 자릿수, ex) 102, d = 1 : 2
# base : 10진수라면 base = 10
def counting_sort_with_digit(A, d, base):
    # k : ex) 10진수의 최대값 = 9
    k = base - 1
    B = [-1] * len(A)
    C = [0] * (k + 1)
    # 현재 자릿수를 기준으로 빈도수 세기
    for a in A:
        C[get_digit(a, d, base)] += 1
    # C 업데이트
    for i in range(k):
        C[i + 1] += C[i]
    # 현재 자릿수를 기준으로 정렬
    for j in reversed(range(len(A))):
        B[C[get_digit(A[j], d, base)] - 1] = A[j]
        C[get_digit(A[j], d, base)] -= 1
    return B


def radix_sort(list, base=10):
    # 입력된 리스트 가운데 최대값의 자릿수 확인
    digit = int(log(max(list), base) + 1)
    # 자릿수 별로 counting sort
    for d in range(digit):
        list = counting_sort_with_digit(list, d, base)
    return list