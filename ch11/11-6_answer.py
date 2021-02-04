# 무지의 먹방 라이브

# 이 문제는 시간이 적게 걸리는 음식부터 확인하는 '탐욕적 접근 방식'으로 해결할 수 있다.
# 모든 음식을 시간 기준으로 정렬한 뒤에, 시간이 적게 걸리는 음식부터 제거해 나가는 방식을 이용하면 된다.
# 이를 위해 '우선순위 큐'를 이용하여 구현할 수 있는데, 문제를 풀기 위해 고려해야 하는 부분이 많아서 까다로울 수 있다.

import heapq


def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1 (다음에 먹을 음식이 없다는 뜻이니까)
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 사용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 시간
    previous = 0
    # 남은 음식의 수
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0]) - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1     # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


food_times = [8, 6, 4]
k = 15
print(solution(food_times, k))